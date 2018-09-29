#include <iostream>
#include <string>
using namespace std;

int **map;
int **gone;
int row, col;
bool success = false;

void goWith(int i, int j) {
	if (i == row-1) success = true;
	if (map[i][j]==0 && gone[i][j] == 0)
	{
		gone[i][j] = 1;
		//cout << "(" << i <<"," << j << ")" << endl;
		if(i-1>0) goWith(i-1, j);
		if(i+1<col) goWith(i+1, j);
		if(j-1>0) goWith(i, j-1);
		if(j+1<row) goWith(i, j+1);
	}
}

void answer() {

	for (int j = 0; j < col; j++) {
		if (map[0][j]==0)
		{
			goWith(0, j);
		}
	}

}


void main(void) {
	string s;
	cin >> row >> col;

	map = new int*[row];
	gone = new int*[row];
	for (int i = 0; i < row; i++) {
		map[i] = new int[col];
		gone[i] = new int[col];
	}

	for (int i = 0; i < row; i++) {
		cin >> s;
		for (int j = 0; j < col; j++) {
			map[i][j] = int(s[j]-'0');
			gone[i][j] = 0;
		}
		cout << endl;
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
	if (success == true) cout << "YES";
	else cout << "NO";

	for (int i = 0; i < row; i++) {
		delete[] map[i];
	}
	delete[] map;

}
