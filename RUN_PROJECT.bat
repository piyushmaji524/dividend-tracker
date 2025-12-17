@echo off
REM ============================================
REM Dividend Tracker - Project Runner
REM ============================================

color 0A
cls

echo.
echo ============================================
echo   DIVIDEND TRACKER - STOCK DIVIDENDS
echo ============================================
echo.
echo Starting the application...
echo.

REM Navigate to project directory
cd /d "d:\Digital Products\STOCK DEVIDENT"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Python is not installed!
    echo Please install Python from https://www.python.org
    echo.
    pause
    exit /b 1
)

REM Install/Update requirements
echo Installing dependencies...
pip install -q -r requirements.txt >nul 2>&1

REM Start the Flask application
echo.
echo ============================================
echo   APPLICATION STARTED SUCCESSFULLY!
echo ============================================
echo.
echo 🌐 Open your browser and go to:
echo    http://localhost:5000
echo.
echo 📱 Features:
echo    ✓ 50 Indian Companies
echo    ✓ Dividend Dates & Eligibility
echo    ✓ Sector Filters
echo    ✓ Company Details
echo    ✓ ROI Calculator
echo    ✓ Shareable Cards
echo.
echo ============================================
echo Press Ctrl+C to stop the server
echo ============================================
echo.

REM Run the Flask app
python app.py

pause
