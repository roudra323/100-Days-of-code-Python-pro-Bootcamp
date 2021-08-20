print('Welcome to The Treasure finder game')

step1 = input("Which side you wanna go? left or right? ").lower()
if step1 == 'left':
    print('Lost')
else:
    step2 = input("stay in home or leave").lower()
    if step2 == 'leave':
        print('lost')
    else:
        step3 = input("boat or walk or cycle?").lower()
        if step3 == ('walk' or 'cycle'):
            print('lost')
        else:
            print('Treasure Found\nCongratulations')
