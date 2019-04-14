from render import Render
import examples as ex

#Menu
print("Elija la imagen a renderizar:")

while True:
    print("1. Punto blanco random en la pantalla.")
    print("2. Punto en cada esquina de la imagen.")
    print("3. Lineas blancas que forman un cuadrado.")
    print("4. Una diagonal.")
    print("5. Estatica.")
    print("6. Imagen con puntos de color random.")
    print("7. Cielo con estrellas.")
    print("8. Imagen de 160x192 del juego Breakout de Atari.")
    print("9. Salir.")

    try:
        choice = int(input())
        if choice == 1:
            ex.random_point()
        elif choice == 2:
            ex.white_point_each_corner()
        elif choice == 3:
            ex.square()
        elif choice == 4:
            ex.diagonal()
        elif choice == 5:
            ex.static()
        elif choice == 6:
            ex.random_colors()
        elif choice == 7:
            ex.stars()
        elif choice == 8:
            ex.atari()
        elif choice == 9:
            break
        else:
            print("Elija una opcion correcta.")
    except:
        print("Elija una opcion correcta.")


# ex.random_point()
# ex.white_point_each_corner()
# ex.square()
# ex.diagonal()
# ex.static()
# ex.random_colors()
# ex.stars()
# ex.atari()
