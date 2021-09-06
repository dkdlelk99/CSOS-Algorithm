#include <iostream>
using namespace std;
int main()
{
    int switch_num, std, sex, number, i, k;

    cin >> switch_num; 
    int *arr = new int[switch_num+1];

    for (i = 1; i <= switch_num; i++)cin >> arr[i];
    cin >> std;
    for (k = 0; k < std; k++)
    {
        cin >> sex >> number; 
        if (sex == 1)for (i = 1; i <= switch_num; i++)if(i % number == 0)arr[i] = arr[i]?0:1; //배수마다 스위치 변경 
        if (sex == 2)
        {
            arr[number] = arr[number]?0:1;                        
            for (i = 1; arr[number + i] == arr[number - i]; i++) 
            {
                if (number + i > switch_num || number - i < 1) 
                    break;
                arr[number + i] = arr[number + i]?0:1; 
                arr[number - i] = arr[number - i]?0:1; 
            }
        }
    }
    for (i = 1; i <= switch_num; i++)
    {
        cout << arr[i] << " ";
        if (i % 20 == 0) 
            cout << "\n";
    }

    return 0;
}
