//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <string.h>
#include <algorithm>

#define MAX 301

using namespace std;


int n;
int arr[MAX] = { 0, };
int dp[MAX] = { 0, };


int main() {
	// faster better
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	dp[0] = arr[0];
	dp[1] = arr[0] + arr[1];
	// finding max value of (second step + last step) and (first step + last step)
	dp[2] = max(arr[1] + arr[2], arr[0] + arr[2]);

	for (int i = 3; i < n + 1; i++) {
		dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i]);
	}

	cout << dp[n - 1] << '\n';

	return 0;
}