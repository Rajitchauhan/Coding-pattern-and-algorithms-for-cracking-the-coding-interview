#include <iostream>
#include <cstring>
#include <vector>
using  namespace std;

/*
int knapsack(int arr[] , int val[], int W , int n){
  if(n==0 or W==0)
    return 0;
  if(arr[n-1]<=W)
    return max(val[n-1]+knapsack(arr , val , W-arr[n-1] , n-1) , knapsack(arr , val , W , n-1));
  else if(arr[n-1]>W)
    return knapsack(arr , val , W , n-1);

}

//int t[W+1];
//memset(t , -1 , sizeof(t));

// memorization.
int knapsackRec(int wt[] , int val[], int W , int n , int **dp){
  if(n==0 or W==0)
    return 0;
  if(dp[n][W] != -1)
    return dp[n][W];
  //wt[n-1] bcz n = n-1
  if(wt[n] <= W){
    dp[n][W] = max(val[n]+knapsackRec(wt , val , W-wt[n] , n-1 , dp) , knapsackRec(wt , val , W , n-1 , dp));
    return dp[n][W];
  }
  else if(wt[n] > W){
    dp[n][W] = knapsackRec(wt , val ,W , n-1 , dp);
    return dp[n][W];
  }

}

int knapsack(int wt[] , int val[], int W , int n){
  int** dp;//  double pointer to declair table dynamically

  dp = new int*[n];
  //  loop to create a table dynamically
  for(int i=0; i<n; i++)
    dp[i] = new int[W+1];
  //initially filled with -1
  for(int i=0; i<n; i++){
    for(int j=0 ;j<W+1; j++){
        dp[i][j] = -1;
    }
  }

  return knapsackRec(val , wt , W , n-1 , dp);

}

*/

int knapSack(int W, int wt[], int val[], int n)
{
    int i , j;
  vector<vector<int>> dp(n+1 , vector<int>(W+1));
 //int  dp[n+1][W+1]; it is also valid.
  for(i=0; i<n+1; i++){
    for(j=0 ;j<W+1; j++){
       if(i==0 or j==0)
        dp[i][j]=0;
       else if(wt[i-1]<=j)
        dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]] , dp[i-1][j]);
       else
        dp[i][j] = dp[i-1][j];
    }
  }
 return dp[n][W];
}

// Driver Code
int main()
{
    int val[] = { 60, 100, 120 };
    int wt[] = { 10, 20, 30 };
    int W = 50;
    int n = sizeof(val) / sizeof(val[0]);

    cout<<"max profit is :: " << knapSack(W, wt, val, n);

    return 0;
}
