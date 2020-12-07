//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <string.h>
#include <vector>

#define MAX 2000000

using namespace std;


vector<int> prime_number;
int eratos[MAX + 1] = { 0, };


void eratosthenes() {
	eratos[0] = 1;
	eratos[1] = 1;

	for (int i = 2; i < MAX + 1; i++) {
		if (eratos[i] == 0) {
			prime_number.push_back(i);

			for (int j = i * 2; j < MAX + 1; j += i) {
				eratos[j] = 1;
			}
		}
	}
}


bool is_prime(long long idx) {
	if (idx <= MAX) {
		if (eratos[idx] == 0) {
			return true;
		}
		else {
			return false;
		}
	}
	else {
		for (int i = 0; i < prime_number.size(); i++) {
			if (idx % prime_number[i] == 0) {
				return false;
			}
		}

		return true;
	}

}


int main() {
	// faster better
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);

	int t;
	cin >> t;

	eratosthenes();

	for (int i = 0; i < t; i++) {
		long long a, b;
		cin >> a >> b;

		long long sum;
		sum = a + b;

		if (sum < 4) {
			cout << "NO" << endl;
			continue;
		}


		if (sum % 2 == 0) {
			cout << "YES" << endl;
		}
		else {
			if (is_prime(sum - 2)) {
				cout << "YES" << endl;
			}
			else {
				cout << "NO" << endl;
			}
		}
	}

	return 0;
}