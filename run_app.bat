@echo off
echo ========================================
echo Solana Common Wallet Finder
echo ========================================
echo.

echo [1/2] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies!
    echo Make sure Python is installed and pip is available.
    pause
    exit /b 1
)

echo.
echo [2/2] Starting Streamlit app...
echo.
echo The app will open in your browser automatically.
echo Press Ctrl+C to stop the app when you're done.
echo.

streamlit run app.py

pause
