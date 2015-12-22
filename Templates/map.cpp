#include <iostream>
#include <map>
#include <string>
#include <iterator>

using namespace std;

int main()
{
    map<string, int> myMap;
    
    
    // Inserting data in map
    myMap.insert(make_pair("Fred",0));
    myMap.insert(make_pair("Alan", 1));
    myMap.insert(make_pair("Bob", 1));
    myMap.insert(make_pair("Jane", 2));

    // Iterate through all elements in map
    map<string, int>::iterator it = myMap.begin();
    
    while(it != myMap.end())
    {
        cout<<  " [" << it->first<<" ,  "<<it->second << " ]"<<endl;
        it++;
    }
    

    return 0;
}