//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <string.h>
#include <algorithm>
#include <queue>

#define MAX 1001

using namespace std;

int m, n;
int matrix[MAX][MAX];
int visited[MAX][MAX];
int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1 };
queue<pair<int, int>> q;


int checker() {
	int output = 0;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (visited[i][j] == -1 && matrix[i][j] == 0) {
				output = -1;
				return output;
			}

			if (output < visited[i][j]) {
				output = visited[i][j];
			}
		}
	}

	return output;
}


void bfs() {
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
				continue;
			}
			if (visited[nx][ny] >= 0 || matrix[nx][ny] == 1 || matrix[nx][ny] == -1) {
				continue;
			}

			visited[nx][ny] = visited[x][y] + 1;
			q.push(make_pair(nx, ny));
		}
	}

	return;
}


int main() {
	// faster better
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> m >> n;

	bool ffward = true;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> matrix[i][j];
			visited[i][j] = -1;

			if (matrix[i][j] == 1) {
				q.push(make_pair(i, j));
				visited[i][j] = 0;
			}
			if (matrix[i][j] == 0) {
				ffward = false;
			}
		}
	}

	if (ffward) {
		cout << 0;
	}
	else {
		bfs();
		int day = checker();

		cout << day;
	}

	return 0;
}