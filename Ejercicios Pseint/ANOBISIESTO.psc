Algoritmo ANOBISIESTO
	Escribir 'Este algoritmo nos ayudara a saber si un año es bisiesto.'
	Escribir 'Ingresa un año: '
	Leer ValorAño
	Si (ValorAño MOD 4 = 0 y ValorAño MOD 100 <> 0) o (ValorAño MOD 400 = 0)  Entonces
		Escribir 'El año ', ValorAño, ' si es bisiesto.'
	SiNo
		Escribir 'El año ', ValorAño, ' no es bisiesto.'
	FinSi
FinAlgoritmo
