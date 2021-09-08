#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int min(int a, int b) {
    return a > b ? b : a;
}

int main() {

    int n;
    cin>>n;
    vector<int> list(n + 1);
  

    list[1] = 0;
    for(int i = 2; i <= n; i++) {
        list[i] = list[i-1] + 1;
        if (!(i % 2)) list[i] = min(list[i], list[i/2] + 1);
        if (!(i % 3)) list[i] = min(list[i], list[i/3] + 1);
    }

    cout<< arr[n]<<endl ;
    
    return 0;
}
