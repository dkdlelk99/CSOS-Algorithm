#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;


int main() {

    int n,my_num;
    int cnt=0;
    
    

    cin>>n; // 후보수 N
    vector<int> candidate(n-1); // 자신 외의 나머지 후보들 
    cin>>my_num;// 자신의 득표수

    if (n==1){ //후보자가 1이면 0 출력 및 종료
        cout<< 0<<endl;
        return 0;
    }
    
    for (int i = 0; i < n-1; i++)cin>>candidate[i];

    sort(candidate.begin(),candidate.end(),greater<int>());// 내림차 순으로 sort


    while (true)
    {
        for(int i = 0; i < n-1; i++) {  
            if(my_num<=candidate[i]){
                candidate[i]--;
                my_num++;
                cnt++;
            }else break;
        }
        if (my_num>candidate[0]){
            break;
        }
    }

    cout<< cnt<<endl ;
    
    return 0;
}
