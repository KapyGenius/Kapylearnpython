class Person:
  def __init__(self, name, age, poids):
    self.name = name
    self.age = age
    self.poids = poids

  def parler(self, texte):
    print(f"je parle le texte: {texte}")

  def presenter(self):
    print(f"je m'appele {self.name}, j'ai {self.age} ans et je pese {self.poids} kilos")

  def monage(self):
    return self.age
  

donald = Person("donald", 15, 60)
ange = Person("ange", 14, 55)

donald.age = 20

#del donald.age

#del donald

print(donald.name)
print(ange.name)

donald.parler("bonjour")

donald.presenter()
ange.presenter()

print(donald.monage())

