Algoritmo SegmentosDisplay
	
    Definir Seg_a, Seg_b, Seg_c, Seg_d, Seg_e, Seg_f, Seg_g Como Entero
	
    Escribir "Digite un valor entre 1 y 0 para a: "
    Leer Seg_a
    Escribir "Digite un valor entre 1 y 0 para b: "
    Leer Seg_b
    Escribir "Digite un valor entre 1 y 0 para c: "
    Leer Seg_c
    Escribir "Digite un valor entre 1 y 0 para d: "
    Leer Seg_d
    Escribir "Digite un valor entre 1 y 0 para e: "
    Leer Seg_e
    Escribir "Digite un valor entre 1 y 0 para f: "
    Leer Seg_f
    Escribir "Digite un valor entre 1 y 0 para g: "
    Leer Seg_g
	
    Si Seg_a = 0 Y Seg_b = 1 Y Seg_c = 1 Y Seg_d = 0 Y Seg_e = 0 Y Seg_f = 0 Y Seg_g = 0 Entonces
        Escribir "Este valor es 1."
    Sino
        Si Seg_a = 1 Y Seg_b = 1 Y Seg_c = 0 Y Seg_d = 1 Y Seg_e = 1 Y Seg_f = 0 Y Seg_g = 1 Entonces
            Escribir "Este valor es 2."
        Sino
            Si Seg_a = 1 Y Seg_b = 1 Y Seg_c = 1 Y Seg_d = 1 Y Seg_e = 0 Y Seg_f = 0 Y Seg_g = 1 Entonces
                Escribir "Este valor es 3."
            Sino
                Si Seg_a = 0 Y Seg_b = 1 Y Seg_c = 1 Y Seg_d = 0 Y Seg_e = 0 Y Seg_f = 1 Y Seg_g = 1 Entonces
                    Escribir "Este valor es 4."
                Sino
                    Si Seg_a = 1 Y Seg_b = 0 Y Seg_c = 1 Y Seg_d = 1 Y Seg_e = 0 Y Seg_f = 1 Y Seg_g = 1 Entonces
                        Escribir "Este valor es 5."
                    Sino
                        Si Seg_a = 1 Y Seg_b = 0 Y Seg_c = 1 Y Seg_d = 1 Y Seg_e = 1 Y Seg_f = 1 Y Seg_g = 1 Entonces
                            Escribir "Este valor es 6."
                        Sino
                            Si Seg_a = 1 Y Seg_b = 1 Y Seg_c = 1 Y Seg_d = 0 Y Seg_e = 0 Y Seg_f = 0 Y Seg_g = 0 Entonces
                                Escribir "Este valor es 7."
                            Sino
                                Si Seg_a = 1 Y Seg_b = 1 Y Seg_c = 1 Y Seg_d = 1 Y Seg_e = 1 Y Seg_f = 1 Y Seg_g = 1 Entonces
                                    Escribir "Este valor es 8."
                                Sino
                                    Si Seg_a = 1 Y Seg_b = 1 Y Seg_c = 1 Y Seg_d = 1 Y Seg_e = 0 Y Seg_f = 1 Y Seg_g = 1 Entonces
                                        Escribir "Este valor es 9."
                                    Sino
                                        Si Seg_a = 1 Y Seg_b = 1 Y Seg_c = 1 Y Seg_d = 1 Y Seg_e = 1 Y Seg_f = 1 Y Seg_g = 0 Entonces
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
	
FinAlgoritmo
