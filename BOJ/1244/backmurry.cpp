#include <iostream>
using namespace std;
int main()
{
    int n, std, g, y, i, k;

    cin >> n;
    int *arr = new int[n+1];

    for (i = 1; i <= n; i++)cin >> arr[i];
    cin >> std;
    for (k = 0; k < std; k++)
    {
        cin >> g >> y; 
        if (g == 1)for (i = 1; i <= n; i++)if(i % y == 0)arr[i] = arr[i]?0:1; 
        if (g == 2)
        {
            arr[y] = arr[y]?0:1;                        
            for (i = 1; arr[y + i] == arr[y - i]; i++) 
            {
                if (y + i > n || y - i < 1) 
                    break;
                arr[y + i] = arr[y + i]?0:1; 
                arr[y - i] = arr[y - i]?0:1; 
            }
        }
    }
    for (i = 1; i <= n; i++)
    {
        cout << arr[i] << " ";
        if (i % 20 == 0) 
            cout << "\n";
    }

    return 0;
}
