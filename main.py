# using for iteration 2
import pandas as pd

count = 1
# master list with all the users added
master_lst = []

# list holding all users who meet requirements
retirement_ready = []

# list holding all users who are not older than 59 1/2
not_old_enough = []

# list holding all users who do not have 25x their salary in 401k
not_enough_money = []

# list holding all users who do not meet any requirements
no_requirement_met = []


# function to get user data (this will be revised to be more agile)
def user_InputMaster(name, age, salary, balance, SSN, email):
    for inputs in range(0, 1):
        info = [name, age, salary, balance, SSN, email]
        master_lst.append(info)


def retirement_check(listOfCustomers):
    counter = 0

    # loops through master list and checks the age and 401k balance of each individual customer
    for subsetData in listOfCustomers:
        ageCheck = subsetData[1]
        salaryCheck = subsetData[2]
        balanceCheck = subsetData[3]

        # if the customer meets requirements, input their information into the retirement_ready list
        if ageCheck >= 59.5 and balanceCheck > salaryCheck*25:
            print("User " + str(counter+1) + " can retire.")
            retired = subsetData.copy()
            retirement_ready.append(retired)

            print(retirement_ready)

        elif ageCheck <= 59.5 and balanceCheck > salaryCheck*25:
            print("User " + str(counter+1) + " is not of age to retire.")
            tooYoung = subsetData.copy()
            not_old_enough.append(tooYoung)

            print(not_old_enough)

        elif ageCheck >= 59.5 and balanceCheck < salaryCheck*25:
            print("User " + str(counter+1) + " does not have the recommended balance in their 401k to retire.")
            broke = subsetData.copy()
            not_enough_money.append(broke)

            print(not_enough_money)

        else:
            print("User " + str(counter+1) + " does not meet any requirements to retire.")
            noChance = subsetData.copy()
            no_requirement_met.append(noChance)

            print(no_requirement_met)

        counter += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    inputCustomerNum = int(input("How many users are you adding?\n"))

    # While loop to consecutively add information to the list
    while True:
        try:
            inName = str(input("Enter user number " + str(count) + "'s name:\n"))
            inAge = int(input("Enter user number " + str(count) + "'s age:\n"))
            inSalary = int(input("Enter user number " + str(count) + "'s salary:\n"))
            inBalance = int(input("Enter user number " + str(count) + "'s 401k balance:\n"))
            inSSN = int(input("Enter user number " + str(count) + "'s Social Security Number:\n"))
            inEmail = str(input("Enter user number " + str(count) + "'s email address:\n"))

            # calls calc function to insert into list
            user_InputMaster(inName, inAge, inSalary, inBalance, inSSN, inEmail)
            count += 1
        except ValueError:
            print("Please check your values again.\n")
            continue

        if count - 1 == inputCustomerNum:
            break
    # print the master list of all users inputted
    print("Here is a full list of all users: \n" + str(master_lst))

    retirement_check(master_lst)
