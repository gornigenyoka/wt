import streamlit as st
import pandas as pd
from collections import Counter
import io

st.set_page_config(
    page_title="Solana Common Wallet Finder",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Solana Common Wallet Finder")
st.markdown("**Upload CSVs of early buyers from multiple tokens to find overlapping wallets.**")

# File uploader
uploaded_files = st.file_uploader(
    "Upload CSV files (one per token)",
    type=['csv'],
    accept_multiple_files=True,
    help="Each CSV should have a 'wallet' column with Solana addresses"
)

if uploaded_files:
    st.success(f"✅ Loaded {len(uploaded_files)} file(s)")
    
    # Process each file
    file_data = {}
    all_wallets_list = []
    # Mapping: lowercase_wallet -> original_case_wallet (first occurrence)
    wallet_case_map = {}
    
    for uploaded_file in uploaded_files:
        try:
            # Read CSV
            df = pd.read_csv(uploaded_file)
            
            # Check if 'wallet' column exists
            if 'wallet' not in df.columns:
                st.warning(f"⚠️ {uploaded_file.name}: 'wallet' column not found. Skipping.")
                continue
            
            # Get original wallets (strip whitespace, remove empty)
            original_wallets = df['wallet'].astype(str).str.strip()
            original_wallets = original_wallets[original_wallets != '']
            original_wallets = original_wallets[original_wallets != 'nan']
            
            # Basic validation: remove addresses that are too short (likely invalid)
            original_wallets = original_wallets[original_wallets.str.len() >= 20]
            
            # Create lowercase versions for matching
            wallets_lower = original_wallets.str.lower()
            
            # Store original case mapping (use first occurrence for each lowercase version)
            for orig, lower in zip(original_wallets, wallets_lower):
                if lower not in wallet_case_map:
                    wallet_case_map[lower] = orig
            
            # Convert to set for fast operations (using lowercase)
            wallet_set = set(wallets_lower)
            
            # Store file data
            file_data[uploaded_file.name] = {
                'wallets': wallet_set,
                'count': len(wallet_set)
            }
            
            # Add to flat list for recurring analysis (using lowercase)
            all_wallets_list.extend(list(wallet_set))
            
            # Display file info
            st.info(f"📊 **{uploaded_file.name}**: {len(wallet_set)} unique wallets")
            
        except Exception as e:
            st.error(f"❌ Error processing {uploaded_file.name}: {str(e)}")
            continue
    
    # Only proceed if we have valid files
    if file_data:
        st.divider()
        
        # Compute intersection (common to ALL tokens)
        if len(file_data) > 1:
            # Start with first file's wallets
            common_wallets = file_data[list(file_data.keys())[0]]['wallets'].copy()
            
            # Intersect with all other files
            for file_name, data in list(file_data.items())[1:]:
                common_wallets &= data['wallets']
            
            # Display intersection results
            st.header("🔸 Wallets in ALL Tokens")
            if common_wallets:
                st.success(f"Found {len(common_wallets)} wallet(s) common to all {len(file_data)} tokens")
                
                # Convert to original case for display
                common_wallets_original = [
                    wallet_case_map.get(wallet, wallet) 
                    for wallet in sorted(common_wallets)
                ]
                
                # Create DataFrame for display (with original case)
                common_df = pd.DataFrame({
                    'wallet': common_wallets_original
                })
                st.dataframe(common_df, use_container_width=True, hide_index=True)
                
                # Download button for intersection
                csv_buffer = io.StringIO()
                common_df.to_csv(csv_buffer, index=False)
                st.download_button(
                    label="📥 Download common_to_all.csv",
                    data=csv_buffer.getvalue(),
                    file_name="common_to_all.csv",
                    mime="text/csv"
                )
            else:
                st.warning(f"No wallets found in all {len(file_data)} tokens")
        else:
            st.info("ℹ️ Upload at least 2 files to find common wallets")
        
        st.divider()
        
        # Compute top recurring wallets (appear in ≥N tokens)
        st.header("🔸 Top Recurring Wallets")
        
        # Number input for minimum token appearances
        col1, col2 = st.columns([1, 3])
        with col1:
            min_appearances = st.number_input(
                "Minimum CSV files wallet must appear in:",
                min_value=2,
                max_value=len(file_data),
                value=2,
                step=1,
                help=f"Enter a number between 2 and {len(file_data)}. Shows wallets that appear in at least this many CSV files."
            )
        
        # Count occurrences
        wallet_counter = Counter(all_wallets_list)
        
        # Filter by minimum appearances
        recurring_wallets = {
            wallet: count 
            for wallet, count in wallet_counter.items() 
            if count >= min_appearances
        }
        
        if recurring_wallets:
            # Sort by count descending, then by wallet address
            sorted_recurring = sorted(
                recurring_wallets.items(),
                key=lambda x: (-x[1], x[0])
            )
            
            st.success(f"Found {len(sorted_recurring)} wallet(s) appearing in ≥{min_appearances} token(s)")
            
            # Convert to original case for display
            recurring_data = [
                (wallet_case_map.get(wallet_lower, wallet_lower), count)
                for wallet_lower, count in sorted_recurring
            ]
            
            # Create DataFrame (with original case)
            recurring_df = pd.DataFrame(
                recurring_data,
                columns=['wallet', 'token_count']
            )
            st.dataframe(recurring_df, use_container_width=True, hide_index=True)
            
            # Download button for recurring wallets
            csv_buffer = io.StringIO()
            recurring_df.to_csv(csv_buffer, index=False)
            st.download_button(
                label=f"📥 Download recurring_wallets.csv",
                data=csv_buffer.getvalue(),
                file_name="recurring_wallets.csv",
                mime="text/csv"
            )
        else:
            st.warning(f"No wallets found appearing in ≥{min_appearances} token(s)")
        
        # Summary statistics
        st.divider()
        st.header("📈 Summary Statistics")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Files", len(file_data))
        with col2:
            st.metric("Total Unique Wallets", len(set(all_wallets_list)))
        with col3:
            if len(file_data) > 1:
                st.metric("Common to All", len(common_wallets) if 'common_wallets' in locals() else 0)
            else:
                st.metric("Common to All", "N/A")
    else:
        st.warning("⚠️ No valid files processed. Please ensure CSVs have a 'wallet' column.")
else:
    st.info("👆 Please upload one or more CSV files to begin analysis.")
    
    # Show example format
    with st.expander("📋 Expected CSV Format"):
        st.code("""wallet
9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM
5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1
...""", language="csv")
