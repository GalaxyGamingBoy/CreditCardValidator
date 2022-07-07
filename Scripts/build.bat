@echo off
cls
g++ .\Project\*.cpp -o creditcardvalidator
echo ----- ----- -----
echo   Build  Output
echo ----- ----- -----
.\creditcardvalidator.exe %0
rm .\creditcardvalidator.exe