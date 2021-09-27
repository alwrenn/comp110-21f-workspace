"""Choose your own adventure."""

__author__ = "730384411"

from random import randint

points: int 
ram: str = "\U0001F40F"
player: str 


def main() -> None:
    """Entry function."""
    global points
    global ram
    points = 0
    greet()
    print("What do you want to do? ")
    print("1: Finish your COMP110 homeowrk ")
    print("2: Head to Kenan Stadium for clues ")
    print("3: Look for clues on the quad ")
    first_choice: int = int(input("1, 2, or 3? "))
    if first_choice == 1: 
        print(f"You missed your opportunity and the game starts without Ramses {ram}. ")
        print(f"Thank you for playing, {player}! You finished with {points} adventure points. ")
    if first_choice == 2:
        kenan()
    if first_choice == 3:
        quad(points)


def greet() -> None: 
    """Greeting to game."""
    global ram
    global player
    print("Welcome to UNC-Chapel Hill!")
    print(f"UNC football is playing Duke tonight but Ramses {ram} has been stolen by Duke! ")
    print("Can you help us get him back! ")
    player = input("What is your name? ")


def kenan() -> None:
    """Kenan Stadium Events."""
    global ram
    counter = 0
    print("Welcome to Kenan Stadium. Let's look in the locker room... ")
    print("Look! It's Mac Brown. What do you want to ask him? ")
    print("1: Coach, have you seen any clues? ")
    print("2: Coach, who is starting at LB this weekend? ")
    print(f"3: Coach, do you know who stole Ramses {ram}? ")
    mac_choice: int = int(input("1, 2, or 3? "))
    while mac_choice > counter:
        if mac_choice == 1:
            global points
            points = points + 5
            print("Congrats! Coach Brown said he saw a suspicious looking man drop a paper on the ground. ")
            print("Let's look at the note. ")
            mac_choice = 0
        if mac_choice == 2: 
            points = points - 1
            print(f"While you now know who the starting LB is tonight, this doesn't help us find Ramses {ram}. ")
            print("Let's pick a new question! ")
            mac_choice_two: int = int(input("Ask Mac Question 1, 2, or 3? "))
            mac_choice = mac_choice_two
        if mac_choice == 3:
            points = points + 5
            print(f"Coach Brown doesn't know who stole Ramses {ram}, but he did see someone drop a note! ")
            print("Let's look at the note. ")
            mac_choice = 0
    print("The note has the address for Wallace Wade Stadium, let's go! ")
    duke()


def quad(a: int) -> int:
    """Quad Events."""
    global ram
    global points
    global player
    print("Welcome to the quad. Let's walk around! ")
    print("Look! It's Sam Howell, let's talk to him. ")
    print("Oh no! To get to Sam, we have to pass Kevin G. ")
    print("Kevin G is thinking of a random number between 1-10. We have to guess it to cross the quad.")
    kevin: int = 7
    guess: int = int(input("What is your guess? "))
    while guess > 0 and guess < 11: 
        if guess == kevin: 
            points = points + 10
            print("We guessed correctly! What do you want to ask Sam? ")
            print("1: Have you seen any Duke players around campus? ")
            print("2: Is it true you've never eaten a burger? ")
            sam_choice = int(input("1 or 2: "))
            while sam_choice == 1 or sam_choice == 2: 
                if sam_choice == 1:
                    points = points + 5
                    print("Congrats! Sam saw a Duke player outside of Kenan when he was leaving morning film review. ")
                    print(f"You have {a} adventure points. Do you want to continue to Kenan Stadium? ")
                    print("1: Yes ")
                    print("2: No ")
                    points_choice: int = int(input("1 or 2? "))
                    if points_choice == 1:
                        print("Let's go to Kenan! ")
                        guess = 0
                        points_choice = 0
                        sam_choice = 0
                        kenan()
                    else: 
                        print(f"You missed your opportunity and the game starts without Ramses {ram}. ")
                        print(f"Thank you for playing, {player}! You finished with {points} adventure points. ")
                        guess = 0
                        points_choice = 0
                        sam_choice = 0
                    guess = 0
                if sam_choice == 2:
                    points = points - 1
                    print(f"You now know that Sam has never had a burger, but nothing about Ramses {ram}! ")
                    print("Let's ask him something else. ")
                    sam_choice = int(input(" Ask Sam Question 1 or 2: "))
        else:
            points = points - 1
            print("That was not Kevin's number. Guess again! ")
            guess = int(input("What is your guess? "))
    return points   


def duke() -> None:
    """Duke Events."""
    global ram
    global points
    points = points + 3
    print(f"We made it to Duke, look there is Ramses' {ram} footprints!") 
    print("Let's flip a coin to see if we should go on the field (heads) or the lockerroom (tails). ")
    coinflip = randint(1, 2)
    if coinflip == 1:
        print("Heads! Let's head to the field. ")
        field()
    else:
        print("Tails! Let's head to the lockerroom. ")
        lockerroom()


def field() -> None:
    """Duke football field events."""
    global ram
    global points 
    global player
    points = points + 5
    print("How lucky that the gates were unlocked! Let's look around. ")
    print(f"Look! It's Ramses {ram}")
    print(f"Thank you for your help! Now Ramses {ram} can get to the football game on time!")
    print(f"Thank you for playing, {player}! You finished with {points} adventure points. ")


def lockerroom() -> None:
    """Duke lockerroom events."""
    global ram
    global points 
    global player
    points = points + 5
    print("We made it to the lockerroom. Let's take a look around. ")
    print(f"It doesn't look like Ramses {ram} is here. Do you want to go to the field")
    print("1: Yes ")
    print("2: No ")
    field_choice: int = int(input("1 or 2? "))
    if field_choice == 1:
        points = points + 5
        print("Let's go! ")
        field()
    else:
        points = points - 1
        print(f"You missed your opportunity and the game starts without Ramses {ram}. ")
        print(f"Thank you for playing, {player}! You finished with {points} adventure points. ")
     

if __name__ == "__main__":
    main()