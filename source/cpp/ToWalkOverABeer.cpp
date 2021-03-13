//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <string.h>
#include <vector>

#define MAX 102

using namespace std;

int t, n;
int matrix[MAX][MAX] = { 0, };
int visited[MAX] = { 0, };
vector<int> line[MAX];


void dfs(int start_point) {
	visited[start_point] = 1;

	for (int i = 0; i < line[start_point].size(); i++) {
		int next_point = line[start_point][i];

		if (visited[next_point] == 1) {
			continue;
		}

		dfs(next_point);
	}

	return;
}


int calculator(int x1, int x2, int y1, int y2) {
	int output = 0;
	output = abs(max(x1, x2) - min(x1, x2)) + abs(max(y1, y2) - min(y1, y2));

	return output;
}


int main() {
	// faster better
    cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> n;

		memset(matrix, 0, sizeof(matrix));
		memset(visited, 0, sizeof(visited));

		for (int j = 0; j < n + 2; j++) {
			cin >> matrix[j][0] >> matrix[j][1];
			line[j].clear();
		}

		for (int j = 0; j < n + 2; j++) {
			for (int k = j + 1; k < n + 2; k++) {
				int temp = 0;
				temp = calculator(matrix[j][0], matrix[k][0], matrix[j][1], matrix[k][1]);

				if (temp <= 1000) {
					line[j].push_back(k);
					line[k].push_back(j);
				}
			}
		}

		dfs(0);

		if (visited[n + 1] == 1) {
			cout << "happy" << endl;;
		}
		else {
			cout << "sad" << endl;
		}
	}

	return 0;
}