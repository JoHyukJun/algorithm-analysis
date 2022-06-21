//
//    main.cpp
//
//    Created by JO HYUK JUN on 2022.
//    Copyright © 2022 JO HYUK JUN. All rights reserved.
//


#include <iostream>
#include <string.h>

using namespace std;

#define MAX 100001


int t, n;
long long dp[MAX];


int main() {
    // faster better
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    long long answer = 0;
    
    cin >> t;
    
    while (t--) {
        cin >> n;
        
        if (n >= 3) {
            dp[0] = 1;
            dp[1] = 1;
            dp[2] = 1;
            
            for (int i = 3; i <= n; i++) {
                dp[i] = dp[i - 2] +dp[i - 3];
            }
            answer = dp[n - 1];
        }
        else {
            answer = 1;
        }
        
        cout << answer << endl;
    }
    
    return 0;
}
