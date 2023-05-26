from functions import *

def menu():
    print("\n==== Programming Quotes ====")
    print("1. Random quote")
    print("2. All quotes")
    print("3. Add a new quote")
    print("4. Exit")

def main():
    while True:
        quotes = load_quotes("quotes.txt")
        menu()

        choice = input("Choose your an action (1-4): ")
        
        if choice == "1":
            print_quote(random_quote(quotes))
	    count = int(input("Enter the number of quotes to display: "))
    	    display_quotes(quotes, count)
        elif choice == "2":
            view_quotes(quotes)
	    count = int(input("Enter the number of quotes to display: "))
	    display_quotes(quotes, count)        
        elif choice == "4":
            print("Good bye...")
	    count = int(input("Enter the number of quotes to display: "))
	    display_quotes(quotes, count)
            break
        else:
            print("Invalid input")
	    count = int(input("Enter the number of quotes to display: "))
	    display_quotes(quotes, count)
if __name__ == "__main__":
    main()
