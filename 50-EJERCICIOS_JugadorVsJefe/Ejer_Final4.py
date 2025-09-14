#--------------------------------------------------
# EJERCICIO FINAL 4 -- Juego de Aventura de Texto
#--------------------------------------------------

print("🎮 Bienvenido a la Aventura de la Cueva Misteriosa")
print("Tu objetivo es salir con vida... o descubrir qué hay en su interior.")
print("Escribe el número de la opción que elijas.\n")

# Primer escenario
print("Te despiertas en la entrada de una cueva oscura.")
print("¿Qué quieres hacer?")
print("1) Entrar en la cueva")
print("2) Rodearla y seguir el sendero")
eleccion = input("> ").strip()

if eleccion == "1":
    # Camino dentro de la cueva
    print("\n💡 Entras en la cueva y escuchas un rugido lejano.")
    print("1) Seguir adelante")
    print("2) Salir corriendo")
    eleccion = input("> ").strip()

    if eleccion == "1":
        # Sigues adelante: segundo escenario
        print("\nTe encuentras con un cofre brillante en medio de la cueva.")
        print("1) Abrir el cofre")
        print("2) Ignorarlo y seguir avanzando")
        eleccion = input("> ").strip()

        if eleccion == "1":
            print("\n🎉 ¡Has encontrado un tesoro! Sales de la cueva rico y feliz.")
            print("🏆 Final bueno: Eres famoso en el pueblo por tu hallazgo.")
        else:
            print("\n⚠ Caminas más profundo en la cueva... y caes en un pozo sin fin.")
            print("💀 Final trágico: Nadie vuelve a verte jamás.")
    else:
        print("\n🏃‍♂️ Sales corriendo y llegas al pueblo sano y salvo.")
        print("😅 Final neutro: Sobreviviste, pero te quedas con la duda para siempre.")

elif eleccion == "2":
    # Camino del sendero
    print("\n🚶 Sigues el sendero y llegas a un puente colgante.")
    print("1) Cruzar el puente")
    print("2) Evitar el puente y seguir por el bosque")
    eleccion = input("> ").strip()

    if eleccion == "1":
        print("\n🌉 El puente cruje, pero logras cruzarlo.")
        print("Del otro lado encuentras un sabio que te da un mapa del tesoro.")
        print("🏆 Final secreto: Comienza una nueva aventura con el mapa en mano.")
    else:
        print("\n🌲 Te adentras en el bosque y encuentras una manada de lobos.")
        print("💀 Final malo: No logras escapar y el bosque se queda en silencio.")

else:
    print("\n😐 No hiciste nada y te quedaste dormido.")
    print("⏳ Final aburrido: Nada cambió en tu vida.")

print("\n--- FIN DEL JUEGO ---")
