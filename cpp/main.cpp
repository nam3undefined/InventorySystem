#include "inventory.hpp"

using namespace std;

int main()
{
    
    Inventory *inv = new Inventory;
    while(true)
    {
        system("clear");
        cout << "[1][ADD ITEM]"<< endl;
        cout << "[2][REMOVE ITEM]"<< endl;
        cout << "[3][SHOW INVENTORY]"<< endl;
        char a;
        int enter;
        cin >> enter;

        if(enter == 1)
        {
            string name;   
            cout << "[ENTER THE NAME OF ITEM][:] ";
            cin >> name;
            inv->add_item(name);
            cin >> a;
            
        }
        if(enter == 2)
        {
            int id;
            cout << "[ENTER THE ID OF ITEM][:] ";
            cin >> id;
            inv->remove_item(id);
            cin >> a;
        }
        if(enter == 3)
        {
            inv->show_items();
            cin >> a;
        }
        

        
    }
    delete inv;
    return 1;
}