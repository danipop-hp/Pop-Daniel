import random

# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

# Afișarea șablonului inițial
print("Ghiceste cuvântul:", " ".join(progres))

# Bucla principală de joc
while "_" in progres and incercari_ramase > 0:
    # Cererea unei litere
    guess = input("Introdu o literă: ").lower()

    # Verificarea validității
    if len(guess) != 1 or not guess.isalpha():
        print("Te rog să introduci o singură literă validă.")
        continue

    if guess in litere_incercate:
        print("Ai încercat deja această literă. Alege alta.")
        continue

    litere_incercate.append(guess)

    # Verificarea literei în cuvânt
    if guess in cuvant_de_ghicit:
        for index, litera in enumerate(cuvant_de_ghicit):
            if litera == guess:
                progres[index] = guess
        print("Bine! Litera se află în cuvânt.")
    else:
        incercari_ramase -= 1
        print("Greșit! Litera nu se află în cuvânt.")
        print("Încercări rămase:", incercari_ramase)

    # Afișarea progresului și încercărilor rămase
    print("Progres:", " ".join(progres))

# Încheierea jocului
if "_" not in progres:
    print("Felicitări! Ai ghicit cuvântul:", cuvant_de_ghicit)
else:
    print("Ai pierdut! Cuvântul era:", cuvant_de_ghicit)

