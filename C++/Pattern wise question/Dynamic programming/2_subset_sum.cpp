#include <iostream>
#include <vector>
#include <cstring>
using  namespace std;

bool subsetsum(int arr[], int W , int n){
 if(W==0)
    return true;
 if(n==0)
    return false;
 else if(arr[n-1]<=W)
    return subsetsum(arr , W-arr[n-1] , n-1) or subsetsum(arr , W , n-1);
 else
    return subsetsum(arr , W , n-1);

}

bool subsetsum1(int arr[], int W , int n){
 int i,j;
 //vector<vector<bool>> dp(n+1 , vector<bool>(W+1));
 bool dp[n+1][W+1];

 for(i=0;i<n+1; i++)
    dp[i][0] = true;

 for(i=1; i<W+1; i++)
    dp[0][i] = false;

 for(i=1; i<n+1; i++){
    for(j=1; j<W+1; j++){
        if(arr[i-1]<=j)
            dp[i][j]  = dp[i-1][j-arr[i-1]] or dp[i-1][j];
        if(arr[i-1]>j)
            dp[i][j]  = dp[i-1][j];
    }
 }
 return dp[n][W];
}

// Memorization.
int dp[2000][2000];
bool subsetsum2(int arr[], int W , int n){
 if(n==0)
    return false;
 if(W==0)
    return true;
 else if(arr[n-1]<=W){
    dp[n][W] = subsetsum2(arr , W-arr[n-1] , n) or subsetsum(arr , W , n-1);
    return dp[n][W];
 }
 else{
    dp[n][W] = subsetsum2(arr , W , n-1);
    return dp[n][W];
 }



return false;
}

int main(){
memset(dp , -1 , sizeof(dp));
int arr[] = {2,3,7,8,10};
int sum = 11;
int n = sizeof(arr)/sizeof(arr[0]);

cout<<"subset is present :: "<<subsetsum2(arr , sum , n);
return 0;
}
