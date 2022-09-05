i = 0
while i < 6:
  print(f"{i}) hello")
  if i == 3:
    break
  i += 1 #i=i+1

fruits = ["orange", "ananas", "mangue"]
dicPerson = {"nom":"donald", "prenom":"ange"}

#fruits = tuple(fruits)

for x in fruits:
  if x == "ananas":
    continue
  for y in x:
    print(y)
  print("")
  

for cle, valeur in dicPerson.items():
  print(f"{cle} - {valeur}")

nom = "donald"

for letter in nom:
  print(letter)

for x in range(6):
  print(f"{x}) hello")