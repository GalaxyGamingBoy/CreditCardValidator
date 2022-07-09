import sys
import os
import filecmp

if sys.platform == "linux" or sys.platform == "linux2":
    os.system("bash ./Scripts/tests.sh")
elif sys.platform == "darwin":
    os.system("sh ./Scripts/tests.sh")
elif sys.platform == "win32":
    os.system(".\\Scripts\\tests.bat")

if filecmp.cmp('./tests.log', './Tests/tests.passed'):
    print("Tests Passed")
else:
    print("Tests Failed, See tests.log")
