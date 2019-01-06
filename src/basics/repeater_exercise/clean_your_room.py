#Take in an input and print the number of times to clean your room.
#Defaults to printing once if no input given


def print_clean_room(number_of_times=1):
    for num in range(number_of_times):
        print("CLEAN UP YOUR ROOM!")


def number_of_times_to_tell():
    return input("How many times do I have to tell you? ")


def main():
    print_clean_room(int(number_of_times_to_tell()))


if __name__ == '__main__':
    main()
