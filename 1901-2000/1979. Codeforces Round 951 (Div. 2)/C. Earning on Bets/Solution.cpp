#include <bits/stdc++.h>

using namespace std;

int gcd(int a, int b){
    a, b = max(a,b), min(a,b);
    while (b) {
        a, b = b, a % b;
    }

    return a;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {
        int n;
        vector<int> k;
        cin >> n;
        long long all = 1;
        int temp;

        for (int i = 0; i < n; i++) {
            cin >> temp;
            k.push_back(temp);
            all = all * k[i] / gcd(all, k[i]);
        }

        int sum = 0;
        for (int i = 0; i < n; i++) {
            k[i] = all / k[i];
            sum += k[i];
        }
        
        if (sum < all){
            for (int i = 0; i < n; i++) {
                cout << k[i] << " ";
            }
        } else {
            cout << -1;
        }
        cout << '\n';
    }
}