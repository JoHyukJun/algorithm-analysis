//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>

#define MAX 101

using namespace std;


int n, m;
int mat[MAX][MAX];
int visited[MAX] = { 0, };
int result = 0;


void dfs(int in_val) {
    visited[in_val] = 1;

    for (int i = 1; i <= n; i++) {
        if (mat[in_val][i] == 1 && visited[i] == 0) {
            result += 1;
            dfs(i);
        }
    }

    return;
}


int main()
{
    cin >> n;
    cin >> m;

    for (int i = 0; i < m; i++) {
        int s, e;

        cin >> s >> e;

        mat[s][e] = 1;
        mat[e][s] = 1;
    }

    dfs(1);

    cout << result;

    return 0;
}