#include<iostream>
#include"binary/include/binary.h"
using namespace std;

int main()
{
	cout << myLib::count_binary(1) << endl;
	cout << myLib::count_binary(9) << endl;
	cout << myLib::toHex(26) << endl;
	cout << myLib::toHex(-1) << endl;
	for(auto a:myLib::int2VString(15))
		cout << a << endl;
}


