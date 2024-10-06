tekst = 'Litwo, Ojczyzno moja! ty jesteś jak zdrowie;Ile cię trzeba cenić, ten tylko się dowie,Kto cię stracił. Dziś piękność twą w całej ozdobieWidzę i opisuję, bo tęsknię po tobie.'

male_litery = tekst.lower()

samogloski = 'aeiouyąęó'

ilosc = sum(1 for liter in male_litery if liter in samogloski)
print(ilosc)
