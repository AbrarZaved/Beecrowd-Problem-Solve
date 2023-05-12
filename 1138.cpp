#include <iostream>
#include <cstring>

using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    if(a==0 && b==0)
    return 0;

    int freq[10];
    memset(freq, 0, sizeof(freq));

    for (int i = a; i <= b; i++) {
        int n = i;
        while (n > 0) {
            freq[n % 10]++;
            n /= 10;
        }
    }

    for (int i = 0; i < 10; i++) {
        cout << freq[i] << " ";
    }
    cout << endl;

    return 0;
}
