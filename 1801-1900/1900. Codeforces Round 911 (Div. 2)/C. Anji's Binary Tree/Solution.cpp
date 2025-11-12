#include <bits/stdc++.h>
using namespace std;

vector<pair<int,int>> childs;
string s;

int closest(int root) {
    if (root == 0)
        return INT_MAX-1;
    auto [l, r] = childs[root - 1];
    if (l == 0 && r == 0)
        return 0;
    int ans = INT_MAX;
    ans = min(ans, closest(l) + (s[root - 1] != 'L'));
    ans = min(ans, closest(r) + (s[root - 1] != 'R'));
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        cin >> s;
        childs.assign(n, {0, 0});
        vector<int> parents(n + 1, 0);

        for (int i = 0; i < n; ++i) {
            int a, b;
            cin >> a >> b;
            childs[i] = {a, b};
            if (a) parents[a] = i + 1;
            if (b) parents[b] = i + 1;
        }

        cout << closest(1) << '\n';
    }

    return 0;
}
