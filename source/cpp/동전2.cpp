//
//    main.cpp
//
//    Created by JO HYUK JUN on 2022.
//    Copyright © 2022 JO HYUK JUN. All rights reserved.
//


#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

#define MAX 100001


int n, k;
int dp[MAX];
int coin[101];


int main() {
    // faster better
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int answer = -1;
    
    cin >> n >> k;
    
    for (int i = 0; i < n; i++) {
        cin >> coin[i];
    }
    
    dp[0] = 0;
    
    for (int i = 1; i <= k; i++) {
        dp[i] = 10001;
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 1; j <= k; j++) {
            if (j >= coin[i]) {
                dp[j] = min(dp[j], dp[j - coin[i]] + 1);
            }
        }
    }
    
    if (dp[k] == 10001) {
        cout << answer;
    }
    else {
        answer = dp[k];
        
        cout << answer;
    }
    
    return 0;
}
