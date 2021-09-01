#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main(int argc, char const *argv[])
{
    int num;
    cin>>num;
    string * str = new string [num];
    for (int i = 0; i < num; i++){
        cin>> str[i];
        reverse(str[i].begin(), str[i].end());//문자열 뒤집음

    }

   bool isdiff;
     for (int i = 1; i <= 100; i++)//자리수 는 100과 같거나 작다
    { 
        string temp;
        isdiff=true;
        for (int j = 0; j < num; j++)//리스트 순회
        {
            if (!isdiff) break;
            temp=str[j].substr(0,i);
            for (int k = 0; k < num; k++)//리스트 비교
            {
                if (j==k) continue;//같은 리스트면 탈주
                if(isdiff){ 
                    if(temp.compare(str[k].substr(0,i))==0){ //순회 중 하나라도 숫자가 같으면 
                        isdiff=false; // false로 지정 
                        break;//토낌
                    }
                }else break; // 이미 자리가 같으면 나머지 검사할 가치가 없음

            }
             
        }
        if(isdiff){ // 여기 까지 내려온것이면 제일 마지막까지 가서 아쉽게 틀린거거나 True임
                 cout<< i<<endl;
                 break;
             }  
        
    }


    return 0;
}
