//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <queue>

#define MAX 102

using namespace std;

int m, n, h;
int mat[MAX][MAX][MAX];
int visited[MAX][MAX][MAX];
int dx[6] = { 0, 0, 1, -1, 0, 0 };
int dy[6] = { -1, 1, 0, 0, 0, 0 };
int dz[6] = { 0, 0, 0, 0, -1, 1 };
queue<pair<pair<int, int>, int>> q;
bool ffward;


void bfs() {
	while (!q.empty()) {
		int q_size = q.size();

		int x = q.front().first.second;
		int y = q.front().second;
		int z = q.front().first.first;

		q.pop();

		for (int i = 0; i < 6; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			int nz = z + dz[i];


			if (nx < 0 || ny < 0 || nz < 0 || nx >= n || ny >= m || nz >= h) {
				continue;
			}
			if (visited[nz][nx][ny] >= 0) {
				continue;
			}

			visited[nz][nx][ny] = visited[z][x][y] + 1;
			q.push(make_pair(make_pair(nz, nx), ny ));
		}
	}

	return;
}


int main() {
	// faster better
    cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> m >> n >> h;

	ffward = true;

	for (int i = 0; i < h; i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < m; k++) {
				cin >> mat[i][j][k];

				if (mat[i][j][k] == 1) {
					q.push(make_pair(make_pair(i, j), k));
				}
				if (mat[i][j][k] == 0) {
					visited[i][j][k] = -1;
					ffward = false;
				}
			}
		}
	}

	if (ffward) {
		cout << 0;
	}
	else {
		bfs();
		int res = checker();
		cout << res;
	}

	return 0;
}