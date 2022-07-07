clear
g++ ./Project/*.cpp -o creditcardvalidator
mv ./creditcardvalidator ./Tests/creditcardvalidator
python ./Tests/runTests.py > tests.log
rm ./Tests/creditcardvalidator