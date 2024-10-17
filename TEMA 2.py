
articol = """
Într-o zi frumoasă de primăvară, oamenii se plimbau prin parc. 
Soarele strălucea, iar florile începeau să înflorească! 
Era o vreme perfectă pentru a ieși la aer liber.
"""


lungime = len(articol)
if lungime % 2 == 0:
    parte1 = articol[:lungime // 2]
    parte2 = articol[lungime // 2:]
else:
    parte1 = articol[:(lungime // 2) + 1]
    parte2 = articol[(lungime // 2) + 1:]


parte1 = parte1.strip().upper()


parte2 = parte2[::-1].strip()
parte2 = parte2.capitalize()
parte2 = ''.join(char for char in parte2 if char.isalnum() or char.isspace())


rezultat = parte1 + ' ' + parte2


print(rezultat)