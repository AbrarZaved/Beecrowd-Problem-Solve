#include<bits/stdc++.h>
#include<cmath>
using namespace std;
int main() {
    unsigned int n, l, c, lines, ch;
    string word;

    while (cin >> n >> l >> c) {
        lines = 1;
        ch = 0;
        int page=1;
        while (n--) {
            cin >> word;
            if (ch + (ch != 0) + word.length() <=c) {
                ch += word.length() +  (ch != 0);

            } else {
                ch = word.length();
                lines++;
                if(lines > l){
                    page++;
                    lines=1;
                }
            }
        }

            cout << page <<endl;
    }
    return 0;
}