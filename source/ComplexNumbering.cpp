//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2012.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <sstream>

#include <vector>
#include <algorithm>

using namespace std;

int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, -1, 0, 1 };
int cnt = 1;
int mat[100][100] = { 0, };
int visited[100][100] = { 0, };
int msize;
char matrix[100][100];




void dfs(int x, int y) {
	visited[x][y] = 1;
	mat[x][y] = 0;

	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (nx < 0 || ny < 0 || nx >= msize || ny >= msize) {
			continue;
		}
		if (visited[nx][ny]) {
			continue;
		}
		if (mat[nx][ny] == 0) {
			visited[nx][ny] = 1;
			continue;
		}

		dfs(nx, ny);
		cnt += 1;
	}

	return;
}


int main() {
	int sizeOfMatrix;
	cin >> sizeOfMatrix;


	vector<int> res;
	msize = sizeOfMatrix;

	for (int i = 0; i < sizeOfMatrix; i++) {
		cin >> matrix[i];
		for (int j = 0; j < sizeOfMatrix; j++) {
			mat[i][j] = matrix[i][j] - '0';
		}
	}

	for (int i = 0; i < sizeOfMatrix; i++) {
		for (int j = 0; j < sizeOfMatrix; j++) {
			if (mat[i][j] == 1) {
				dfs(i, j);
				res.push_back(cnt);
				cnt = 1;
			}
			else {
				continue;
			}
		}
	}

	cout << res.size() << endl;
	sort(res.begin(), res.end());

	for (int i = 0; i < res.size(); i++) {
		cout << res[i] << ' ';
	}

	return 0;
}