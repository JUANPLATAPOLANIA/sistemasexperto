def sistema_experto():
    print("="*60)
    print("        SISTEMA EXPERTO: DIAGNÓSTICO DE FALLAS EN AUTOMÓVILES")
    print("="*60)
    print("\nPor favor responde con 'si' o 'no' según corresponda.\n")

    arranca = input("¿El auto arranca? (si/no): ").strip().lower()

    if arranca == "no":
        luces = input("¿Las luces del tablero encienden? (si/no): ").strip().lower()
        if luces == "no":
            print("\nDiagnóstico: Posible causa → Batería descargada.")
        elif luces == "si":
            print("\nDiagnóstico: Posible causa → Fallo en el motor de arranque.")
        else:
            print("\n[Error] Respuesta no válida. Intenta de nuevo.")
    elif arranca == "si":
        apaga = input("¿El auto se apaga al acelerar? (si/no): ").strip().lower()
        if apaga == "si":
            print("\nDiagnóstico: Posible causa → Problema en el suministro de combustible.")
        else:
            humo_negro = input("¿Sale humo negro por el escape? (si/no): ").strip().lower()
            if humo_negro == "si":
                print("\nDiagnóstico: Posible causa → Mezcla rica de combustible.")
            else:
                humo_blanco = input("¿Sale humo blanco constante por el escape? (si/no): ").strip().lower()
                if humo_blanco == "si":
                    print("\nDiagnóstico: Posible causa → Falla en la junta de culata.")
                else:
                    print("\nInformación: No se encontró una falla en la base de conocimiento.")
    else:
        print("\n[Error] Respuesta no válida. Intenta de nuevo.")

    print("\n" + "="*60)
    print("   Gracias por usar el Sistema Experto de Diagnóstico Automotriz")
    print("="*60)


# Ejecutar el sistema
if __name__ == "__main__":
    sistema_experto()




