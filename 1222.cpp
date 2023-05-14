#include<bits/stdc++.h>
#include<cmath>
using namespace std;
int main() {
    unsigned int n, l, c, lines, characters;
    string word;

    while (cin >> n >> l >> c) {
        lines = 1;
        characters = 0;
        int an=1;
        while (n--) {
            cin >> word;
            if (characters + (characters != 0) + word.length() <=c) {
                characters += word.length() +  (characters != 0);

            } else {
                characters = word.length();
                lines++;
                if(lines > l){
                    an++;
                    lines=1;
                }
            }
        }

            cout << an <<endl;
    }
    return 0;
}