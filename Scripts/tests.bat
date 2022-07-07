@echo off
cls
g++ ./Project/*.cpp -o creditcardvalidator
move .\creditcardvalidator.exe .\Tests\creditcardvalidator.exe
python .\Tests\runTests.py > tests.log
rm .\Tests\creditcardvalidator