#include <unordered_map>
#include <iostream>
//#include <initializer_list>
#include <iterator>
#include <string>

using namespace std;



int main()
{
    unordered_map<string, int> Mymap;
    
    Mymap.insert(make_pair("Fred", 0));
    Mymap.insert(make_pair("Alan", 1));
    Mymap.insert(make_pair("Bob", 1));
    Mymap.insert(make_pair("Jane", 2));
   
    
    // display contents " [c 3] [b 2] [a 1]"
  /*  for (const auto& c : Mymap) {
        cout << " [" << c.first << ", " << c.second << "]"<<endl;
    }*/
   
    unordered_map<string, int>::iterator it = Mymap.begin();
    
    while(it != Mymap.end())
    {
       cout << " [" << it->first << ", " << it->second << "]"<<endl;
        it++;
    }
    
    cout << endl;


     
}