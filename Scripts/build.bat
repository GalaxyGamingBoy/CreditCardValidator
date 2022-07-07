@echo off
cls
g++ .\Project\*.cpp -o creditcardvalidator
echo ----- ----- -----
echo   Build  Output
echo ----- ----- -----
.\creditcardvalidator.exe %1
rm .\creditcardvalidator.exe