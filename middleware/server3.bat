@echo off
:repeat
    C:\Python34\python.exe srvapp3.py
echo %errorlevel%
if %errorlevel% == 3 goto repeat