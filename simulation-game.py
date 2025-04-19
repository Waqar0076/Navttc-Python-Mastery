print("-- Wellcome to Student Simulation Game!!!! --")

choice = int(input("""Select an Action you want to perform?
        1- Study
        2- Rest
        3- Exercise
"""))

match choice:
    case 1:
        print("You select an option Study...")
        studyChoice = int(input("""you want to study Alone or with Friends>>?
            1- Alone
            2- Friends
"""))
        if(studyChoice ==  1):
            print("you select an option to study ALone!!! \nKeeps working hard")
        elif(studyChoice == 2):
            print("you select an option to study with Friends !!! \nstudy hard !!!")
        else:
            print("invalid Choice....")

    case 2:
        print("You select an option for Rest...")
        restChoice=int(input("""you want to Sleep or go for outing>?
            1- Sleep
            2 - Outing
"""))
        if(restChoice == 1):
            print("you select option for sleep \nSweet Dreams")
        elif(restChoice == 2):
            print("you select option for outing \nEnjoy the nature")
        else:
            print("Invalid Choice")

    case default:
        print("Try Again.........")

print("------- Program Execute Sucessfully -------")


