@echo off
cls
g++ .\Project\*.cpp -o out
echo ----- ----- -----
echo   Build  Output
echo ----- ----- -----
.\out.exe
rm .\out.exe