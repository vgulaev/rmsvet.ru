@echo off
:repeat
    python srvapp.py
if %errorlevel% == 3 goto repeat