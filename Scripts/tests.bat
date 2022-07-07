@echo off
cls
g++ ./Project/*.cpp -o creditcardvalidator
move .\creditcardvalidator .\Tests\creditcardvalidator
python .\Tests\runTests.py > tests.log
rm .\Tests\creditcardvalidator