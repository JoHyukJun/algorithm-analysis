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

int n, m;
int arr[MAX];


int j_binary_serach(int in_term) {
	int output = 0;

	int head = 0;
	int tail = n - 1;

	if (head > tail) {
		return output;
	}

	while (head <= tail) {
		int mid = (head + tail) / 2;

		if (arr[mid] == in_term) {
			output = 1;

			return output;
		}
		else if (arr[mid] > in_term) {
			tail = mid - 1;
		}
		else if (arr[mid] < in_term) {
			head = mid + 1;
		}
	}

	return output;
}


int main() {
	// faster better
    cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	sort(arr, arr + n);

	cin >> m;

	for (int i = 0; i < m; i++) {
		int term;
		cin >> term;

		cout << j_binary_serach(term) << '\n';
	}

	return 0;
}