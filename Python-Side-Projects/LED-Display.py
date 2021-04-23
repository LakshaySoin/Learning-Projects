row1 = {'1':'#','2':'###','3':'###','4':'# #','5':'###','6':'###','7':'###','8':'###','9':'###','0':'###'}
row2 = {'1':'#','2':'  #','3':'  #','4':'# #','5':'#  ','6':'#  ','7':'  #','8':'# #','9':'# #','0':'# #'}
row3 = {'1':'#','2':'###','3':'###','4':'###','5':'###','6':'###','7':'  #','8':'###','9':'###','0':'# #'}
row4 = {'1':'#','2':'#  ','3':'  #','4':'  #','5':'  #','6':'# #','7':'  #','8':'# #','9':'  #','0':'# #'}
row5 = {'1':'#','2':'###','3':'###','4':'  #','5':'###','6':'###','7':'  #','8':'###','9':'###','0':'###'}

def LedDisplay(num):
    while True:
        try:
            ask = input(num)
            user = int(ask)
            if user >= 0 and user <= 9:
                user = str(ask)
                print(row1[user])
                print(row2[user])
                print(row3[user])
                print(row4[user])
                print(row5[user])
                num = "Enter your number (Enter a anything else to stop): "
                continue
            elif user > 9:
                for i in str(user):
                    print(row1[i], end = ' ')
                print('')
                for i in str(user):
                    print(row2[i], end = ' ')
                print('')
                for i in str(user):
                    print(row3[i], end = ' ')
                print('')
                for i in str(user):
                    print(row4[i], end = ' ')
                print('')
                for i in str(user):
                    print(row5[i], end = ' ')
                print('')
            else:
                print("Try again")
                continue
        except ValueError:
            print("Goodybe")
            break

LedDisplay("Enter your number (Enter anything else to stop): ")
