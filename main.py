#Typy danych 
# int - typ numeryczny, liczby całkowite
# float- typ numeryczny, liczby zmiennoprzecinkowe 
# bool - typ logiczny, prawda/fałsz
# str - tym znakowy, napisy 

# a = 0
# print((float(a)))
# print(bool(a))

# type(obj) - zwraca typ obiektu przekazanego jako argument
# insistance(obj, typ) - sprawdza czy dany obiekt jest 'instancja' konkretnego typu lub klasy

# print(isinstance('hello', (int, str))) # Czy hello to typ int lub str? output: True - bo jest to str

# None to specjalny obiekt w Pythonie, który reorezentuje brak wartości lub "nic"
# Jest uzywany, gdy zmienna lub funkcja nie ma przypisanej konkretnej wartości
# Typ obiekty None to NoneType

# a = None 
# print(type(a))

# if a is int:
#     print('Zmienna a jest int')
# else:
#     print('Zmienna a jest None')

# print(range(6))

# x = bool(5)
# print(x)
# print(str(x))

# x = 5
# x+= 3 
# print(x)

# x = 'tak'
# y = 'tak'

# if x in y:
#     print('tak')
# else:
#     print('nie')


imie = input('Podaj swoje imie: ')
nazwisko = input('Podaj swoje nazwisko: ')
print(f'Witaj {imie} {nazwisko}!')