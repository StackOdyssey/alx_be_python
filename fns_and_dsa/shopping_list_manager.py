shopping_list = []

def display_list():
    print("*******Shopping List Manager*******")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    
    while True:
        display_list()
        user_input = int(input("Please enter your choice : "))
        if user_input == 1:
            add_to_list()
        elif user_input == 2:
            remove_item()
        elif user_input == 3:
            print_list()
        elif user_input == 4:
            byebye()
        else:
            invalid()
      
def add_to_list():
    user_add = input("Please add item to the list : ").lower()
    if user_add in shopping_list:
        print("This item already exist")
    else:
        shopping_list.append(user_add)
def remove_item():
    print(shopping_list)
    user_add = input("Please choose the item to be removed : ").lower()
    if user_add in shopping_list:
        shopping_list.remove(user_add)
        print(f"The {user_add} has been removed from the list")
    else:
        print("Item not found in the list.")
def print_list():
    for item in shopping_list:
        print(f"- {item}")
def byebye():
    print("See you soon!!")
    exit()
def invalid():
    print("Invalid choice. Please try again.")

main()
