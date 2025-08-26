Proceso Segmentos_FOR
    Definir Seg_a, Seg_b, Seg_c, Seg_d, Seg_e, Seg_f, Seg_g, i, valor Como Entero
    
    Para i <- 1 Hasta 7 Con Paso 1 Hacer
        Escribir "Digite un valor entre 1 y 0 para el segmento ", i, ": "
        Segun i Hacer
            1: Leer Seg_a
            2: Leer Seg_b
            3: Leer Seg_c
            4: Leer Seg_d
            5: Leer Seg_e
            6: Leer Seg_f
            7: Leer Seg_g
        FinSegun
    FinPara
		
	Si (Seg_a=0 Y Seg_b=1 Y Seg_c=1 Y Seg_d=0 Y Seg_e=0 Y Seg_f=0 Y Seg_g=0) Entonces
        Escribir "Este valor es 1."
		Sino
			Si (Seg_a=1 Y Seg_b=1 Y Seg_c=0 Y Seg_d=1 Y Seg_e=1 Y Seg_f=0 Y Seg_g=1) Entonces
			Escribir "Este valor es 2."
			Sino
				Si (Seg_a=1 Y Seg_b=1 Y Seg_c=1 Y Seg_d=1 Y Seg_e=0 Y Seg_f=0 Y Seg_g=1) Entonces
				Escribir "Este valor es 3."
				Sino
					Si (Seg_a=0 Y Seg_b=1 Y Seg_c=1 Y Seg_d=0 Y Seg_e=0 Y Seg_f=1 Y Seg_g=1) Entonces
					Escribir "Este valor es 4."
					Sino		
						Si (Seg_a=1 Y Seg_b=0 Y Seg_c=1 Y Seg_d=1 Y Seg_e=0 Y Seg_f=1 Y Seg_g=1) Entonces
						Escribir "Este valor es 5."
						Sino			
							Si (Seg_a=1 Y Seg_b=0 Y Seg_c=1 Y Seg_d=1 Y Seg_e=1 Y Seg_f=1 Y Seg_g=1) Entonces
							Escribir "Este valor es 6."
							Sino
								Si (Seg_a=1 Y Seg_b=1 Y Seg_c=1 Y Seg_d=0 Y Seg_e=0 Y Seg_f=0 Y Seg_g=0) Entonces
								Escribir "Este valor es 7."
								Sino
									Si (Seg_a=1 Y Seg_b=1 Y Seg_c=1 Y Seg_d=1 Y Seg_e=1 Y Seg_f=1 Y Seg_g=1) Entonces
									Escribir "Este valor es 8."
									Sino
										Si (Seg_a=1 Y Seg_b=1 Y Seg_c=1 Y Seg_d=1 Y Seg_e=0 Y Seg_f=1 Y Seg_g=1) Entonces
										Escribir "Este valor es 9."
										Sino
											Si (Seg_a=1 Y Seg_b=1 Y Seg_c=1 Y Seg_d=1 Y Seg_e=1 Y Seg_f=1 Y Seg_g=0) Entonces
											Escribir "Este valor es 0."
											Sino
												Escribir "Este valor es un error."
											FinSi
										FinSi
									FinSi
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
		
FinProceso
