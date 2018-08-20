#include<vector>
#include<stack>
#include<cstdio>

using namespace std;

struct Vertex {
	vector<int> adj;
	bool visited;
};

vector<Vertex> vertexes;

void dfs(int seed) {
	stack<int> s;
	int next;
	s.push(seed);
	while (!s.empty()) {
		next = s.top();
		s.pop();
		printf("%d\n", next);
		Vertex v = vertexes[next];
		vertexes[next].visited = true;
		for (vector<int>::iterator it=v.adj.begin(); it != v.adj.end(); ++it) {
			if (!vertexes[*it].visited) {
				s.push(*it);
			}
		}
	}
}

void read() {
	int n, m, vnum;
	Vertex v;
	v.visited = false;
	scanf("%d", &n);
	for (int i=0; i<n; ++i) {
		scanf("%d", &m);
		for (int j=0; j<m; ++j) {
			scanf("%d", &vnum);
			v.adj.push_back(vnum);
		}
		vertexes.push_back(v);
	}
}

int main() {
	read();
	// printf("AAAA");
	dfs(0);
}
