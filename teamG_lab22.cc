#include <iostream>
using namespace std;

int main()

{	
  float number;
  int divider;
	
  divider = 9;
	
  cout << "Hi there" << endl;
  cout << "Please input a number and then hit return" << endl;
  cin  >> number;
	
  number = number / divider;
 	
  cout << "Half of your number is " << number << endl;
	
  return 0;
}