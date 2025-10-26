#!/usr/bin/env python3
"""
Caso 2: Hello World Intermedio
Introducción a funciones y entrada del usuario
"""

def saludar(nombre="Mundo"):
    """Función que genera un saludo personalizado"""
    return f"¡Hola, {nombre}!"

def main():
    """Función principal del programa"""
    print("=== Programa Hello World Intermedio ===")
    
    # Entrada del usuario
    nombre_usuario = input("¿Cuál es tu nombre? ")
    
    # Usar la función de saludo
    mensaje = saludar(nombre_usuario)
    print(mensaje)
    
    # Saludo múltiple
    idiomas = {
        "español": "¡Hola!",
        "inglés": "Hello!",
        "francés": "Bonjour!"
    }
    
    print("\nSaludos en diferentes idiomas:")
    for idioma, saludo in idiomas.items():
        print(f"{idioma.capitalize()}: {saludo} {nombre_usuario}")

if __name__ == "__main__":
    main()
