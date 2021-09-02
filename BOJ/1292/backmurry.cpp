#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char const *argv[])
{
    int a,b;
    int total=0; 
    int temp = 0;
    vector<int> v(1000);
    cin>>a>>b;
    for (int i = 1;temp < 1000;i++ ) for (int j = 0; j < i && temp < 1000; j++)v[temp++] = i;
    for (int i = a-1; i <= b-1; i++) total += v[i];
    cout<< total<<endl ;
    return 0;
}
