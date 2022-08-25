#include <iostream>

using namespace std;

class Solution {
public:
    bool isHappy(int n) {
      int fast = n , slow = n;
      while(true){
          slow = sqr_num(slow);
          fast = sqr_num(sqr_num(fast));
          if(slow==fast) break;
      }
        return slow==1;
    }

    int sqr_num(int n){
        int sum=0;
        int digit=0;
        while(n > 0){
        int digit = n%10;
        sum += digit*digit;
        n = n/10;

        }
        return sum;
    }
};




class Solution{
public:
    int isHappy(int N){
        // code here
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int N;
        cin>>N;
        Solution ob;
        cout << ob.isHappy(N) << endl;
    }
    return 0;
}
// } Driver Code Ends
