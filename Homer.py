# code prints the time (in mins) needed to eat different lunch options combining hamburgers and cheeseburgers, the amount of hamburgers and cheeseburgers 

class Burger:
    def __init__(self, eating_time):
        self.eating_time = eating_time


class Hamburger(Burger):
    ingredients = 'ham'


class CheeseBurger(Burger):
    ingredients = 'cheese'
    

class LunchSolver:
    
    def __init__(self, time_for_lunch):
        self.time_for_lunch = time_for_lunch

    # def __str__(self):
    #     return f"The time to have lunch is {self.time_for_lunch} mins" 
    
    def solveLunch(self, hamburger, cheeseburger):
        options = []
        sum = 0
        print(hamburger)
        sequence_ham = range(0, self.time_for_lunch, hamburger.eating_time)
        sequence_cheese = range(0, self.time_for_lunch, cheeseburger.eating_time)

        for x in sequence_ham:
            for y in sequence_cheese:
                sum = x + y
                h = x / (hamburger.eating_time)
                c = y / (cheeseburger.eating_time)
                h_tuple = 'hamburgers %d' % h
                ch_tuple = 'cheeseburgers %d' % c
            
                tuple = (sum, h_tuple , ch_tuple) 
                if sum <= self.time_for_lunch:
                    options.append(tuple)

        options_sorted = sorted(options, reverse=True)

        for option in options_sorted:
            print(option)    

hamburger = Hamburger(2)
cheeseburger = CheeseBurger(1)
lunch = LunchSolver(20)
lunch.solveLunch(hamburger, cheeseburger)


