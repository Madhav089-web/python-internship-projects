tickets = {}

print("Welcome to the Ticket Counter")


while True:
    
     name = input("Enter your name: ")
     age = int(input("Enter your age: "))

     if age < 18:
       print(f"Sorry {name}, you are under 18, so you are not permitted !")
       break

    

     print(f"Hello {name}, you are eligible to continue.")
  
     print("1. Book Ticket")
     print("2. Cancel Ticket")
     print("3. Exit")
     choice = input("Choose an option: ")

     if choice == "1":
        if name in tickets:




            print("You already have a ticket booked.")
        else:
            tickets[name] = "Booked"



            print("Your ticket has been booked successfully!")

     elif choice == "2":
        if name in tickets:


            
            del tickets[name]
            print("Your ticket has been canceled successfully!")
        else:
            print("You have no ticket to cancel.")

     elif choice == "3":
        print("Thank you for visiting, goodbye!")
        break

     else:
        print("Invalid choice! try again.")
