#include <iostream>
#include <string>

using namespace std; 

/*

struct ContactInfo{
	string firstName, lastName, address, city, state, zip, phone; 
}; 

or 

class ContactInfo{
	string firstName, lastName, address, city, state, zip, phone; 
	
	ContactInfo(string f, string l, string addr, string name, string abbreviation, string code, string number)
		:firstName(f), lastName(l), address(addr), city(name), state(abbreviation), zip(code), phone(number)
	{
	}
}
now can create multiple ContactInfo :)  
*/

int main(){
	
	string firstName, lastName, address, city, state, zip, phone; 
	//cin or initialize variables 
	cout << firstName << " " << lastName << endl << address << endl << city << ", " << state << " " << zip << endl << phone << endl; 
	return 0; 
}