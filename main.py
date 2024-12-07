import os
import sys

def main():
    """Entry point of the application."""
    print("Welcome to the main.py script!")
    
    # Example functionality
    while True:
        print("\nChoose an option:")
        print("1. Greet")
        print("2. Show Current Directory")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            greet()
        elif choice == '2':
            show_current_directory()
        elif choice == '3':
            print("Exiting the script. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def greet():
    """Greet the user."""
    name = input("Enter your name: ")
    print(f"Hello, {name}! Nice to meet you.")

def show_current_directory():
    """Display the current working directory."""
    cwd = os.getcwd()
    print(f"Current Working Directory: {cwd}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting gracefully.")
        sys.exit(0)
