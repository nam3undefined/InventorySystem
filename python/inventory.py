class Inventory:

    def __init__(self, max_count: int = 100) -> None:
        self.max_count = max_count
        self.inventory = []

    def _add_to_inventory(self, item_name: str) -> None:
        if len(self.inventory) + 1 < self.max_count:
            self.inventory.append(item_name)
        else:
            print("Inventory is full! Remove some item to add other item inside!")

    def _remove_from_inventory(self, item_name) -> None:
        if len(self.inventory) > 0:
            self.inventory.remove(item_name)
        else:
            print("Inventory is empty! Add some item to remove him!")

    def _show_inventory(self) -> list:
        return self.inventory