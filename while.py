def main():
    while True:
        number_as_string = input("enter a number:")
        if number_as_string.isdigit():
            number_as_string = int(number_as_string)
            break
        else:
            print("please enter a digits only")

    print(number_as_string + 2)

    number_as_string = ""
    while not number_as_string.isdigit():
        number_as_string = input("enter a number: ")
        if not number_as_string.isdigit():
            print("please enter digits only")

    print(int(number_as_string)+2)


if __name__ == '__main__':
    main()
