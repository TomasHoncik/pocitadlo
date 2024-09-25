slova = 0
radky = 1

with open("text.txt", "r") as file:
    soubor = file.read()

for radek in soubor:
    if radek == "\n":
        radky += 1

slova = len(soubor.split())
pocet_znaku = len(soubor)


print(f"V souboru je: {pocet_znaku} znaků")
print(f"V souboru je: {slova} slov")
print(f"V souboru je {radky} řádků")