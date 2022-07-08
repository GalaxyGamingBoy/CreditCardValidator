#include <iostream>
#include <string>

// Functions Initialization
bool argumentValid(int argumentCount);
void printUsage();
bool isCreditCardValid(std::string cardNumber);
std::string recognizeCreditCardCompany(int firstDigit);

int main(int argc, char const *argv[]) {
  if (!argumentValid(argc)) {
    printUsage();
    return 1;
  }

  if (isCreditCardValid(argv[1])) {
    std::cout << "VALID ( " << recognizeCreditCardCompany(argv[1][0] - '0')
              << " )";
  } else {
    std::cout << "NOT VALID";
  }
  return 0;
}

// Check if arguments are valid
bool argumentValid(int argumentCount) {
  if (argumentCount > 1 && argumentCount < 3) {
    return true;
  }

  return false;
}

// Print Usage
void printUsage() {
  std::cout << "Usage: ./creditcardvalidator <CREDIT CARD NUMBER>" << std::endl;
}

// Check if credit card is valid with Luhn algorithm
bool isCreditCardValid(std::string cardNumber) {
  // RUN LUHN ALGORITHM
  std::string checkDigit(1, cardNumber[cardNumber.length() - 1]);
  int sum = 0;

  for (int i = cardNumber.length(); i >= 0; i--) {
    if (i % 2 == 0) {
      int value = cardNumber[i] - '0'; // Get number from char - 0 is 48
      value *= 2;                      // Double value
      while (value > 0) {
        int digitSelected = value % 10;
        sum += digitSelected;
        value /= 10;
      }
    } else {
      int value = cardNumber[i] - '0';
      sum += value;
    }
  }

  if (std::to_string(sum).back() == '0')
    return true;
  return false;
}

// Recognize credit card company
std::string recognizeCreditCardCompany(int firstDigit) {
  switch (firstDigit) {
  case 2:
    return "MASTERCARD";
  case 3:
    return "AMEX / DINERS / JCB";
  case 4:
    return "VISA";
  case 5:
    return "MASTERCARD";
  case 6:
    return "DISCOVER";
  default:
    return "UNKNOWN";
  }
}