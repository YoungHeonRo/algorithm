#include <iostream>
#include <string>
#include <ios>
using namespace std;

int **map;
int **gone;
int row, col;
bool success = false;

void goWith(int i, int j) {
	if (i == row - 1) success = true;
	if (map[i][j] == 0 && gone[i][j] == 0)
	{
		gone[i][j] = 1;
		//cout << "(" << i <<"," << j << ")" << endl;
		if (i - 1>0) goWith(i - 1, j);
		if (i + 1<row) goWith(i + 1, j);
		if (j - 1>0) goWith(i, j - 1);
		if (j + 1<col) goWith(i, j + 1);
	}
}

void answer() {

	for (int j = 0; j < col; j++) {
		if (map[0][j] == 0)
		{
			goWith(0, j);
		}
	}

}


int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	string s;
	cin >> row >> col;
	cin.ignore();

	map = new int*[row];
	gone = new int*[row];
	for (int i = 0; i < row; i++) {
		map[i] = new int[col];
		gone[i] = new int[col];
	}

	for (int i = 0; i < row; i++) {
		getline(cin, s);
		for (int j = 0; j < col; j++) {
			map[i][j] = int(s[j] - '0');
			gone[i][j] = 0;
		}
	}
	/*
	cout << "MAP :" << endl;
	for (int i = 0; i < row; i++) {
	for (int j = 0; j < col; j++) {
	cout << map[i][j];
	}
	cout << endl;
	}
	*/
	answer();
	if (success == true) cout << "YES" <<endl;
	else cout << "NO" <<endl;

	for (int i = 0; i < row; i++) {
		delete[] map[i];
	}
	delete[] map;
	return 0;
}
