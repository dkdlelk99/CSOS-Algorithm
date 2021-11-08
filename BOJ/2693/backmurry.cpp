#include <iostream> 
#include <algorithm> 
#include <vector> 
using namespace std; 
int main() { 
    int n; 
    vector<int> v(10); 
    cin >> n; 
    
    for (int i = 0; i < n; i++) {
         for (int j = 0; j < 10; j++) 
         cin >> v[j]; 
         sort(v.begin(), v.end()); 
         cout << v[7] << endl; 
         } 
         return 0; 
 }


