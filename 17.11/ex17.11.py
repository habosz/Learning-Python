# #Zadanie 1.5
# x = int(input("wprowadź liczbę:"))
# result = x / 2 + 4
# assert result == 14


# # Zadanie 2.1
# imie = input("Wprowadź swoje imię: ")
# nazwisko = input("Wprowadź swoje nazwisko: ")
# print(f"Cześć {nazwisko} {imie}")


# # Zadanie 2.2 
# plik = input("Wprowadź nazwę pliku: ")
# print(plik.split('.')[1]) # funkcja split('.') rozdziela wartosci któ®e są oddzielone kropką; 
# # [1] mówi o tym wartość na jakiej pozycji pokazać -> przy inpucie abc.java "abc" jest na pozycji 0 a "java" na 1

# #alternatywa 
# filename = input('Wprowadź nazwę pliku: ')
# extension = filename.split('.')[1]
# print(f'Rozszerzenie pliku to: {extension}')

# # Zadanie 2.3
# dd = input('Podaj dzień: ')
# mm = input('Podaj miesiąc: ')
# yyyy = input('Podaj rok: ')
# print(f'{dd}/{mm}/{yyyy}')


# #Zadanie 2.4
# x = int(input("Podaj liczbę: "))
# y = int(input("Podaj druga liczbę: "))
# z = x + y 
# print(f'Suma {x} oraz {y} to {z}')

# #Zadanie 2.5
# x = int(input("Podaj liczbę całkowitą: "))
# y = int(input("Podaj liczbę całkowitą: "))
# a = float(input("Podaj liczbę po przecinku: "))
# b = float(input("Podaj liczbę po przecinku: "))
# g = x + a
# print(g)
# print(type(g))
# f = y - b 
# print(f)
# h = g + f
# print(f"Wynik to {h}")

# #alternatywa
# a = int(input("Wprowadź pierwszą liczbę całkowitą: "))
# b = int(input("Wprowadź drugą liczbę całkowitą: "))
# c = float(input("Wprowadź pierwszą liczbę zmiennoprzecinkową: "))
# d = float(input("Wprowadź drugą liczbę zmiennoprzecinkową: "))
 
# wynik1 = a+c
# wynik2 = d-b
 
# print(f"Wynik operacji 1: {wynik1}")
# print(type(wynik1))
# print(f"Wynik operacji 2: {wynik2}")
# print(type(wynik2))
 
# suma = wynik1 + wynik2
 
# print(f"Suma to: {suma}")
# print(type(suma))

# # Zadanie 2.6
# l = int(input("Podaj liczbę: "))
# st_pierw = int(input("Podaj stopień pierwiastka: "))
# print(f'Pierwiastek {st_pierw} stopnia z {l} to {l ** (1/st_pierw)}')

# #Jak wyświetlić tylko kilka miejsc po przecinku: ta dwójka przy f (.2f) mówi o tym ile chcemy widzieć miejsc po przecinku 
# print(f'{(0.1+0.2):.2f}')

# # Zadanie 2.7
# napis1 = input("Wprowadź napis: ")
# napis2 = input("Wprowadź napis drugi: ")
# print(f'{napis1} {napis dwa}')
# print(napis1, napis2, sep=", ")
# print(napis1, end=" ")
# print(napis2)

# # Zadanie 2.8
# a = float(input("Wprowadz 1 bok trójkąta: ")) # float bo ktoś moe podać libe po przecinku
# b = float(input("Wprowadz 2 bok trójkąta: "))
# c = float(input("Wprowadz 3 bok trójkąta: "))
# p = 1/2 * (a + b + c)
# P = (p*(p-a)*(p-b)*(p-c))**0.5
# print(f'Pole trójkąta to {P:.2f}') # chcemy tylko dwie liczby po przecinku dlatego :.2f

# # Zadanie 2.9
# km = float(input("Wprowadź liczbę kilometrów: "))
# mile = km * 0.621371192
# print(f'{km} kilometra to {mile:.2f} mili.')

# # Zadanie 2.10
# C = float(input("Podaj wartość temeratury w Celcjuszach: "))
# F = (C * 9/5) + 32
# print(f'{C:.1f} stopni Celcjusza to {F:.1f} stopni Farenhajta')



