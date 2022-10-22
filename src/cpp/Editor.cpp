//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <string.h>
#include <algorithm>
#include <list>

#define MAX 0

using namespace std;

string n;
int m;
list<char> editor;


int main() {
	// faster better
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	cin >> m;

	for (int i = 0; i < n.size(); i++) {
		editor.push_back(n[i]);
	}

	auto cursor = editor.end();

	for (int i = 0; i < m; i++) {
		char command;
		cin >> command;

		if (command == 'L') {
			if (cursor != editor.begin()) {
				cursor--;
			}
		}
		else if (command == 'D') {
			if (cursor != editor.end()) {
				cursor++;
			}
		}
		else if (command == 'B') {
			if (cursor != editor.begin()) {
				cursor--;
				cursor = editor.erase(cursor);
			}
		}
		else if (command == 'P') {
			char adder;
			cin >> adder;
			editor.insert(cursor, adder);
		}
	}

	for (auto i = editor.begin(); i != editor.end(); i++) {
		cout << *i;
	}

	return 0;
}