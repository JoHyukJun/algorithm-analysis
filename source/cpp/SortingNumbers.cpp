//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <string.h>
#include <algorithm>

#define MAX 10001

using namespace std;


int n;
int arr[MAX];


int main() {
	// faster better
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;

	for (int i = 0; i < n; i++) {
		int idx;
		cin >> idx;
		arr[idx] += 1;
	}

	for (int i = 0; i < MAX; i++) {
		for (int j = 0; j < arr[i]; j++) {
			cout << i << '\n';
		}
	}

	return 0;
}