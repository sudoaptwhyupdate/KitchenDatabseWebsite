#include <iostream>
#include <string>
using namespace std;



// using a C++ script because is it easier to have somthing that is a binary
// so that anybody on any machine can run somthing like this to setup the 
// project, just have to run this and the entire project will get setup

void windowsSetup();
void macSetup();

int main() {

  const char *starting_message = "\n@2022 Brendan Fineran, sudoaptwhyupdate\n"
                             "This script is made for Windows or MacOS only\n"
                             "Due to the fact that there are so many Linux\n"
                             "distributions, I've decided that if you want to\n"
                             "create your own setup script for your distribution\n"
                             "you are more than welcome to.\n\n"
                             "NOTE: THIS SCRIPT SHOULD BE RUN EVERYTIME YOU CREATE A\n"
                             "CLONE OF THE PROJECT SO THAT EVERYTHING YOU ARE WORKING WITH\n"
                             "IS UP TO DATE\n\n";

  cout << starting_message << endl;

  bool os_chosen = false;
  do {
    string os;
    cout << "Enter your operating system (W: Windows, M: MacOS): ";
    cin >> os;

    if (os == "W" || os == "Windows" || os == "w") {
      os_chosen = true;
      windowsSetup();
    } 
    else if (os == "Mac" || os == "macos" || os == "m" || os == "M" || os == "MacOS") {
      os_chosen = true;
      macSetup();
    }

  }while(os_chosen == false);

  return 0;

}

void windowsSetup() {
  cout << "You will need to install python from python.org";
  cout << "Make sure you add python pip to path, so that you can install\n packages\n";
  system("pip install flask");
  system("pip install sqlalchemy");
}

void macSetup() {
  cout << "\nYou will need to make sure that python has been installed";
  system("python3 -m pip install flask");
  system("python3 -m pip install sqlalchemy");
}
