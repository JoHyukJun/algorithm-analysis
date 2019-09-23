//
//	main.cpp
//	BasicStarsPrinter
//
//	Created by Jo Hyuk Jun on 2019/09/21.
//	Copyright © 2019 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>

using namespace std;


int main()
{
	int a, b;
	cin >> a >> b;


	for (int i = 0; i < b; i++) {
		for (int j = 0; j < a; j++) {
			cout << "*";
		}

		cout << endl;
	}
}