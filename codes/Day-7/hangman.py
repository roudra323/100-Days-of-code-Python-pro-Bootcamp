from random import randint
word_list = ['ardvark', 'baboon', 'camel']
ran_generator = randint(0, len(word_list)-1)
chosen_word = word_list[ran_generator]

l = ['_']*len(chosen_word)
lost = 0
for jk in range(len(chosen_word) + 5):
    guess_word = input()

    if guess_word not in chosen_word:
        print("Wrong Guess")
        lost += 1

    if lost == 6:
        print('You have lost')
        break

    elif guess_word in chosen_word:

        for i in range(len(chosen_word)):

            if guess_word == chosen_word[i]:
                l[i] = guess_word
                chosen_word.replace(chosen_word[i], '')
                print(*l)

    if not '_' in l:
        print("You Won")
        break


# print(*l)
