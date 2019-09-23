//
//	main.cpp
//	TournamentRoundCalculation
//
//	Created by Jo Hyuk Jun on 2019/09/21.
//	Copyright © 2019 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int solution(int n, int a, int b);

int main()
{
	int res = 0;

	cout << solution(8, 4, 7);

	return 0;
}



int solution(int n, int a, int b)
{
	int answer = 0;

	vector<int> checker;
	int per = 1;


	for (int i = 0; i < n; i++) {
		checker.push_back(per);
		per++;
	}

	int round = 1;

	int tempSize = checker.size();

	bool flg = false;

	while (1) {
		vector<int> tmp(tempSize);

		for (int i = 0; i < checker.size(); i++) {
			if (i % 2 == 1) {
				if ((checker[i] == a || checker[i] == b) && (checker[i - 1] == a || checker[i - 1] == b)) {
					answer = round;
					flg = true;
				}


				if (checker[i] == a || checker[i] == b) {
					checker[i / 2] = checker[i];
				}
				else if (checker[i - 1] == a || checker[i - 1] == b) {
					checker[i / 2] = checker[i - 1];
				}
				else {
					checker[i / 2] = checker[i];
				}
			}
		}
		
		if (flg == 1) {
			break;
		}

		checker.resize(checker.size() / 2);
		round++;
	}


	return answer;
}