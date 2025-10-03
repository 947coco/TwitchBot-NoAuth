@echo off

echo This Installation script should take no more than 1 min
echo please, be patient

:: Install python
python --version 
if %ERRORLEVEL% == 0 (
    echo python is already installed
) else (
    winget install Python 3.13 --accept-package-agreements
)

:: Create python virtual environnement and install pyttsx3 in it
python -m venv TwitchBotDependencies
call TwitchBotDependencies\Scripts\activate.cmd
pip install pyttsx3 keyboard
deactivate

:: create an START script in Documents folder
(
echo @echo off 
echo call %cd%\Scripts\activate.cmd
echo python .\scripts\main.py 
echo pause 
) > %USERPROFILE%\Documents\START_TWITCH_BOT.cmd

echo Go check your Documents folder, the START_TWITCH_BOT.cmd file should be ready !
echo You can of course move it wherever you want
echo And do not forget to write your twitch channel name in config.txt !
pause 

:: delete this file
del "%0"
