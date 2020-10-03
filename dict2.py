def main():
    persons = []

    while True:
        person = {}

        person["first"] = input("enter the first name of a person:")
        person["last"] = input("enter the last name of a person:")
        persons.append(person)
        answer = input("enter more persons?")
        if answer.lower() == "n":
            break
    print(persons)


if __name__ == '__main__':
    main()
