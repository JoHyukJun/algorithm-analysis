// test-sol.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <string>
#include <vector>

using namespace std;


string in_str1, in_str2, res;
int carry = 0;

int main()
{
    cin >> in_str1 >> in_str2;

    reverse(in_str1.begin(), in_str1.end());
    reverse(in_str2.begin(), in_str2.end());

    int holder = max(in_str1.size(), in_str2.size());

    while (in_str1.size() < holder) {
        in_str1 += '0';
    }
    while (in_str2.size() < holder) {
        in_str2 += '0';
    }

    for (int i = 0; i < holder; i++) {
        int tmp = (in_str1[i] - '0') + (in_str2[i] - '0') + carry;

        if (tmp >= 10) {
            tmp %= 10;
            carry = 1;
        }
        else {
            carry = 0;
        }

        res += to_string(tmp);
    }

    if (carry) {
        res += '1';
    }

    reverse(res.begin(), res.end());

    cout << res << endl;


    return 0;
}