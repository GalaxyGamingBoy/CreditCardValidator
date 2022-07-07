import sys
import os

if len(sys.argv) > 1 and len(sys.argv) < 3:
    if sys.platform == "linux" or sys.platform == "linux2":
        os.system(f"bash ./Scripts/build.sh {sys.argv[1]}")
    elif sys.platform == "darwin":
        os.system(f"sh ./Scripts/build.sh {sys.argv[1]}")
    elif sys.platform == "win32":
        os.system(f".\\Scripts\\build.bat {sys.argv[1]}")
else:
    print("Usage: ./creditcardvalidator <CREDIT CARD NUMBER>")
