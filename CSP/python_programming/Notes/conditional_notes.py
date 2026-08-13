#DD Period 7 Conditional Notes

homework_done = input("Did you do your homework? (Yes/No) ").capitalize().strip()

if "Yes" in homework_done and "No" in homework_done or "Yesn't" in homework_done:
    print("You can't both do and not do your homework, kiddo!")

elif "No" in homework_done:
    print("You need to do your homework, failure!")

elif "Yes" in homework_done:
    print("Good job, you can do what you want!")

elif "Rawr" in homework_done:
    print("OH MY GOD MY KID TURNED INTO A DINOSAUR!!!!! RUUUUNNN!!!!")

else:
    print("Hmmmmm, that sounds like something you made up...")
    import time
    time.sleep(1)
    are_you_sure = input("ARE YOU SURE YOUR HOMEWORK IS DONE?!?! ").capitalize().strip()
    if "Yes" in are_you_sure:
        print("Okay, I believe you...")
    elif "No" in are_you_sure:
        print("I knew it! You need to do your homework, failure!")

    else:
        print("Alright, I'm done. YOU'RE GROUNDED FOR LIFE!")

import random
grade = random.randint(0, 100)
if grade >= 90:
    print("You got an A! Great job!")
elif grade >= 80:
    print("You got a B! Good job!")
elif grade >= 70:
    print("You got a C! You passed!")
elif grade >= 60:
    print("You got a D! You barely passed...")
else:
    print("You got an F! You failed...")
    print("I knew I was right to name you Failure when you popped out!")

print("Your grade was:", grade)