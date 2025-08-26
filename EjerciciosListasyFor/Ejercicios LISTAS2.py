Lista = ['David', 'Steban', 'Sebastian', 'Maicol', 'Mario', 'Erwin', 'Julian', 'Juan']
print(Lista)

for i in Lista:
    print(f"LOS ELEMENTOS DE LA LISTA SON: {i}")

for no, listas in enumerate(Lista):
   print(no, "¡", listas)


for var in (Lista[2:6]):
    print(var)
    print(Lista[var])
print(len(Lista[4]))

var1 = "David" in Lista
print(var1)


var2 = "aeiouaeiouaaa"

var3 = var2.count("a")
print(var3)

var4 = Lista.index("Maicol")
print(var4)
