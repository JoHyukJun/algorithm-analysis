//
//    main.cpp
//
//    Created by JO HYUK JUN on 2022.
//    Copyright © 2022 JO HYUK JUN. All rights reserved.
//


#include <iostream>
#include <string.h>
#include <queue>
#include <vector>

using namespace std;

#define MAX 1500

int r, c;
bool ckr;
char mat[MAX][MAX];
bool visited[MAX][MAX];

// Up Down Right Left
int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0, 0 };

queue<pair<int, int>> swanQueue, swanNQeueu, lakeQueue, lakeNQeueu;
pair<int, int> swanPtr;


void SwanBfs() {
    while (swanQueue.empty() == 0 && ckr == false) {
        int x = swanQueue.front().first;
        int y = swanQueue.front().second;
        swanQueue.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < r && ny >= 0 && ny < c) {
                if (visited[nx][ny] == false) {
                    if (mat[nx][ny] == '.') {
                        visited[nx][ny] = true;
                        swanQueue.push(make_pair(nx, ny));
                    }
                    else if (mat[nx][ny] == 'L') {
                        visited[nx][ny] = true;
                        ckr = true;
                        break;
                    }
                    else if (mat[nx][ny] == 'X') {
                        visited[nx][ny] = true;
                        swanNQeueu.push(make_pair(nx, ny));
                    }
                }
            }
        }
    }
}


void LakeBfs() {
    while (lakeQueue.empty() == 0) {
        int x = lakeQueue.front().first;
        int y = lakeQueue.front().second;
        lakeQueue.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < r && ny >= 0 && ny < c) {
                if (mat[nx][ny] == 'X') {
                    mat[nx][ny] = '.';
                    lakeNQeueu.push(make_pair(nx, ny));
                }
            }
        }
    }
}


int main() {
    // faster better
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> r >> c;

    ckr = false;
    int res = 0;

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> mat[i][j];

            if (mat[i][j] != 'X') {
                lakeQueue.push(make_pair(i, j));
            }

            if (mat[i][j] == 'L') {
                swanPtr.first = i;
                swanPtr.second = j;
            }
        }
    }

    swanQueue.push(make_pair(swanPtr.first, swanPtr.second));
    visited[swanPtr.first][swanPtr.second] = true;

    while (ckr == false) {
        SwanBfs();

        if (ckr == false) {
            LakeBfs();
            lakeQueue = lakeNQeueu;
            swanQueue = swanNQeueu;

            while (lakeNQeueu.empty() == 0) lakeNQeueu.pop();
            while (swanNQeueu.empty() == 0) swanNQeueu.pop();

            res ++;
        }
    }

    cout << res << endl;

    return 0;
}