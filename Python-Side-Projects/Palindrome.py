def Palindrome(word):
    count = 0
    a_word = input(word)
    the_word = a_word.replace(' ', '')
    a_list = list(the_word.lower())
    list1 = []
    for i in the_word:
        count += 1
    count1 = count
    if count == len(the_word):
        for x in range(count):
            count1 -= 1
            list1.append(a_list[count1])
        if the_word == '':
            print("It's not a palindrome")
        elif list1 == a_list:
            print("It's a palindrome")
        else:
            print("It's not a palindrome")
    else:
        print("It's not a palindrome")

Palindrome("Enter your word(s): ")
