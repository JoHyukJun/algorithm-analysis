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


int a, b;


int main() {
    // faster better
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int answer = 0;

    cin >> a >> b;

    string str_a = to_string(a);
    string str_b = to_string(b);

    reverse(str_a.begin(), str_a.end());
    reverse(str_b.begin(), str_b.end());

    int rev_a = stoi(str_a);
    int rev_b = stoi(str_b);

    if (rev_a > rev_b) {
        answer = rev_a;
    }
    else {
        answer = rev_b;
    }
    
    cout << answer << endl;

    return 0;
}