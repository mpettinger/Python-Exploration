while True:

    mynumber = input("Please enter your number: ")

    if mynumber == "q":
        print("Quitting program")
        quit()

    answer = int(mynumber) * (int(mynumber)>=5)

    print(f"The answer is {answer}")
