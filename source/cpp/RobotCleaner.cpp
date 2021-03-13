//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <string.h>
#include <vector>

#define MAX 51

using namespace std;

int n, m;
int matrix[MAX][MAX] = { 0 , };
int visited[MAX][MAX] = { 0, };
int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, 1, 0, -1 };
int ddx[4] = { 1, 0, -1, 0 };
int ddy[4] = { 0, -1, 0, 1 };
int moving = 0;


struct Robot
{
	int x;
	int y;
	int d;
};

Robot robot;


int direction(int in_d) {
	int output = 0;

	switch (in_d)
	{
	case 0:
		output = 3;
		break;
	case 1:
		output = 0;
		break;
	case 2:
		output = 1;
		break;
	case 3:
		output = 2;
		break;
	default:
		break;
	}

	return output;
}


void dfs(int in_x, int in_y, int in_d) {
	bool back_moving = true;

	if (matrix[in_x][in_y] == 1) {
		return;
	}

	if (matrix[in_x][in_y] == 0) {
		moving += 1;
		matrix[in_x][in_y] = -1;
	}

	for (int i = 0; i < 4; i++) {
		int nd = direction(in_d);
		int nx = in_x + dx[nd];
		int ny = in_y + dy[nd];


		if (matrix[nx][ny] == 0) {
			dfs(nx, ny, nd);

			return;
		}
		else {
			in_d = nd;
		}
	}

	int bx = in_x + ddx[in_d];
	int by = in_y + ddy[in_d];

	dfs(bx, by, in_d);

	return;
}


int main() {
	// faster better
    cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> n >> m;
	cin >> robot.x >> robot.y >> robot.d;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> matrix[i][j];
		}
	}

	dfs(robot.x, robot.y, robot.d);
	
	cout << moving;

	return 0;
}