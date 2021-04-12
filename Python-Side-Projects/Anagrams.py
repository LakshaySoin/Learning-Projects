def Anagram(word1, word2):
    count = 0
    count1 = 0
    the_word = input(word1)
    the_word = the_word.lower()
    w1 = the_word.replace(' ', '')
    count2 = len(w1)
    a_word = input(word2)
    a_word = a_word.lower()
    w2 = a_word.replace(' ', '')
    cool = []
    for i in w1:
        count += 1
        cool.append(i)
    for x in w2:
        count1 += 1
    if count == count1:
        if w1 == '':
            print("Not anagrams")
        elif w2 == '':
            print("Not anagrams")
        for y in w2:
            if y in cool:
                condition = True
            else:
                condition = False
                print('Not anagrams')
                break
        if condition == True:
            print("Anagrams")
        else:
            print("")
    else:
        print("Not anagrams")


Anagram("Enter your first word: ", "Enter your second word: ")