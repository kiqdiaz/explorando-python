#!/usr/bin/env python3
"""
Demostración de gestión de entornos virtuales
Comparación entre virtualenv tradicional y uv moderno
"""

import subprocess
import time
import os

def ejecutar_comando(comando, descripcion):
    """Ejecuta un comando y mide el tiempo"""
    print(f"\n🔄 {descripcion}")
    print(f"Comando: {comando}")
    
    inicio = time.time()
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        fin = time.time()
        
        print(f"⏱️  Tiempo: {fin - inicio:.2f} segundos")
        
        if resultado.returncode == 0:
            print("✅ Éxito")
            if resultado.stdout:
                print(f"Salida: {resultado.stdout[:200]}...")
        else:
            print("❌ Error")
            if resultado.stderr:
                print(f"Error: {resultado.stderr[:200]}...")
                
    except Exception as e:
        print(f"❌ Excepción: {e}")

def demo_virtualenv():
    """Demostración de virtualenv tradicional"""
    print("\n" + "="*50)
    print("DEMOSTRACIÓN: VIRTUALENV TRADICIONAL")
    print("="*50)
    
    # Crear entorno virtual
    ejecutar_comando(
        "python -m venv demo_venv",
        "Creando entorno virtual con virtualenv"
    )
    
    # Activar y instalar paquete (simulado)
    if os.name == 'nt':  # Windows
        activar = "demo_venv\\Scripts\\activate"
    else:  # macOS/Linux
        activar = "source demo_venv/bin/activate"
    
    print(f"\n📝 Para activar: {activar}")
    print("📝 Para instalar: pip install requests")
    print("📝 Para desactivar: deactivate")

def demo_uv():
    """Demostración de uv moderno"""
    print("\n" + "="*50)
    print("DEMOSTRACIÓN: UV MODERNO")
    print("="*50)
    
    # Verificar si uv está instalado
    ejecutar_comando("uv --version", "Verificando instalación de uv")
    
    # Crear proyecto con uv
    ejecutar_comando(
        "uv init demo-uv-project --no-readme",
        "Creando proyecto con uv"
    )
    
    # Mostrar estructura creada
    if os.path.exists("demo-uv-project"):
        print("\n📁 Estructura creada por uv:")
        ejecutar_comando("ls -la demo-uv-project", "Listando archivos del proyecto")

def comparacion_velocidad():
    """Compara velocidad entre pip y uv"""
    print("\n" + "="*50)
    print("COMPARACIÓN DE VELOCIDAD")
    print("="*50)
    
    print("📊 Instalación de paquetes:")
    print("   pip install requests: ~3-5 segundos")
    print("   uv add requests: ~0.5-1 segundo")
    print("\n📊 Resolución de dependencias:")
    print("   pip: Secuencial, puede tomar minutos")
    print("   uv: Paralelo, segundos")

def mejores_practicas():
    """Muestra mejores prácticas para entornos virtuales"""
    print("\n" + "="*50)
    print("MEJORES PRÁCTICAS")
    print("="*50)
    
    practicas = [
        "✅ Siempre usar entornos virtuales para proyectos",
        "✅ Nombrar entornos de forma descriptiva",
        "✅ Mantener requirements.txt actualizado",
        "✅ No versionar la carpeta del entorno virtual",
        "✅ Usar .gitignore para excluir entornos",
        "✅ Documentar versión de Python requerida",
        "✅ Considerar uv para proyectos nuevos",
        "✅ Usar virtualenv para compatibilidad legacy"
    ]
    
    for practica in practicas:
        print(f"  {practica}")

def limpiar_demos():
    """Limpia archivos de demostración creados"""
    print("\n🧹 Limpiando archivos de demostración...")
    
    # Limpiar virtualenv
    ejecutar_comando("rm -rf demo_venv", "Eliminando demo_venv")
    
    # Limpiar uv
    ejecutar_comando("rm -rf demo-uv-project", "Eliminando demo-uv-project")
    
    print("✅ Limpieza completada")

def main():
    """Función principal de demostración"""
    print("🐍 DEMOSTRACIÓN: GESTIÓN DE ENTORNOS VIRTUALES")
    print("=" * 60)
    
    try:
        demo_virtualenv()
        demo_uv()
        comparacion_velocidad()
        mejores_practicas()
        
        respuesta = input("\n¿Limpiar archivos de demostración? (s/n): ")
        if respuesta.lower() in ['s', 'sí', 'si', 'y', 'yes']:
            limpiar_demos()
            
    except KeyboardInterrupt:
        print("\n\n⏹️  Demostración interrumpida")
    except Exception as e:
        print(f"\n❌ Error en demostración: {e}")

if __name__ == "__main__":
    main()
