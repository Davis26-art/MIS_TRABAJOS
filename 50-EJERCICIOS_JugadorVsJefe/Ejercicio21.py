#----------------------------------------------------
# EJERCICIO 21 -- Funciones con frutas
#----------------------------------------------------

# Mi primera función con frutas
def describir_fruta(nombre, color, sabor):  # def define la función, tiene 3 parámetros
    """Esta función describe una fruta con su color y sabor"""
    descripcion = f"La {nombre} es de color {color} y tiene un sabor {sabor}."
    return descripcion  # return devuelve el resultado

# Usar la función (llamarla)
fruta1 = describir_fruta("manzana", "rojo", "dulce")
fruta2 = describir_fruta("limón", "verde", "ácido")
fruta3 = describir_fruta("uva", "morado", "jugoso")

print("Usando mi función de descripción de frutas:")
print(fruta1)
print(fruta2)
print(fruta3)

# También podemos usarla directamente
print("\nUsando directamente:")
print(describir_fruta("naranja", "naranja", "cítrico"))
print(describir_fruta("fresa", "rojo", "dulce"))
