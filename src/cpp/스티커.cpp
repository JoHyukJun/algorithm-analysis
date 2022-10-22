//
//    main.cpp
//
//    Created by JO HYUK JUN on 2022.
//    Copyright © 2022 JO HYUK JUN. All rights reserved.
//


#include <iostream>
#include <string.h>
#include <algorithm>
#include <string>

using namespace std;

#define MAX 100001

int t, n;
int mat[2][MAX];


int main() {
    // faster better
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int answer = 0;
    
    cin >> t;
    
    while (t--) {
        cin >> n;
        
        for (int i = 0; i < 2; i++) {
            for (int j = 2; j <= n + 1; j++) {
                cin >> mat[i][j];
            }
        }
        
        for (int i = 2; i <= n + 1; i++) {
            mat[0][i] += max(mat[1][i - 1], mat[1][i - 2]);
            mat[1][i] += max(mat[0][i - 1], mat[0][i - 2]);
        }
        
        answer = max(mat[0][n + 1], mat[1][n + 1]);
        
        cout << answer << endl;
    }
    
    return 0;
}