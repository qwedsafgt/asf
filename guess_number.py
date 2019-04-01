import random
the_number=random.randint(1,100)
while True :
    try:
        the_number=int(input())
    except ValueError:
        print("you must enter an integer!")

    if the_number < guess_number :
        print("It is too large！")
    elif the_number >  guess_number:
        print("It's too small!")
    elif the_number == guess_number:
        print("congratulations!")
        exit(0)
