def main():
    problem1()
    problem2()
    problem3()
    problem4()

    #created an array and used built functions to remove itmes from the array


def problem1():
    arrayForProblem2 = ['Kenn', 'Kevin', 'Erin', 'Meka']
    print(arrayForProblem2[2])
    print(arrayForProblem2.__len__())
    print(arrayForProblem2.pop(1))
    print(arrayForProblem2.pop(2))

#Python Program that Creates a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.



def problem2():
    userInput = ""
    while(userInput != 'q'):
        userInput = input("Enter something to quit the program")

def problem3():
    myPeople = {
        "Jonathan": "John",
        "Michaek":"Mike",
        "William":"Bill",
        "Robert":"Rob"
    }
    print(myPeople)
    print(myPeople["William"])

def problem4():
    numArray = [1,2,3,4,5]
    for i in range( len(numArray) - 1, -1, -1) :
        print(i)


def problem5():

    totalArray = [1,2,3,4,5,6,7,8,9,10]

    playerOne = int(input("how many numbers in an array are higher, lower, or equal to it."))





if __name__ == '__main__':
        main()
