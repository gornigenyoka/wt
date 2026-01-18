@echo off
echo ========================================
echo Solana Common Wallet Finder
echo ========================================
echo.

REM Try pip first, then python -m pip as fallback
echo [1/2] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Trying alternative method...
    python -m pip install -r requirements.txt
    if errorlevel 1 (
        echo.
        echo ERROR: Failed to install dependencies!
        echo Make sure Python is installed and pip is available.
        echo.
        echo Try installing Python from: https://www.python.org/downloads/
        echo Make sure to check "Add Python to PATH" during installation.
        pause
        exit /b 1
    )
)

echo.
echo [2/2] Starting Streamlit app...
echo.
echo The app will open in your browser automatically.
echo Press Ctrl+C to stop the app when you're done.
echo.

REM Try streamlit first, then python -m streamlit as fallback
streamlit run app.py
if errorlevel 1 (
    python -m streamlit run app.py
    if errorlevel 1 (
        echo.
        echo ERROR: Failed to start Streamlit!
        echo Make sure all dependencies were installed correctly.
        pause
        exit /b 1
    )
)

pause
