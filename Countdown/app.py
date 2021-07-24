import datetime

goal_with_date = input(
    "Enter your goal with a deadline separated by a comma(EX: Learn Python, 20.06.2021): ")

goal, date = goal_with_date.split(", ")
[day, month, year] = map(int, date.split("."))

today = datetime.date.today()
someday = datetime.date(year, month, day)

diffrence = today - someday

print(
    f"Dear user! Time remaining for your goal: {goal} is {diffrence.days} days.")
