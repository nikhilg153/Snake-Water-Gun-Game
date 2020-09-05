#snake water gun game:
import random
list = ["s","w","g"]
i = 0
n = 10
human_point = 0
computer_point = 0
while (i<n):
    num = input("Enter s for snake, w for water and g for gun\n")
    comp = random.choice(list)
    if num == comp:
        print("Tie.Point for both is 0\n")

    # when user enter s
    elif num == "s" and comp == "w":
        print(f"your guess is {num} and computer guess is {comp}\n")
        print("You won 1 point\n")
        human_point = human_point + 1
        print(f"your point is {human_point} and computer point is {computer_point}\n")

    elif num == "s" and comp == "g":
        print(f"your guess is {num} and computer guess is {comp}\n")
        print("Computer won 1 point\n")
        computer_point = computer_point + 1
        print(f"your point is {human_point} and computer point is {computer_point}\n")

    # when user enter w
    elif num == "w" and comp == "g":
        print(f"your guess is {num} and computer guess is {comp}\n")
        print("You won 1 point\n")
        human_point = human_point + 1
        print(f"your point is {human_point} and computer point is {computer_point}\n")

    elif num == "w" and comp == "s":
        print(f"your guess is {num} and computer guess is {comp}\n")
        print("Computer won 1 point\n")
        computer_point = computer_point + 1
        print(f"your point is {human_point} and computer point is {computer_point}\n")

    #when user enter g
    elif num == "g" and comp == "s":
        print(f"your guess is {num} and computer guess is {comp}\n")
        print("You won 1 point\n")
        human_point = human_point + 1
        print(f"your point is {human_point} and computer point is {computer_point}\n")

    elif num == "g" and comp == "w":
        print(f"your guess is {num} and computer guess is {comp}\n")
        print("Computer won 1 point\n")
        computer_point = computer_point + 1
        print(f"your point is {human_point} and computer point is {computer_point}\n")
    else:
        print("Invalid input\n")

    i += 1
    print(f"{n-i} is left out of {n}")
print("Game Over\n")
if human_point == computer_point:
    print("Tie\n")
elif human_point>computer_point:
    print("You won and computer lose\n")
else:
    print("Computer won and you lose\n")
print(f"your point is {human_point} and computer point is {computer_point}")


