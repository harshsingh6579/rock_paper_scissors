import random

def play():
    user_choice = input('Make a choice: "r" for rock, "p" for paper, "s" for scissor ')
    cpu_choice = random.choice(["r", "p", "s"])
    print(f"CPU chose: {cpu_choice}")

    if user_choice == cpu_choice:
        return "It's a Tie"
    
    if user_win(user_choice, cpu_choice):
        return "You won!"
    
    return "You lost..."
    
def user_win(player, cpu):
    if (player == "r" and cpu == "s") or (player == "p" and cpu == "r") or (player == "s" and cpu == "p"):
        return True

print(play())