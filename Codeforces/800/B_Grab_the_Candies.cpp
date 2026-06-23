#include <bits/stdc++.h>
using namespace std;
 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
     int a;
     cin>> a;
     while(a--){
        int n,p1=0,p2=0;
        cin>>n;
        vector<int> num(n);
        for(int i=0;i<n;++i){cin>> num[i];
         if(num[i]%2==0){
              p1+=num[i];
          }
         else{ p2+=num[i];}
        }
             if(p2>=p1){cout<<"NO"<<'\n';}
             else{cout<<"YES"<<'\n';}
       }
     
    return 0;
}
