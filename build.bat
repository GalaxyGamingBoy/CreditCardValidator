@echo off
cls
g++ .\Project\*.cpp -o out
echo ----- ----- -----
echo   Build  Output
echo ----- ----- -----
.\out.exe %0
rm .\out.exe