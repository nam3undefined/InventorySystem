import inventory
from time import sleep as sl
import os

def main() -> int:
    os.system("clear || cls")
    choise = input("Standart size of inventory = 100, u need to update him?[y/n]: ")
    if choise == 'y' or choise == 'Y':
        max_count = int(input("Enter the max count of items in inventory: "))
        inv: object = inventory.Inventory(max_count)
    elif choise == 'n' or choise == 'N':
        inv: object = inventory.Inventory()
    else:
        print("Y or N, stupid! Fuck u idiot!")
        main()

    while 1:
        os.system("clear || cls")
        print("SIMPLE INVENTORY SYSTEM")
        print("AUTHOR: PLAYER_CLI\n")
        print("[1][ADD ITEM]")
        print("[2][REMOVE ITEM]")
        print("[3][SHOW INVENTORY]")
        print("[99][EXIT]")
        
        enter = int(input("[ENTER YOUR CHOISE][:] "))
        match(enter):
            case 1:
                os.system("clear || cls")
                item = input("[ENTER THE NAME OF ITEM TO ADD][:] ")
                inv._add_to_inventory(item)
                print("[ADD NEW ITEM]")
                sl(2)
                os.system("clear || cls")
                
            case 2:
                os.system("clear || cls")
                item = input("[ENTER THE NAME OF ITEM TO REMOVE][:] ")
                inv._remove_from_inventory(item)
                print("[REMOVE ITEM]")
                sl(2)
                os.system("clear || cls")
            case 3:
                os.system("clear || cls")
                c = 1
                items = inv._show_inventory()
                for i in items:
                    sl(0.1)
                    print(f"[{c}][{i}]")
                    c+=1
                enter = input("[PRESS ANY BUTTON TO GO]")
                sl(2)
                os.system("clear || cls")
            case 99:
                exit()
            case _:
                print("[IDIOT U NEED TO CHOISE SOME COMMAND!]")
                sl(1.5)
                
    return 1

if __name__ == "__main__":
    main()