blocks = int(input("Enter the number of blocks: "))

height = 0
condition = True
while condition == True:
    height += 1
    blocks -= height
    if blocks == 0:
        condition = False
    elif blocks < 0:
        condition = False
    else:
        condition = True

print("The height of the pyramid:", height)
