password = input("Crea tu contraseña: ")

intentos = 3

while intentos > 0:
    password_usuario = input("Introduce la contraseña: (Tienes " + str(intentos) + " intentos) ")
    if password_usuario == password:
        print("La contraseña introducida es correcta.")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print("La contraseña introducida es incorrecta, vuelve a intentarlo.")
        else:
            print("Has agotado todos los intentos.")
