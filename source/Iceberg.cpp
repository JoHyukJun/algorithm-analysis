//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2012.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <string.h>

#define MAX 301

using namespace std;

int n, m;
int matrix[MAX][MAX] = { 0, };
int visited[MAX][MAX] = { 0, };
int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1 };
int result = 0;
int year = 0;


void dfs(int x, int y) {
	visited[x][y] = 1;

	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
			continue;
		}
		if (matrix[nx][ny] <= 0 || visited[nx][ny] == 1) {
			continue;
		}

		dfs(nx, ny);
	}

	return;
}


void melt_down() {
	int deep_copy[MAX][MAX];

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			deep_copy[i][j] = matrix[i][j];
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			int cnt = 0;

			if (deep_copy[i][j] > 0) {
				for (int k = 0; k < 4; k++) {
					int ni = i + dx[k];
					int nj = j + dy[k];

					if (deep_copy[ni][nj] == 0) {
						cnt += 1;
					}
				}

				matrix[i][j] -= cnt;

				if (matrix[i][j] < 0) {
					matrix[i][j] = 0;
				}
			}
		}
	}

	return;
}


int main() {
	// faster better
    cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> matrix[i][j];
		}
	}

	while (true) {
		memset(visited, 0, sizeof(visited));

		int div_cnt = 0;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (matrix[i][j] > 0 && visited[i][j] == 0) {
					div_cnt += 1;
					dfs(i, j);
				}
			}
		}

		if (div_cnt > 1) {
			result = year;
			break;
		}
		if (div_cnt == 0) {
			result = 0;
			break;
		}

		melt_down();
		year += 1;
	}

	cout << result;
	
	return 0;
}