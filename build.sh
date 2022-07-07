clear
g++ ./Project/*.cpp -o out
echo ----- ----- -----
echo   Build  Output
echo ----- ----- -----
./out $1
rm ./out
