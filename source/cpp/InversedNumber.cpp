//
//	main.cpp
//	InversedNumber
//
//	Created by Jo Hyuk Jun on 2019/09/21.
//	Copyright © 2019 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <string>
#include <vector>

using namespace std;


vector<int> solution(long long n);

int main()
{
	int a = 12345;

	vector<int> res;

	res = solution(a);

	for (int i = 0; i < res.size(); i++) {
		cout << res.at(i) << ' ';
	}

	return 0;
}



vector<int> solution(long long n) {
	vector<int> answer;

	string str;

	str = to_string(n);
	
	for (int i = 0; i < str.size(); i++) {
		answer.push_back(str[str.size() - i - 1] - '0');
	}


	return answer;
}