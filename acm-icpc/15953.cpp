#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int n;
	int firstPrize[22] = { 0 };
	int secondPrize[32] = { 0 };
	
	int tmp1;
	int tmp2;

	int count = 1;

	for (int i = 1; i <= 6; i++) {
		for (int j = 0; j < i; j++) {
			switch (i) {
			case 1: firstPrize[count] = 5000000;
				break;
			case 2: firstPrize[count] = 3000000;
				break;
			case 3: firstPrize[count] = 2000000;
				break;
			case 4: firstPrize[count] = 500000;
				break;
			case 5: firstPrize[count] = 300000;
				break;
			case 6: firstPrize[count] = 100000;
				break;
			}
			count++;
		}
	}
	count = 1;
	for (int i = 0; i < 5; i++) {
		for(int j = 0; j < pow(2,i); j++) {
			secondPrize[count] = 5120000 / pow(2,i);
			count++;
		}
	}

	cin >> n;
	int *number = new int[n*2];
	for (int i = 0; i < n; i++) {
		cin >> number[2*i] >> number[2*i+1];
	}

	for (int i = 0; i < n; i++) {
		tmp1 = number[2 * i] < 22 ? firstPrize[number[2 * i]] : 0;
		tmp2 = number[2 * i + 1] < 32 ? secondPrize[number[2 * i + 1]] : 0;
		//cout << "1: " << tmp1 << " 2: " << tmp2 << "\n";
		cout << tmp1 + tmp2 << endl;
	}

	delete[] number;

	return 0;
}