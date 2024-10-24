
meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ['guias'] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []


for i in range(len(studenti)):
    if not studenti or not comenzi or not tavi:
        break

    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    tavi.pop()
    istoric_comenzi.append((student, comanda))

    print(f"{student} a comandat {comanda}.")


s_au_comandat = {"guias": 0, "ceafa": 0, "papanasi": 0}
for _, comanda in istoric_comenzi:
    s_au_comandat[comanda] += 1


print(f"S-au comandat {s_au_comandat['guias']} guias, {s_au_comandat['ceafa']} ceafa, {s_au_comandat['papanasi']} papanasi.")


tavi_ramase = len(tavi)
print(f"Mai sunt {tavi_ramase} tavi.")


stocuri = {
    "papanasi": meniu.count("papanasi"),
    "ceafa": meniu.count("ceafa"),
    "guias": meniu.count("guias")
}

print(f"Mai este ceafa: {stocuri['ceafa'] > 0}.")
print(f"Mai sunt papanasi: {stocuri['papanasi'] > 0}.")
print(f"Mai sunt guias: {stocuri['guias'] > 0}.")


total_incasat = 0
for  comanda in istoric_comenzi:
    for produs in preturi:
        if comanda == produs[0]:
            total_incasat += produs[1]

print(f"Cantina a încasat: {total_incasat} lei.")


produse_accessibile = [produs for produs in preturi if produs[1] <= 7]
print(f"Produse care costă cel mult 7 lei: {produse_accessibile}.")


