@echo off
:start
python brain.py
echo Program terminated at %Date% %Time% with Error %ErrorLevel%
echo Press Ctrl-C if you don't want to restart automatically
ping -n 1 localhost
goto start