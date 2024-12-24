#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;

    vector<int> needs(n, 0);
    vector<int> backs(n + 1, 0);

    vector<vector<int>> can(n, vector<int>(n + 1, 0));

    for (int _ = 0; _ < q; _++) {
        int s;
        char m;
        cin >> s >> m;
        s -= 1;

        if (m == '+') {
            needs[s] += 1;
        } else {
            backs[s] += 1;
        }

        for (int i = 0; i <= n; i++) {
            if (i != s) {
                can[s][i] = max(needs[s] - backs[i], can[s][i]);
            }
        }
    }

    auto min_dis = [&]() -> int {
        vector<vector<int>> dp(1 << n, vector<int>(n, 0));

        for (int i = 0; i < n; i++) {
            dp[0][i] = can[i][n];
        }

        for (int passing_bits = 1; passing_bits < (1 << n) - 1; passing_bits++) {
            for (int i = 0; i < n; i++) {
                if (passing_bits & (1 << i)) {
                    continue;
                }
                int ans = INT_MAX;
                for (int j = 0; j < n; j++) {
                    if (!(passing_bits & (1 << j))) {
                        continue;
                    }
                    int new_bits = passing_bits & ~(1 << j);
                    ans = min(ans, dp[new_bits][j] + can[i][j]);
                }
                dp[passing_bits][i] = ans;
            }
        }

        int bits = (1 << n) - 1;
        int ans = INT_MAX;

        for (int i = 0; i < n; i++) {
            int newbits = bits & ~(1 << i);
            ans = min(ans, dp[newbits][i]);
        }

        return ans;
    };

    cout << min_dis() + n << "\n";

    return 0;
}
