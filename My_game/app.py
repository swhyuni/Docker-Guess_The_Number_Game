import pandas as pd 
import numpy as np

def number_guessing_game():
    print('''
    Selamat datang dipermainan tebak angka
    Silakan tebak angka 0-9 sebenyak 3 kali      
    ''')

    computer_number = np.random.randint(0,9,3)
    user_number = []
    for loop in range(3):
        number = int(input(f'Masukan angka ke {loop+1}: '))
        user_number.append(number)

    result = list(user_number == computer_number)
    output = pd.DataFrame([user_number, computer_number, result], index = ['Angka Anda', 'Angka Komputer', 'Hasil']).T
    print(output)

if __name__ == '__main__':
    number_guessing_game()