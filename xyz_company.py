 #data storing variables
projectList = []
project = []
projectStatusList = []
projectIndexList = []
numberOfWorkers = 0
projectStatusChoices = ["ongoing", "on hold", "completed"]
saveConfirmation = ["yes","no"]
projectIndex = 0
userChoice = 0
option5Call = ""

# Workers input for the program because no workers are there to assaign, you can also do this in 3rd option
while True:
    numberOfWorkers = input("Enter how many workers are available in the company (for program to start): ")
    
    if numberOfWorkers.isdigit():
        numberOfWorkers = int(numberOfWorkers)
        break
    else:
        print("Input a valid number.")

#main menu
while True:
    if option5Call == "addproject":
        userChoice = 1
        option5Call = "" #to reset option5Call to stop repeating loop when user enter 0 to project code
    else:
        print("XYZ Company".center(60))
        print("Main Menu".center(60))
        print("""
    1. Add a new project to existing projects.
    2. Remove a completed project from existing projects.
    3. Add new Workers to available workers group.
    4. Update details on ongoing projects.
    5. Project Statistics
    6. Exit """)
        print()
        userChoice = (input("Enter your choice: "))

        # to check if the input is a number(.isdigit find refering w3schools.com)
        if not userChoice.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        # then convert the user Choice to an integer
        userChoice = int(userChoice)

    #if choose 1
    if (userChoice == 1):
            print("XYZ Company".center(60))
            print("Add a new project.".center(62))
            print()
            projectCode = (input("Enter project code: "))
            while projectCode in projectIndexList:
                print("Project assaigned with " ,projectCode , " Already Exists , Please Try Again.")
                projectCode = (input("Enter project code: "))
            if (projectCode == "0"):
                continue
            else:
                clientsName = (input("Enter clients name: "))
                startDate = input("Enter start date(date/month/year): ")
                while "/" not in startDate:
                    print("Use the format as:(date/month/year: ")
                    startDate = input("Enter start date(date/month/year): ")
                expectedEndDate = input("Enter expected end date(date/month/year): ")
                while "/" not in startDate:
                    print("Use the format as:(date/month/year: ")
                    expectedEndDate = input("Enter expected end date(date/month/year): ")
                workersNeed = int(input("How many workers need to assign: "))
                #check if enough workers are available
                if (workersNeed > numberOfWorkers+1):
                    print("Not enough Workers")
                    continue

                else:
                    numberOfWorkers = numberOfWorkers-workersNeed

                while True:
                    #to make sure valid input is entered
                    projectStatus = input(f"Whats the project status ({', '.join(projectStatusChoices)}): ").lower()

                    # check if the input is in the list of options given
                    if projectStatus in projectStatusChoices:
                        break  
                        #if the input valid exiting the lop by breaking the loop
                    else:
                        print("Invalid input. Please enter a valid option.")
                        #repeat the loop until input is valid
                #show the information entered before confirm
                print()
                print(f"Information you entered are as below\n"
                f"\n"
                f"  Clients name: {clientsName}\n"
                f"  Start date: {startDate}\n"
                f"  Expected end date: {expectedEndDate}\n"
                f"  Number of workers assigned: {workersNeed}\n"
                f"  Project Status: {projectStatus}")
                print()
                saveConfirmation = input("Do you want to save the project (yes/no)? : ").lower()
                #saving the inputs to the database(lists in this case)
                if (saveConfirmation == "yes"):
                    project = [projectCode,clientsName,startDate,expectedEndDate,workersNeed,projectStatus]
                    projectList.append(project)
                    projectIndexList.append(projectCode)
                    projectStatusList.append(projectStatus)
                    print("Project saved successfully.")

                elif (saveConfirmation.lower() == "no"):
                    print("Project discarded successfully")
                else:
                    print("Invalid Input ")
    # if choose 2
    elif userChoice == 2:
        print("XYZ Company".center(60))
        print("Remove Completed Project.".center(58))
        print()

        projectCodeToRemove = (input("Enter project code: "))

        if projectCodeToRemove in projectIndexList:
            #to check if the entered project code assaign to a project
            print()
            saveConfirmation = input("Do you want to remove the project (yes/no): ").lower()

            if saveConfirmation == "yes":
                # get the index of the project to remove
                projectIndexToRemove = projectIndexList.index(projectCodeToRemove)

                # move assigned workers to available workers pile
                numberOfWorkers += projectList[projectIndexToRemove][4]

                # deleting the saved information
                del projectList[projectIndexToRemove]
                del projectIndexList[projectIndexToRemove]
                del projectStatusList[projectIndexToRemove]

                print("Project removed successfully")
            elif saveConfirmation == "no":
                continue
            else:
                print("Invalid input, please try again")
        else:
            print("Invalid input, try again")
            continue


    #if choose 3
    elif (userChoice == 3):
        print("XYZ Company".center(60))
        print("Add new Workers".center(60))
        print()
        tempWorkers = int(input("Number of workers to add: "))
        #check if enterd number of workers are positive negative number of workers cant be added that reduces the workers count
        if tempWorkers < 0:
            print("Invalid input. Please enter a positive number of workers.")
            continue
        else:
            print()
            saveConfirmation = input("Do you want to add(yes/no)? " ).lower()
            #adding workers to the company
            if saveConfirmation == "yes":
                numberOfWorkers = numberOfWorkers + tempWorkers
                print("Total workers available free = ",numberOfWorkers)
                print("Workers added successfully. ")
            elif saveConfirmation == "no":
                print("Changes not appilied.")
            else:
                print("Invalid project code")
                continue


    #if choose 4
    elif (userChoice == 4):
        print("XYZ Company".center(60))
        print("Update Project Details".center(58))
        print()
        projectIndex = (input("Enter project code: "))
        if (projectIndex == "0"):
            continue
        else:
            #check project code assaign to a project
            if projectIndex in project :
                project [1] = (input("Enter clients name: "))
                project [2] = input("Enter start date(date/month/year): ")
                while "/" not in project [2]:
                    print("Use the format as:(date/month/year: ")
                    project [2] = input("Enter start date(date/month/year): ")
                project [3] = input("Enter expected end date: ")
                while "/" not in project [3]:
                    print("Use the format as:(date/month/year: ")
                    project [3] = input("Enter expected end date(date/month/year): ")
                project [4] = int(input("How many workers need to assign: "))
                if (workersNeed > numberOfWorkers):
                    print("Not enough Workers")
                    continue
                else:
                    numberOfWorkers = numberOfWorkers-workersNeed

                while True:
                    #to make sure valid input is entered
                    project [5] = input(f"Whats the project status ({', '.join(projectStatusChoices)}): ")

                    # check if the input is in the list of options given
                    if project [5] in projectStatusChoices:
                        break
                        if project[5] == "completed":
                            numberOfWorkers = numberOfWorkers + workersNeed
                            print("Workers added to free Workers. ")

                        #if the input valid exiting the lop by breaking the loop
                    else:
                        print("Invalid input. Please enter a valid option.")
                        #repeat the loop until input is valid
                print()
                saveConfirmation = input("Do you want to save the project (yes/no)? : ").lower()
                if (saveConfirmation == "yes"):
                    print("Project updated successfully.")
                elif (saveConfirmation == "no"):
                    print("Changes not applied")
                else:
                    print("Invalid response")
                print(project)

    #if choose 5
    #display all the statistics by counting and referring data storing lists
    
    elif userChoice == 5:
        print("XYZ Company".center(60))
        print("Project Statistics".center(62))
        print()
        onGoingProjects = projectStatusList.count("ongoing")
        onHoldProjects = projectStatusList.count("on hold", )
        completedProjects = projectStatusList.count("completed")
        print("Number of ongoing projects: ", onGoingProjects)
        print("Number of completed projects: ", completedProjects)
        print("Number of on hold projects: ", onHoldProjects)
        print("Number of available workers to assign: ", numberOfWorkers)
        print()
        temp = input("Do you want to add the project (yes/no)? : ").lower()

        if temp == "yes":
            option5Call = "addproject"
        elif temp == "no":
            continue
        else:
            while True:
                temp = input("Invalid choice. Do you want to add the project (yes/no)? : ").lower()
                if temp in ["yes", "no"]:
                    break

    #if choose 6
    #exiting the program
    elif (userChoice == 6):
        print("Exiting the program".center(65))
        exit()
    else:
        print(("Invalid option"))
        print()
        continue