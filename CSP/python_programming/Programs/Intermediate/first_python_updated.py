#DD Period 7 First Python Program, but updated!

def user():
    user_name = input("Hello human. What string of characters would you like me to call you to get your attention?\n")
    return user_name

user_name = user()
print(f"Hello, {user_name}, I would like your attention now.")
