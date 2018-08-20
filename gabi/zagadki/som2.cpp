#include <iostream>
#include <ctype.h>


using namespace std;

bool is_atu(char c) {
	c = toupper(c);
	return (c > '4' && c <= '9') || c == '0' || c == 'W' || c == 'D';
}

int main()
{
	string s;
	cin >> s;
	if (s.length() != 15) return 0;
	if (s.substr(0, 5) != "xAxxx") return 0;
	if (!is_atu(s[5])) return 0;
	if (s.substr(6, 3) != "xAx") return 0;
	if (!is_atu(s[9])) return 0;
	if (s.substr(10, 3) != "x8x") return 0;
	if (!is_atu(s[13])) return 0;
	if (!is_atu(s[14])) return 0;
	cout << "Hasło: nie_zgadlabys\n";
}
