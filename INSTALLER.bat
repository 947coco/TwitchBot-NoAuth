@echo off
python --version 
if %ERRORLEVEL% == 0 (
    echo python est deja installe
) else (
    winget install Python 3.13 --accept-package-agreements
)
python -m venv venv
call .\venv\Scripts\activate.bat
pip install pyttsx3
echo @echo off > LANCER.bat
echo call .\venv\Scripts\activate.bat >> LANCER.bat
echo python .\scripts\main.py >> LANCER.bat
echo pause >> LANCER.bat
start LANCER.bat
del "%0"