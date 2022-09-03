listNote = [15, 17, 20, 12, 16, 13, 20]
listNom = ["donald", "ange", "michael"]
listNom2 = ["roger", "marius"]
#print(listNote[:4])
#if "donalda" in listNom:
#  print("il ya donalda dans la liste")

listNom[1:3] = ["angela", "Aichaela"]

listNom.insert(1, "fabiol")

listNom.append("nahomie")

listNom.extend(listNom2)

#listNom.remove("donald")

listNom.pop(1)

listNom.insert(2, "dominique")

#listNom.clear()

listNom.sort()

listNomTotal = listNom + listNom2

print(listNomTotal.count("ange"))


tupleNom = ("donald", "ange")

tupleNom = list(tupleNom)
tupleNom[0] = "donaldo"
tupleNom = tuple(tupleNom)

print(tupleNom[0])