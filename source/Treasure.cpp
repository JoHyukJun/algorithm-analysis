//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2012.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <string.h>
#include <algorithm>

#define MAX 50

using namespace std;


int n;
int arr[MAX];
int target[MAX];
int result = 0;


int main() {
	// faster better
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	for (int i = 0; i < n; i++) {
		cin >> target[i];
	}

	sort(arr, arr + n);
	sort(target, target + n, greater<int>());

	for (int i = 0; i < n; i++) {
		result = result + (arr[i] * target[i]);
	}

	cout << result << '\n';

	return 0;
}