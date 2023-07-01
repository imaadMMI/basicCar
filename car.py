command = ""
started = False

while True:
    command = input(">")
    if command.lower() == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started...")

    elif command.lower() == "help":
        print("""start - to start the car
stop - to stop the car
quit - to exit the program""")

    elif command.lower() == "stop":
        if not started:
            print("The car has already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command.lower() == "quit":
        print("Thanks for playing!")
        break
    else:
        print("Sorry I didn't understand that. Type help to see the proper options.")
