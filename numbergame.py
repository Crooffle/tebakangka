import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'tebak nomor dari 1 sampai {x}: '))
        if guess < random_number:
            print('kurang gede angkalu bang')
        elif guess > random_number:
            print('kegedean angkalu bang')
    print(f'anjay selamat bang kamu berhasil nebak {random_number}')


guess(10)
