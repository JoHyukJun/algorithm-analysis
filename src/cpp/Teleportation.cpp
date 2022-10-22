//
//	main.cpp
//	Teleportation
//
//	Created by Jo Hyuk Jun on 2019/09/21.
//	Copyright © 2019 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int solution(int n);

int main()
{
	int res = 0;

	res = solution(5000);

	cout << res;

	return 0;
}



int solution(int n)
{
	int ans = 0;
	int ckr = 0;

	while (1) {


		if (n % 2 == 1) {
			ckr += 1;
		}
		
		if (n == 1) {
			break;
		}

		n /= 2;
	}

	ans = ckr;

	return ans;
}