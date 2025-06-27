@echo off
echo ===== TimeMachine Setup Script (Python 3.13) =====

:: Step 1: Create virtual environment using Python 3.13
echo Creating virtual environment...
python -m venv .venv

:: Step 2: Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

:: Step 3: Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

:: Step 4: Install required packages
echo Installing dependencies...
pip install flask flask-cors transformers torch sentencepiece

:: Step 5: Run Flask backend
echo Running backend...
cd backend
python app.py

pause
