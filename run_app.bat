@echo off
echo Starting Cancer Diagnosis Statistical Analysis Application...
echo.
echo To run the application:
echo 1. Open Command Prompt or PowerShell
echo 2. Navigate to this directory
echo 3. Run: streamlit run app.py
echo.
echo Or use this batch file to start automatically...
echo.
cd /d "%~dp0"
"%~dp0..\.venv\Scripts\python.exe" -m streamlit run app.py
pause