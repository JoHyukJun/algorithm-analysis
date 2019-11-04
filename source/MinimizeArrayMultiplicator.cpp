//
//	main.cpp
//	MinimizeArrayMultiplicator
//
//	Created by Jo Hyuk Jun on 2019/10/07.
//	Copyright © 2019 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int solution(vector<int> A, vector<int> B);

int main()
{
	int res;

	vector<int> test = {1, 4, 2};
	vector<int> test1 = { 5, 4, 4 };

	res = solution(test, test1);

	cout << res << endl;



	return 0;
}

int solution(vector<int> A, vector<int> B) {
	int answer = 0;

	sort(A.begin(), A.end());
	sort(B.begin(), B.end(), greater<int>());


	for (int i = 0; i < A.size(); i++) {
		answer += A[i] * B[i];
	}


	return answer;
}