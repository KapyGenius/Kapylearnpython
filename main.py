person = {
  "nom": "donald",
  "prenom": "steve",
  "age": 14,
  "note": [12, 23, 14]
}

x = person.keys()
#person.values()
#person.items()
print(x)

person["nom"] = "ange"
#person.update({"nom":"ange"})
person["sexe"] = "m"
person.pop("note")
#person.popitem()

#person.clear()

person2 = person.copy()
print(x)

print(person2)

mySets = {"donald", "ange", "fabiolle"}

mySets.add("dominique")

print(mySets)