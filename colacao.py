# Teaching PC how to make ColaCao

print("[!]Si [!]No \n") # Aceptable answer

inicio = input("¿Quieres que te prepare un colacao? \n") # Initial question

if inicio == "Si":  # Conditions based on answer
    print("\n[!] Entrando en la cocina...\n")
    leche = input("¿Hay leche en la nevera? \n")

    if leche == "si":
        print("\n[!] Añadiendo leche en el vaso...\n")
        colacao = input("¿Hay colacao en la lacena? \n")
        
        if colacao == "si":
            print("\n[!] Añadiendo colacao a la leche \n")
            cucharadas = float(input("¿Cuantas cucharadas quieres? \n"))
            
            if cucharadas > 0:
                print("\n[!] Añadiendo {} cucharadas \n".format(cucharadas))
                print("[^_^] Colacao listo, que lo disfrutes.")

        else:
            print("[*] No hay colacao, por lo tanto te bebes solo la leche.\n")

    else:
        print("[*] No hay leche, por tanto te quedas sin colacao. \n")
        
else:
    print("[-] Otra vez será.")