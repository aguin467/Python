num_guesses = 3
user_guesses = []

guess = 0

while guess < num_guesses:
    num = int(input())
    user_guesses.append(num)
    guess += 1

print(user_guesses)


