
# List of Functions
# Asking for Number of Students and if entered number is actually valid.

def studentmaker():
    while True:
        try:
            studentamount = int(input("Input how many Students have attended: "))
        except ValueError:
            print("That is not a number")
            continue
        if studentamount == 0:
            print("We need Students not air")
            continue
        elif studentamount >= 0:
            break
    count = 0
    # Making a sentence

    while count < studentamount:
        # We are Trying to input values

        # First we need to make sure it's less than 10
        name = str(input("Input a Name: "))
        if name.isdigit():
            print("You need a Name not Number")
            continue
        elif len(name) > 10:
            print("Please enter Name that is less than 10")
            continue

        # Now we have to try to get a proper Integer
        while True:
            try:
                mark1 = int(input("Input Mark1: "))
                mark2 = int(input("Input Mark2: "))
                mark3 = int(input("Input Mark3: "))
                if mark1 > 100 or mark2 > 100 or mark3 > 100:
                    print("Number is Too Big BRUDA")
                    continue
            except ValueError:
                print("One Mark is not a Digit")
                continue
            break

        # Now we have to type the line
        theline = format(name.ljust(10, )) + "|" + str(mark1).center(10) + "|" + str(mark2).center(10) + "|" + str(mark3).center(10) + "|" + "\n"
        print(theline)
        with open("sia.txt", mode="a", encoding="UTF-8") as fa:
            fa.write(theline)

        # Adding the amount of Students we have entered, so it stops
        count += 1



while True:
    print("\nWhat do you want to do")
    print("1 Create a New File")
    print("2 Append New Children")
    print("3 Edit Student")
    print("4 End this program")
    choice = 0
    while True:
        try:
            choice = int(input("Answer: "))
        except ValueError:
            continue
        if 0 < choice < 5:
            break
    if choice == 1:
        thestringer = f'{"Name":<10}|{"Mark 1":^10}|{"Mark 2":^10}|{"Mark 3":^10}|\n{"-" * 44}\n'
        print(thestringer)
        with open("sia.txt", mode="w", encoding="UTF-8") as fw:
            fw.write(thestringer)
        studentmaker()
        continue
    elif choice == 2:
        studentmaker()
        continue
    elif choice == 4:
        print("Shutting Downnn.....")
        break
    elif choice == 3:
        while True:
            with open("sia.txt", mode="r", encoding="UTF-8") as fr:
                lines = fr.readlines()
                studentnum = input('Which student do you want to edit (if none, type "none"): ')
                if studentnum == "none":
                    break
                elif studentnum.isdigit() and int(studentnum)+2 <= len(lines):
                    studentnum = int(studentnum)+1
                    theline = lines[studentnum]
                else:
                    print("this aint a valid Number or Word")
                    continue


            while True:
                print(f'{"Options":^20}')
                print("1 I want to edit Mark 1")
                print("2 I want to edit Mark 2")
                print("3 I want to edit Mark 3")
                print("4 I dont want to edit anything")


                try:
                    choice2 = int(input("Choice: "))
                    if 1 > choice2 > 4:
                        print("This aint an option")
                        continue
                except ValueError:
                    print("This aint a valid number")

                if choice2 == 1:
                    while True:
                        try:
                            mark = int(input("Input Number: "))
                            if mark > 100:
                                print("Number is Too Big BRUDA")
                                continue
                        except ValueError:
                            print("Mark is not a Digit")
                            continue
                        break

                    line1 = theline[:14]
                    line2 = theline[17:]
                    newline = line1 + str(mark).center(3) + line2
                    lines[studentnum] = newline
                    lines = "".join(lines)
                    with open("sia.txt", mode="w", encoding="UTF-8") as fw:
                        fw.write(lines)
                elif choice2 == 2:
                    while True:
                        try:
                            mark = int(input("Input Number: "))
                            if mark > 100:
                                print("Number is Too Big BRUDA")
                                continue
                        except ValueError:
                            print("Mark is not a Digit")
                            continue
                        break

                    line1 = theline[:25]
                    line2 = theline[28:]
                    newline = line1 + str(mark).center(3) + line2
                    lines[studentnum] = newline
                    lines = "".join(lines)
                    with open("sia.txt", mode="w", encoding="UTF-8") as fw:
                        fw.write(lines)
                elif choice2 == 3:
                    while True:
                        try:
                            mark = int(input("Input Number: "))
                            if mark > 100:
                                print("Number is Too Big BRUDA")
                                continue
                        except ValueError:
                            print("Mark is not a Digit")
                            continue
                        break
                    line1 = theline[:36]
                    line2 = theline[39:]
                    newline = line1 + str(mark).center(3) + line2
                    lines[studentnum] = newline
                    lines = "".join(lines)
                    with open("sia.txt", mode="w", encoding="UTF-8") as fw:
                        fw.write(lines)
                elif choice2 == 4:
                    print("Ok sorry...")
                    break
                break




