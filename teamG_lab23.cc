#include <iostream>
#include <string>

using namespace std; 

/*struct ContactInfo{
	string firstName, lastName, address, city, state, zip, phone; 
}; 
or class 
now can create multiple ContactInfo 
*/

int main(){
	
	string firstName, lastName, address, city, state, zip, phone; 
	//cin or initialize variables 
	cout << firstName << " " << lastName << endl << address << endl << city << ", " << state << " " << zip << endl << phone << endl; 
	return 0; 
}