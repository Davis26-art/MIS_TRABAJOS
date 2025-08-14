Algoritmo MayorDeDosNumeros
	Escribir 'Este algoritmo nos ayudara a saber cual es el mayor entre dos números:'
	Escribir 'Ingresa el primer número: '
	Leer Numero1
	Escribir 'Ingresa el segundo número; '
	Leer Numero2
	Si Numero1>Numero2 Entonces
		Escribir 'El número ', Numero1, ' es mayor que ', Numero2
	SiNo
		Si Numero2 > Numero1 Entonces
			Escribir 'El número ', Numero2, ' es mayor que ', Numero1
		SiNo
			Escribir 'Los números son iguales.'
		FinSi
	FinSi
FinAlgoritmo
