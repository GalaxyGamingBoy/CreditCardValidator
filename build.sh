clear
g++ ./Project/*.cpp -o creditcardvalidator
echo ----- ----- -----
echo   Build  Output
echo ----- ----- -----
./creditcardvalidator $1
rm ./creditcardvalidator
