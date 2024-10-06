print('Kalkulator BMI')

masa = int(input('Podaj swoją wagę: '))
wzrost = int(input('Podaj swój wzrost: '))

bmi = masa/wzrost**2

print('Twoje BMI wynosi: ', bmi)

if bmi > 18 and bmi < 25:
    print('Jestes w normie')
elif bmi < 18:
    print('Niedowaga')
elif bmi > 25:
    print('Nadwaga')