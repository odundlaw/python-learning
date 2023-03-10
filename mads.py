from random import randint

class Guess():
    def __init__(self):
        self.attempts_list = [];
        self.attempt = 0;

    def show_score(self):
        if not self.attempts_list:
            print("There's presently not High Score it\'s yours for the taking!")
        else:
            print(f"The current high score is {min(self.attempts_list)} attempts")

    def start_game(self):
        random_number = randint(1, 10);
        player_name = input("What's your name player: ");
        will_play = input("Do you want to play? (Enter Yes/ No): ");

        if will_play.lower() != "yes":
            print("Thank you i wont proceed with the game")
            exit();
        
        self.show_score();

        while will_play.lower() == "yes":
            try:
                player_guess = int(input(f"{player_name} pick a random number between 1 to 10: "));
                if player_guess < 1 or player_guess > 10:
                    raise ValueError("Please select a number between 1 and 10");
                self.attempt += 1;
                self.attempts_list.append(self.attempt);

                if player_guess == random_number:
                    print("Nice job you got it");
                    print(f"it looks like it took you {self.attempt} attempts");

                    will_play = input("Do you want to play again? (Enter Yes/No: ");
                    if will_play.lower() != "yes":
                        print("I will not continue thank you!")
                        break;
                    else:
                        self.attempt = 0;
                        random_number = randint(1, 10);
                        self.show_score();
                        continue;
                else:
                    if player_guess < random_number:
                        print("It's Higher");
                    elif player_guess > random_number:
                        print("It's Lower")
            
            except ValueError as err:
                print("Oh no, that is not a valid value!");
                print(err);
            




    
guess = Guess();

print(guess.start_game());