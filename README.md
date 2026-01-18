# Solana Common Wallet Finder

A Streamlit web app that finds overlapping Solana wallet addresses across multiple token CSV files.

## Features

- Upload multiple CSV files (one per token)
- Find wallets common to ALL tokens (intersection)
- Find top recurring wallets (appear in ≥N tokens)
- Download results as CSV
- Clean, user-friendly interface

## Installation

### Windows (Easy Method):
**Just double-click `run_app.bat`** - it will install everything and start the app automatically!

### Manual Installation:

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
streamlit run app.py
```

## CSV Format

Each CSV file should have a single column named `wallet` (lowercase) with Solana wallet addresses:

```csv
wallet
9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM
5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1
...
```

## Usage

1. Open the app in your browser (usually http://localhost:8501)
2. Upload one or more CSV files using the file uploader
3. View results:
   - **Wallets in ALL Tokens**: Wallets that appear in every uploaded file
   - **Top Recurring Wallets**: Wallets appearing in at least N tokens (adjustable via slider)
4. Download results as CSV files

## Requirements

- Python 3.7+
- streamlit
- pandas
