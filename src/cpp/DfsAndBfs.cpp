//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <queue>

#define MAX 1001

using namespace std;


int n, m, v;
int mat[MAX][MAX] = { 0, };
int dvisited[MAX] = { 0, };
int bvisited[MAX] = { 0, };
queue<int> q;


void dfs(int start_point) {
    cout << start_point << ' ';

    dvisited[start_point] = 1;

    for (int i = 1; i <= n; i++) {
        if (mat[start_point][i] == 1 && dvisited[i] == 0) {
            dfs(i);
        }
    }

    return;
}


void bfs(int start_point) {
    bvisited[start_point] = 1;

    q.push(start_point);

    while (!q.empty()) {
        start_point = q.front();
        q.pop();

        cout << start_point << ' ';

        for (int i = 1; i <= n; i++) {
            if (mat[start_point][i] == 1 && bvisited[i] == 0) {
                q.push(i);
                bvisited[i] = 1;
            }
        }
    }

    return;
}


int main()
{
    cin >> n >> m >> v;

    for (int i = 0; i < m; i++) {
        int s, e;

        cin >> s >> e;

        mat[s][e] = 1;
        mat[e][s] = 1;
    }

    dfs(v);
    cout << endl;

    
    bfs(v);
    cout << endl;

    return 0;
}