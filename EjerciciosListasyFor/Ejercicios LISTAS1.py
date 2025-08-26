Lista = ['David', 'Steban', 'Sebastian', 'Maicol', 'Mario', 'Erwin', 'Julian', 'Juan']
print(Lista)
Lista2 = Lista[2 : 5]

print(Lista[2:6])
print(Lista[2],Lista[6])
print(Lista2)
print(Lista2[1])

Lista2.append("Miguel")
Lista2.insert( 3, "Pedro")
Lista2.extend(Lista)

print(Lista2)

Lista.remove('David')
print(Lista)
Lista.pop(3)
print(Lista)
Lista.clear()
print(Lista)


 
