//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2012.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <queue>

#define MAX 101

using namespace std;


int n, m;
char mat[MAX][MAX];
int visited[MAX][MAX] = { 0, };
int res[MAX][MAX] = { 0, };

// Up Down Right Left
int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0, 0 };


void bfs(int in_x, int in_y) {
    visited[in_x][in_y] = 1;

    queue<pair<int, int>> q;
    q.push(make_pair(in_x, in_y));

    while (!q.empty()) {
        int x = q.front().second;
        int y = q.front().first;

        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= m || ny < 0 || ny >= n) {
                continue;
            }
            if (visited[ny][nx] == 1) {
                continue;
            }
            if (mat[ny][nx] != '1') {
                continue;
            }
            if (res[ny][nx] != 0) {
                continue;
            }

            visited[ny][nx] = 1;
            q.push(make_pair(ny, nx));

            res[ny][nx] = res[y][x] + 1;
        }
    }

    return;
}


int main()
{
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> mat[i];
    }

    bfs(0, 0);

    cout << res[n - 1][m - 1] + 1 << endl;

    return 0;
}