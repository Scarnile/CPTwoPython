class ActivityOne:

    def run(self): 
        mylist = [10, 15, 20, 30]
        average = 0

        for number in mylist:
            average += number 

        average /= len(mylist)

        print(f"The average of {mylist} is {average}")

class ActivityTwo: 
    def run(self): 
        people = [
            ("Kurt", 15),
            ("Carl", 23),
            ("JK", 45),
            ("James", 60),
            ("Kelvin", 39),
            ("Haze", 18),
            ("Gaze", 10),
            ("Soap", 20),
            ("Price", 23),
            ("McQueen", 80),
            ("Bascreveil", 50),
        ]

        limit_age = int(input("Enter an Age: "))

        print(f"\nPerson with the lower age than {limit_age}")

        for name, age in people:
            if age < limit_age:
                print(f"Name: {name} Age: {age}")

class ActivityThree: 
    def run(self): 
        list_one = [1, 20, 3, 6, 8, 9, 10, 7, 12, 21, 18]
        list_two = [10, 2, 30, 15, 8, 21, 13, 18, 28, 25, 16]

        print("List One:", list_one)
        print("List Two:", list_two)

        print("\nAll same numbers on both List:", end=" ")

        # Loop through list_one
        for i in range(len(list_one)):
            # For each number, check in list_two
            for j in range(len(list_two)):
                if list_one[i] == list_two[j]:
                    print(list_one[i], end=", ")

activityOne = ActivityOne()
activityTwo = ActivityTwo()
activityThree = ActivityThree()
activityOne.run()
activityTwo.run()
activityThree.run()