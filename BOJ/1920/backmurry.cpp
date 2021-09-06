#include<iostream>
#include<cstdio>
#include<algorithm>
 
using namespace std;
 
int arr[100001];

void binary_Search(int n, int key){
 
    int start = 0;
    int end = n-1;
    int mid;
 
    while(end - start >= 0){
        mid = (start + end)/2;
        if(arr[mid] == key){ 
            printf("1\n");
            return ;
        }else if(arr[mid] > key) end = mid - 1; else start = mid + 1;
    }
    printf("0\n");
    return ;
}
 
int main(void){
 
    int n, m, temp;

    scanf("%d", &n);
    for(int i=0; i<n; i++)scanf("%d", &arr[i]);

    sort(arr, arr+n);  
    scanf("%d", &m);
    for(int i=0; i<m; i++){
        scanf("%d", &temp);
        binary_Search(n, temp);
    }
 
    return 0;
}

