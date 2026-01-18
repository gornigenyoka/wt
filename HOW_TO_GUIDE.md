# How to Find Common Wallets Across Multiple Tokens

This guide walks you through the complete workflow from getting a token call to finding overlapping wallets using this app.

## Overview

When someone posts a token call, you can find their wallet by:
1. Looking at early buyers on Solscan
2. Filtering transactions by time and value
3. Extracting wallet addresses
4. Comparing across multiple tokens to find common wallets

---

## Step-by-Step Workflow

### Step 1: Get the Token Information

When someone posts a token call:
- Note the **token contract address (CA)**
- Note the **date/time they posted the call**
- This is your "until date" - they likely bought before posting

### Step 2: Go to Solscan

1. Open [Solscan.io](https://solscan.io) in your browser
2. In the search bar, paste the **token contract address (CA)**
3. Press Enter or click search

### Step 3: Navigate to Activity/Transfers

1. On the token page, click on **"Activity"** tab 

### Step 4: Set Time Filter

1. Look for the **date/time filter** on the Activity page
2. Set the **"Until" date** to when the call was posted (or 1 day before to be safe)
3. Set the **"From" date** to a reasonable time before 
   - **Tip**: Start with a wider range, you can narrow it down later

### Step 5: Check Transaction Count

1. Look at how many transactions Solscan shows
2. **Important**: Solscan only displays up to **1,000 transactions**
3. If you see "1,000" or more, you need to filter further

### Step 6: Filter by Dollar Value (If Needed)

If you have more than 1,000 transactions:

1. Look for a **filter option** (usually a filter icon or dropdown)
2. Filter by **value** (e.g., $10, $50, $100)
3. This removes small transactions and helps you focus on significant buyers
4. Adjust until you have less than 1,000 transactions


### Step 7: Download CSV

1. On the Solscan Activity page, look for the **"Export CSV"** button
2. Click it to download the transaction data as CSV
3. Save the file with a descriptive name (e.g., `token_frog.csv`)

### Step 8: Prepare the CSV File

1. Open the downloaded CSV in Excel, Google Sheets, or any spreadsheet app
2. Find the **"from"** column (this contains the wallet addresses)
3. **Rename** the "from" column header to **"wallet"** (lowercase, exactly)
4. **Delete all other columns** - you only need the "wallet" column
5. Save the file

**Example of what your CSV should look like:**
```csv
wallet
9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM
5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1
7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU
```

### Step 9: Repeat for Multiple Tokens

1. Repeat Steps 2-8 for each token call you want to analyze
2. Create one CSV file per token
3. Name them clearly (e.g., `token_frog.csv`, `token_dog.csv`, `token_cat.csv`)

### Step 10: Use the App

1. **Start the app**: Double-click `run_app.bat` (Windows) or run `streamlit run app.py`
2. **Upload CSVs**: Click "Browse files" and select all your prepared CSV files
3. **View results**:
   - **Wallets in ALL Tokens**: Shows wallets that appear in every token (likely the caller's wallet)
   - **Top Recurring Wallets**: Shows wallets appearing in multiple tokens (adjust the minimum number)
4. **Download results**: Click the download buttons to save the results as CSV
5. You can start tacking the wallets, and copy if you'd like
---

## Example Scenario

**Scenario**: Someone posted a call for "FROG token" on January 15th at 2:00 PM

1. Token CA: `ABC123...`
2. Go to Solscan → Search token
3. Activity tab → Set filter:
   - From: January 14th
   - Until: January 15th, 2:00 PM
4. See 1,500 transactions → Filter by $50+ → Now 800 transactions
5. Download CSV
6. Open CSV → Rename "from" to "wallet" → Delete other columns
7. Save as `frog_token.csv`
8. Repeat for 2-3 other token calls
9. Upload all CSVs to app
10. Find wallets common to all tokens = likely the caller's wallet!

---

**Happy hunting! 🎯**
