#code for simple inventory
inventory = {}

def add_item(name, quantity):
  """Adds an item to the inventory or updates its quantity if it already exists."""
  if name in inventory:
    inventory[name] += quantity
  else:
    inventory[name] = quantity
  print(f"Item '{name}' added/updated with quantity {quantity}.")

def get_item_info(name):
  """Retrieves information about an item in the inventory."""
  if name in inventory:
    quantity = inventory[name]
    print(f"Item '{name}' has a quantity of {quantity}.")
  else:
    print(f"Item '{name}' not found in inventory.")

def total_quantity():
  """Calculates and displays the total quantity of all items in the inventory."""
  total = sum(inventory.values())
  print(f"Total quantity of all items: {total}")

while True:
  action = input("Enter 'add', 'info', 'total', or 'quit': ").lower()
  if action == "add":
    name = input("Enter item name: ")
    quantity = int(input("Enter item quantity: "))
    add_item(name, quantity)
  elif action == "info":
    name = input("Enter item name: ")
    get_item_info(name)
  elif action == "total":
    total_quantity()
  elif action == "quit":
    break
  else:
    print("Invalid action. Please try again.")