Algoritmo DescuentoCompra
	Escribir "Este algoritmo nos va a ayudar a aplicar un descuento del 10% si la compra supera los 100$."
	Escribir "Ingrese el valor de la compra:"
    Leer compra
	
    Si compra > 100 Entonces
        descuento <- compra * 0.10
        total <- compra - descuento
    SiNo
        descuento <- 0
        total <- compra
    Fin Si
	
    Escribir "Descuento aplicado: $", descuento
    Escribir "Total a pagar: $", total
FinAlgoritmo
