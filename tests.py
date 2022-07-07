import sys
import os

if sys.platform == "linux" or sys.platform == "linux2":
    os.system("bash ./Scripts/tests.sh")
elif sys.platform == "darwin":
    os.system("sh ./Scripts/tests.sh")
elif sys.platform == "win32":
    os.system(".\\Scripts\\tests.bat")
