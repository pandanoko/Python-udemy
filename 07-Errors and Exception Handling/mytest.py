def get_int():
    while True:
        try:
            result = int(input("Please type a number"))
        except:
            print("WHOOPS, this is not a number")
            continue
        else:
            print(f"Your typed {result}, thank you")
            break
        #finally:
        #    print("I'm asking again \n")

get_int()