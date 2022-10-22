//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <string.h>
#include <algorithm>

#define MAX 1000001

using namespace std;


int n;
int arr[MAX] = { 0, };


int main() {
	// faster better
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;

	int x = n;

	arr[1] = 0;

	for (int i = 2; i < n + 1; i++) {
		arr[i] = arr[i - 1] + 1;
		
		if (i % 3 == 0) {
			arr[i] = min(arr[i], arr[i / 3] + 1);
		}

		if (i % 2 == 0) {
			arr[i] = min(arr[i], arr[i / 2] + 1);
		}
	}

	cout << arr[n] << '\n';

	return 0;
}