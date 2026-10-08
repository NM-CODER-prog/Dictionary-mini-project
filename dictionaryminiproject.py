while True:
    print("\nDictionary Management system")
    print("1.Add a word")
    print("2. Search for Meaning")
    print("3.Display All Words")
    print("4.Update Meaning")
    print("Delete Word")
    print("6.Exit")
    dictionary =[]
    Choice = input("Enter your Choice")


    if Choice == "1":
        Word  =  input("Enter the word").lower()
        meaning = input("Enter the meaning : ")
        dictionary[Word] = meaning
        print("word added successfully!")

    elif Choice == '2':
        word = input("Enter the word to search: ").lower()
        if word in dictionary:
            print("Meaning:",dictionary[word])
        else:
            print("Word not found in the dictionaru.")

    elif Choice == '3':
        if dictionary:
            print("Word and their meanings: ")
            for word, meaningin  in dictionary.iteams():
                print(f"{Word}: {meaning}")
        else:
            print("Dictionary is empty.")

    elif Choice == '4':
        word = input("Enter the word to update meaning: ").lower()
        if word in dictionary:
            new_meaning = input("Enter the new meaning: ")
            dictionary[Word] = new_meaning
            print("Meaning updated successfully!")
            print("updated Meaning:", dictionary[Word])
        else:
            print("Word not found in the dictionary.")

    elif Choice == '5':
        Word = input("Enter Delete word: ").lower()
        if Word in dictionary:
             del dictionary[Word] 
             print("Word deleted Succesfully!")
        else:
            print("Word not deleted.")
    elif Choice == '6':
        word = input("Enter Exit: ")
        break
    else:
        print("invalid choice. enter valid option.")

    


