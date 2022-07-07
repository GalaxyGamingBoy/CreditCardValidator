g++ ./Project/*.cpp -o creditcardvalidator
mv ./creditcardvalidator ./Tests/creditcardvalidator
python ./Tests/runTests.py
rm ./Tests/creditcardvalidator