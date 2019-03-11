#include <iostream>
#include <vector>

using namespace std;

vector<int> tree[10000];
int par[10000];
int n;


void read()
{
	cin >> n;
	for (int i = 1; i < n; ++i) {
		int a,b;
		cin >> a >> b;
		tree[a].push_back(b);
		tree[b].push_back(a);
	}
	tree[1].push_back(0);
}

bool is_lisc(int k) {
	return tree[k].size() == 1;
}

int res[10000];

void dfs(int k, bool is_min) {
	if (is_lisc(k)) return;
	if (is_min) {
		for (int i=0; i < tree[k].size(); ++i) {
			if (tree[k][i] == par[k]) continue;
			par[tree[k][i]] = k;
			dfs(tree[k][i], !is_min);
			res[k] += res[tree[k][i]] + is_lisc(tree[k][i]);
		}
	} else {
		int m = 10000;
		for (int i=0; i < tree[k].size(); ++i) {
			if (tree[k][i] == par[k]) continue;
			par[tree[k][i]] = k;
			dfs(tree[k][i], !is_min);
			m = min(m, res[tree[k][i]]);
		}
		res[k] = max(m, 1);
	}
}


int main(int argc, char *argv[])
{
	read();
	dfs(1, false);
	cout << res[1];
	return 0;
}
