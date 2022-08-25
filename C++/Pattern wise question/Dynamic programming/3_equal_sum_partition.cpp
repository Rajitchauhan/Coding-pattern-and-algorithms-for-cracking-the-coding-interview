#include <iostream>
using namespace std;

bool subsetsum(int arr[] , int n , int sum){
  bool dp[n+1][sum+1];
  int i ,j;
  for(i=0;i<n; i++)
    dp[i][0] = true;
  for(i=1; i<sum; i++)
     dp[0][i] = false;
  for(i=1; i<n+1; i++){
    for(j=1; j<sum+1; j++){
        if(arr[i-1]<=sum)
            dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j];
        else
            dp[i][j] = dp[i-1][j];
    }
  }
  return dp[n][sum];
 }

bool equalsum(int arr[] , int n){
 int sum =0;
 for(int i=0; i<n; i++){
    sum = sum+arr[i];
 }
 if(sum%2!=0)
    return false;
 return subsetsum(arr , n , sum);

}

int main()
{
    int arr[] = {1,5,11,5};
    int n = sizeof(arr)/sizeof(arr[0]);
    cout<<"Equal sum partition :: "<<equalsum(arr , n);
    return 0;
}
