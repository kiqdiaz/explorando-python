#!/usr/bin/env python3
"""
Caso 3: Hello World Avanzado
Introducción a clases, manejo de excepciones y logging
"""

import logging
from datetime import datetime

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SaludadorAvanzado:
    """Clase para manejar saludos de manera avanzada"""
    
    def __init__(self):
        self.contador_saludos = 0
        self.historial = []
        logging.info("SaludadorAvanzado inicializado")
    
    def saludar(self, nombre, idioma="español"):
        """Genera saludo en diferentes idiomas con manejo de errores"""
        try:
            saludos = {
                "español": f"¡Hola, {nombre}!",
                "inglés": f"Hello, {nombre}!",
                "francés": f"Bonjour, {nombre}!",
                "alemán": f"Hallo, {nombre}!",
                "italiano": f"Ciao, {nombre}!"
            }
            
            if idioma not in saludos:
                raise ValueError(f"Idioma '{idioma}' no soportado")
            
            mensaje = saludos[idioma]
            self.contador_saludos += 1
            
            # Registrar en historial
            registro = {
                "timestamp": datetime.now(),
                "nombre": nombre,
                "idioma": idioma,
                "mensaje": mensaje
            }
            self.historial.append(registro)
            
            logging.info(f"Saludo generado: {mensaje}")
            return mensaje
            
        except ValueError as e:
            logging.error(f"Error en saludo: {e}")
            return f"Error: {e}"
        except Exception as e:
            logging.error(f"Error inesperado: {e}")
            return "Error inesperado al generar saludo"
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas de uso"""
        print(f"\n=== Estadísticas ===")
        print(f"Total de saludos: {self.contador_saludos}")
        print(f"Idiomas usados: {len(set(r['idioma'] for r in self.historial))}")
        
        if self.historial:
            print(f"Último saludo: {self.historial[-1]['timestamp']}")

def main():
    """Función principal con manejo completo"""
    try:
        print("=== Hello World Avanzado ===")
        saludador = SaludadorAvanzado()
        
        # Solicitar datos del usuario
        nombre = input("Ingresa tu nombre: ").strip()
        if not nombre:
            nombre = "Usuario"
        
        print("\nIdiomas disponibles: español, inglés, francés, alemán, italiano")
        idioma = input("Elige un idioma (por defecto español): ").strip().lower()
        if not idioma:
            idioma = "español"
        
        # Generar saludo
        resultado = saludador.saludar(nombre, idioma)
        print(f"\n{resultado}")
        
        # Saludos adicionales de demostración
        print("\n=== Demostración de múltiples saludos ===")
        for lang in ["inglés", "francés", "alemán"]:
            mensaje = saludador.saludar(nombre, lang)
            print(mensaje)
        
        # Mostrar estadísticas
        saludador.mostrar_estadisticas()
        
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario")
        logging.info("Programa terminado por el usuario")
    except Exception as e:
        print(f"Error crítico: {e}")
        logging.critical(f"Error crítico en main: {e}")

if __name__ == "__main__":
    main()
