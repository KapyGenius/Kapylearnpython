print("hello")

def myFunction(age, nom, sexe = "m"):
  print(f"hello {nom} from function {age} et ton sexe {sexe}")

def myFunc2(foods):
  for x in foods:
    print(x)

myFunction(nom = "donald", age = 16, sexe="f")
myFunction(14, "ange", "f")

#myFunc2(["banane", "Ero", "Orange"])

# f(n) = f(n-1) + n, f(0)=1

def f(n):
  if n == 0:
    return 1
  else:
    return f(n-1) + n

resultat = f(3)

print(resultat)

carre = lambda x, y : x**y

print(carre(5, 3))


























#list comprehension
myList = [1, 3, 4, 5, 6]

#myListCarre = []
#for x in myList:
#  if x % 2 == 1:
#    myListCarre.append(x**2)

myListCarre = [ x**2 for x in myList if x % 2 == 1 ]

#print(myListCarre)
