#!/usr/bin/env python3
"""
Configuración y demostración de VS Code para Python
Este archivo muestra las características principales de VS Code
"""

import os
import sys

def mostrar_info_entorno():
    """Muestra información del entorno de desarrollo"""
    print("=== Información del Entorno ===")
    print(f"Python: {sys.version}")
    print(f"Directorio actual: {os.getcwd()}")
    print(f"Path de Python: {sys.executable}")
    
    # Verificar si estamos en un entorno virtual
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Entorno virtual activo")
    else:
        print("⚠️  No hay entorno virtual activo")

def demo_debugging():
    """Función para demostrar debugging en VS Code"""
    numeros = [1, 2, 3, 4, 5]
    
    # Punto de breakpoint sugerido aquí
    resultado = 0
    for num in numeros:
        resultado += num * 2  # Breakpoint aquí para ver valores
    
    print(f"Resultado del cálculo: {resultado}")
    return resultado

def demo_extensiones():
    """Demuestra funcionalidades que requieren extensiones de VS Code"""
    print("\n=== Funcionalidades de Extensiones ===")
    
    # Pylance: Type hints
    def sumar(a: int, b: int) -> int:
        return a + b
    
    # GitLens: Información de Git (si está disponible)
    try:
        import subprocess
        git_info = subprocess.run(['git', 'status', '--porcelain'], 
                                capture_output=True, text=True)
        if git_info.returncode == 0:
            print("✅ Repositorio Git detectado")
        else:
            print("ℹ️  No es un repositorio Git")
    except:
        print("ℹ️  Git no disponible")
    
    # Demostrar type hints
    resultado = sumar(5, 3)
    print(f"Suma con type hints: {resultado}")

if __name__ == "__main__":
    mostrar_info_entorno()
    demo_debugging()
    demo_extensiones()
