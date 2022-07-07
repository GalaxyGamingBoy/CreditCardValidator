import sys
import os

if sys.platform == "linux" or sys.platform == "linux2":
    os.system("bash ./Scripts/build.sh")
elif sys.platform == "darwin":
    os.system("sh ./Scripts/build.sh")
elif sys.platform == "win32":
    os.system(".\\Scripts\\build.bat")
