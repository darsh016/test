#include<iostream>
#include<map>
using namespace std;

int main()
{
    int n;
    cin>>n;
    map<string,int> m;
    for(int i =0; i<n; i++)
    {
        string s;
        cin>>s;
        m[s]++;
    }
    for(auto &val:m)
    {
        cout<<val.first<<" "<<val.second<<endl;
    }
    return 0;





}