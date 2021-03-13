//
//	main.cpp
//	SortedNumber
//
//	Created by Jo Hyuk Jun on 2019/09/21.
//	Copyright © 2019 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


long long solution(long long n);

int main()
{
	int a = 118372;
	long long res;


	res = solution(a);

	cout << res;

	return 0;
}



long long solution(long long n) {
	long long answer = 0;

	string str;
	vector<int> sorter;
	long long decimal = 1;

	str = to_string(n);
	
	for (int i = 0; i < str.size(); i++) {
		sorter.push_back(str[i] - '0');
	}

	sort(sorter.begin(), sorter.end(), greater<int>());

	for (int i = 0; i < sorter.size(); i++) {
		answer += sorter[sorter.size() - 1 - i] * decimal;
		decimal *= 10;
	}

	return answer;
}