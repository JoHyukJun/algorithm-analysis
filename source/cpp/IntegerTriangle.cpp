//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <string.h>
#include <algorithm>

#define MAX 501

using namespace std;


int n;
int dp[MAX][MAX] = { 0, };


int main() {
	// faster better
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i + 1; j++) {
			cin >> dp[i][j];
		}
	}

	for (int i = 1; i < n; i++) {
		for (int j = 0; j < i + 1; j++) {
			if (j == 0) {
				dp[i][j] += dp[i - 1][j];
			}
			else if (j == i) {
				dp[i][j] += dp[i - 1][j - 1];
			}
			else {
				dp[i][j] += max(dp[i - 1][j], dp[i - 1][j - 1]);
			}
		}
	}

	int result = 0;

	for (int i = 0; i < n; i++) {
		if (result < dp[n - 1][i]) {
			result = dp[n - 1][i];
		}
	}

	cout << result << '\n';

	return 0;
}