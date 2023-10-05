class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_price(self, new_price):
        self.price = new_price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def __str__(self):
        return f"Name: {self.name}\nPrice: ${self.price:.2f}\nQuantity: {self.quantity}"

class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)
        print(f"Product '{product.name}' added to inventory.")

    def view_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for index, product in enumerate(self.inventory, start=1):
                print(f"{index}. {product.name}")

    def view_product_details(self, index):
        if 0 <= index < len(self.inventory):
            product = self.inventory[index]
            print(product)
        else:
            print("Invalid product index.")

    def update_product_price(self, index, new_price):
        if 0 <= index < len(self.inventory):
            product = self.inventory[index]
            product.update_price(new_price)
            print(f"Price of '{product.name}' updated successfully.")

    def update_product_quantity(self, index, new_quantity):
        if 0 <= index < len(self.inventory):
            product = self.inventory[index]
            product.update_quantity(new_quantity)
            print(f"Quantity of '{product.name}' updated successfully.")

    def remove_product(self, index):
        if 0 <= index < len(self.inventory):
            removed_product = self.inventory.pop(index)
            print(f"Removed product: {removed_product.name}")
        else:
            print("Invalid product index.")

def main():
    inventory_manager = InventoryManager()

    while True:
        print("\nInventory Management Menu:")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. View Product Details")
        print("4. Update Product Price")
        print("5. Update Product Quantity")
        print("6. Remove Product")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(name, price, quantity)
            inventory_manager.add_product(product)
        elif choice == "2":
            inventory_manager.view_inventory()
        elif choice == "3":
            index = int(input("Enter the index of the product to view: "))
            inventory_manager.view_product_details(index)
        elif choice == "4":
            index = int(input("Enter the index of the product to update price: "))
            new_price = float(input("Enter the new price: "))
            inventory_manager.update_product_price(index, new_price)
        elif choice == "5":
            index = int(input("Enter the index of the product to update quantity: "))
            new_quantity = int(input("Enter the new quantity: "))
            inventory_manager.update_product_quantity(index, new_quantity)
        elif choice == "6":
            index = int(input("Enter the index of the product to remove: "))
            inventory_manager.remove_product(index)
        elif choice == "7":
            print("Exiting the Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
