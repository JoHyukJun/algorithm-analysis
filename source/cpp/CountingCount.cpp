//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <queue>

#define MAX 101

using namespace std;

int n, x, y, m;
int mat[MAX][MAX] = { 0, };
int visited[MAX] = { 0, };
int relation[MAX] = { 0, };


void bfs(int start_point) {
	queue<int> q;

	q.push(start_point);
	visited[start_point] = 1;

	while (!q.empty()) {
		int cur = q.front();
		q.pop();

		for (int i = 1; i <= n; i++) {
			if (mat[cur][i] == 1 && visited[i] == 0) {
				visited[i] = 1;
				relation[i] = relation[cur] + 1;
				q.push(i);
			}
		}
	}

	return;
}


int main() {
	cin >> n;
	cin >> x >> y;
	cin >> m;

	for (int i = 0; i < m; i++) {
		int head, tail;

		cin >> head >> tail;

		mat[head][tail] = 1;
		mat[tail][head] = 1;
	}

	bfs(x);

	if (relation[y] != 0) {
		cout << relation[y];
	}
	else {
		cout << -1;
	}

	return 0;
}