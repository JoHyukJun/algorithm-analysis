//
//	main.cpp
//	MakeRectanglePoint
//
//	Created by Jo Hyuk Jun on 2019/09/21.
//	Copyright © 2019 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <vector>

using namespace std;


vector<int> solution(vector<vector<int>> v);


int main()
{
	vector<vector<int>> v1;
	v1 = { { 1, 1 }, { 2, 2 }, { 1, 2 } };

	vector<int> res;

	res = solution(v1);

	cout << res[0] << ", " << res[1];


	return 0;
}



vector<int> solution(vector<vector<int>> v) {
	vector<int> ans;

	int d1 = 0, d2 = 0;
	int coreidx = 0;


	for (int i = 0; i < v.size(); i++) {
		bool flg1 = false;
		bool flg2 = false;

		for (int j = 0; j < v.size(); j++) {
			if (i != j) {
				if (v[i][0] == v[j][0]) {
					flg1 = true;
					d1= v[j][1];
				}
				else if (v[i][1] == v[j][1]) {
					flg2 = true;
					d2 = v[j][0];
				}
			}


			if (flg1 && flg2) {
				coreidx = i;
				ans = { d2, d1 };
			}
		}
	}

	return ans;
}
