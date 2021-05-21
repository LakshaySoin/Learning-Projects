hour = int(input("Starting time(hours): "))
mins = int(input("Starting time(minutes): "))
dura = int(input("Event duration(minutes): "))

if mins+dura >= 60:
    new_hour = hour + (mins+dura)//60
    new_mins = (mins+dura) % 60
    if new_hour > 24:
        new_hour = new_hour % 24
        print("The time is " + str(new_hour) + " : " + str(new_mins))
    else:
        print("The time is " + str(new_hour) + " : " + str(new_mins))
else:
    print("The time is " + str(new_hour) + " : " + str(new_mins))


