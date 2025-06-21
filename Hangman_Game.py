import random

words = ['apple', 'banana', 'grape', 'orange', 'peach']
word = random.choice(words)
guessed = []
attempts = 6

while attempts > 0:
    display = ''
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += '_'
    print('Word:', display)

    if display == word:
        print("🎉 You guessed the word!")
        break

    guess = input("Guess a letter: ").lower()
    if guess in guessed:
        print("Already guessed!")
    elif guess in word:
        guessed.append(guess)
        print("Correct!")
    else:
        guessed.append(guess)
        attempts -= 1
        print(f"Wrong! {attempts} attempts left.")

if attempts == 0:
    print(f"😢 You lost! The word was '{word}'.")
