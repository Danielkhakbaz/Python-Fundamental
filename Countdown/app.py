import datetime

goal_with_date = input(
    "Enter your goal with a deadline separated by a comma(EX: Learn Python, 20.06.2021): ")

goal, date = goal_with_date.split(", ")
[day, month, year] = map(int, date.split("."))

someday = datetime.date(year, month, day)
today = datetime.date.today()

diffrence_in_days = (someday - today).days

if diffrence_in_days > 0:
    print(
        f"Dear user! Time remaining for your goal: {goal} is {diffrence_in_days} days.")
else:
    print("You entered an unvalid date!")
