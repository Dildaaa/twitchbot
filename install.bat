@echo off
SETLOCAL

:: ==== Python ====
echo Installing Python...
curl -o python-installer.exe https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe
start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1

:: Python PATH
setx PATH "%PATH%;C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\Scripts;C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311"

:: Python
python --version
pip --version

:: Git
echo Installing Git...
curl -o git-installer.exe https://github.com/git-for-windows/git/releases/download/v2.44.0.windows.1/Git-2.44.0-64-bit.exe
start /wait git-installer.exe /SILENT

git --version

echo Cloning GitHub repository...
git clone https://github.com/Dildaaa/twitchbot

cd twitchbot
echo Installing Python dependencies...
pip install -r requirements.txt

echo All done!
pause
