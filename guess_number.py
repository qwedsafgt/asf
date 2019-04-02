import random
the_number=random.randint(1,100)
while True :
    try:
        guess_number=int(input())
        Judgement_input()

    except ValueError:
        print("You must enter an integer!")

    def Judgement_input():
        if the_number < guess_number:
            print("It's too large!")
    elif the_number > guess_number:
            print("It's too small!")
        elif the_number == guess_number:
            print("congratuations!")
            exit(0)
