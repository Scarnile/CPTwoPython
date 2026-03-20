class ActivityOne:

    def run(self): 
        mylist = [10, 15, 20, 30]
        average = 0

        for number in mylist:
            average += number 

        average /= len(mylist)

        print(f"The average of {mylist} is {average}")

activityOne = ActivityOne()
activityOne.run()