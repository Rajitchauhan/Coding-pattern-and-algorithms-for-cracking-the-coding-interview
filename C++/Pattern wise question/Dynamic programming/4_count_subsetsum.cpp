#include <iostream>
using namespace std;

int countsubset(int arr[] , int n , int sum){
 int i,j;
 bool dp[n+1][sum+1];
 for(i=0; i<n; i++)
    dp[i][0] = 1;
 for(i=1; i<sum; i++)
    dp[0][i] = 0;
 for(i=1; i<n+1; i++){
    for(j=1; j<sum+1; j++){
        if(arr[i-1]<=sum)
            dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j];
        else
            dp[i][j] = dp[i-1][j];
    }
 }
 return dp[n][sum];
}

int main(){
 int arr[]={2,3,5,6,8,10};
 int sum=10;
 int n = sizeof(arr)/sizeof(arr[0]);
 cout<<"count subsetsum is :: "<<countsubset(arr , n,  sum);

return 0;
}
