#include <iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    int a;
    cin>>a;
    int * list = new int [a];
    int temp;
    for (int i = 0; i < a; i++){
        cin>> list[i];
    }
    if (a == 1) {
       cout<< list[0]*list[0]<<endl;
    }
    else {
    for (int i = 0 ; i< a-1 ; i++){
        for (int j = i+1; j< a; j++){
            if (list[i]>list[j]){
                temp = list[i];
                list[i]=list[j];
                list[j]=temp;
            }
        }
    }
    cout<< (list[0]*list[a-1])<<endl;
    }
    
    return 0;
}
