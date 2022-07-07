import json
import os


def testCard(cardCodename):
    print(f"Testing {cardCodename} Cards: ")
    for i in testJSONData["cards"][cardCodename]:
        output = os.popen(f"./Tests/creditcardvalidator {i}").read()
        print(f"{cardCodename} - {i}: {output}")
    print("\n")


print("Running Credit Card Validator - Tests\n")

testJSONFile = open("./Tests/tests.json")
testJSONData = json.load(testJSONFile)
testJSONFile.close()

testCard("AMEX")
testCard("DINERS")
testCard("DISCOVER")
testCard("JCB")
testCard("MASTERCARD")
testCard("VISA")
