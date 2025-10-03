@echo off
python --version 
if %ERRORLEVEL% == 0 (
    echo python is already installed
) else (
    winget install Python 3.13 --accept-package-agreements
)
set PATH_VENV=%USERPROFILE%\Documents\TwitchBot
set PATH_START_FILE=%USERPROFILE%\Documents\START_TWITCH_BOT.bat
python -m venv %PATH_VENV%
call %PATH_VENV%\Scripts\activate.bat
pip install pyttsx3
echo @echo off > %PATH_START_FILE%
echo call %PATH_VENV%\Scripts\activate.bat >> %PATH_START_FILE%
echo python .\scripts\main.py >> %PATH_START_FILE%
echo pause >> %PATH_START_FILE%
start %PATH_START_FILE%
del "%0"