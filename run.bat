@echo off
chcp 65001 > nul
echo Запуск сервера CryptoWatch...

:: Переход в папку скрипта
cd /d "%~dp0"

:: Активация виртуального окружения (если используется .venv)
if exist .venv\Scripts\activate.bat (
    call .venv\Scripts\activate.bat
)

:: Автоматическое открытие сайта в браузере через 2 секунды после старта бэкенда
start "" "http://127.0.0.1:8000/"

:: Запуск бэкенда FastAPI
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

pause