import art
import random
import game_data

#print art
print(art.logo)
current_score = 0
A = random.choice(game_data.data)
while current_score < 10:
    B = random.choice(game_data.data)  # Pick another random choice
    while A == B:  # Ensure A and B are different
        B = random.choice(game_data.data)
    #ask for user input
    print(f"Compare A: {A['name']}, {A['description']} from {A['country']}")
    print(art.vs)
    print(f"Against B: {B['name']}, {B['description']} from {B['country']}")
    choice=input("Who has the most followers? . Type 'A' or 'B'").strip().lower()

    if (A['follower_count']>B['follower_count'] and choice=='a') or (B['follower_count']>A['follower_count'] and choice=='b'):
        current_score+=1
        print(f"Yes, that's right! Current score is {current_score}.")

    elif (B['follower_count']>A['follower_count'] and choice=='a') or (B['follower_count']<A['follower_count'] and choice=='b'):
        final_Score=current_score
        print(f"Sorry, That's wrong! final score is {final_Score}")
        break

    else :
        final_Score = current_score
        print(f"Sorry, That's wrong! final score is {final_Score}")
        break

