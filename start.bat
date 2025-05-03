@echo off
SETLOCAL

:: Вказати назву папки репозиторію
set REPO_DIR="twitchbot"

:: Перейти в директорію
cd /d "%~dp0%REPO_DIR%"

:: Запустити бота
echo Running bot.py...
python bot.py

pause