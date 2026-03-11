import random
from GameData import data
from art import logo, vs
game_not_over = True
print(logo)

score = 0
# Pull 2 different instagram accounts from data
result = random.sample(data, 2)
first = result[0]
second = result[1]
name1, follower_count1, description1, country1 = first["name"], first["follower_count"], first["description"], first["country"]
while game_not_over:
    name2, follower_count2, description2, country2 = second["name"], second["follower_count"], second["description"], second["country"]
    print(f"Compare A: {name1}, a {description1}, from {country1}.")
    print(vs)
    guess = input(f"Against B: {name2}, a {description2}, from {country2}. Who has more followers? Type 'A' or 'B': ").lower()
    if guess == "a" and follower_count1 > follower_count2:
        score += 1
        print(f"Correct! Your score is {score}")
        second = random.choice(data)
        while second == first:
            second = random.choice(data)
    elif guess == "b" and follower_count1 < follower_count2:
        score += 1
        print(f"Correct! Your score is {score}")
        first = second
        name1 = first["name"]
        follower_count1 = first["follower_count"]
        description1 = first["description"]
        country1 = first["country"]
        second = random.choice(data)
        while second == first:
            second = random.choice(data)
    else:
        print(f"Wrong! Your score was {score}.")
        game_not_over = False