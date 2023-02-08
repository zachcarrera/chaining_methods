class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0

    def display_info(self):
        """ func that prints out all of User's attributes """
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_reward_member)
        print(self.gold_card_points)
        return self

    def enroll(self):
        """ enroll a user if they are not already enrolled """
        if self.is_reward_member:
            print(f"{self.first_name} is already a member")
        else:
            self.is_reward_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        """ spend a user's points if they have enough points to spend """
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print(f"{self.first_name} does not have enough points.")
        return self

# user 1
john_doe = User("John", "Doe", "jdoe@email.com", 25)

# display info, enroll, spend 50 points, and display info of user 1
john_doe.display_info().enroll().spend_points(50).display_info()


# user 2
jack_smith = User("Jack", "Smith", "jsmith@email.com", 40)

# enroll, spend 80 points and display info of user 2
jack_smith.enroll().spend_points(80).display_info()

# user 3
jane_williams = User("Jane", "Williams", "jwilliams@email.com", 30)

# display info, and try to spend 80 for user 3
jane_williams.display_info().spend_points(40)
