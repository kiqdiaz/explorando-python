# Lab: Hello World - Configuración del Entorno de Desarrollo Python

## Objetivos del Laboratorio
- Configurar VS Code como IDE principal para Python
- Dominar la gestión de entornos virtuales con virtualenv y uv
- Establecer conexiones remotas por SSH
- Implementar y ejecutar casos Hello World
- Crear un flujo de trabajo eficiente para futuros proyectos

## Herramientas Requeridas
- **VS Code** - Editor principal
- **Python 3.8+** - Lenguaje de programación
- **virtualenv** - Gestión tradicional de entornos
- **uv** - Framework moderno de gestión de proyectos Python
- **Git** - Control de versiones
- **SSH** - Conexión remota (opcional)

## Parte 1: Configuración de VS Code

### 1.1 Instalación de Extensiones Esenciales
```bash
# Extensiones recomendadas para instalar:
# - Python (Microsoft)
# - Python Debugger
# - Pylance
# - GitLens
# - Remote - SSH (para conexiones remotas)
```

### 1.2 Estructura del Workspace
- **Explorer**: Navegación de archivos y carpetas
- **Search**: Búsqueda en todo el proyecto
- **Source Control**: Integración con Git
- **Run and Debug**: Ejecución y depuración
- **Extensions**: Gestión de extensiones

### 1.3 Configuración de SSH Remoto
```json
// settings.json para conexión remota
{
    "remote.SSH.remotePlatform": {
        "hostname": "linux"
    }
}
```
TODO: Toda la parte 1 es hacer un esquema de instalar vscode, y se alcanzan videos actualizados de youtube de canales que ya explican eso.

## Parte 2: Gestión de Entornos Virtuales

### 2.1 Usando virtualenv (Método Tradicional)
```bash
# Crear entorno virtual
python -m venv venv_helloworld

# Activar entorno (macOS/Linux)
source venv_helloworld/bin/activate

# Activar entorno (Windows)
venv_helloworld\Scripts\activate

# Desactivar entorno
deactivate
```

### 2.2 Usando uv (Método Moderno)
```bash
# Instalar uv
pip install uv

# Crear proyecto con uv
uv init hello-world-project

# Activar entorno con uv
uv venv

# Instalar dependencias
uv add requests numpy
```
#TODO: averiguar si requests es necesario

## Parte 3: Desarrollo de Casos Hello World

### 3.1 Caso Básico
Archivo: `caso1_basico.py`
- Salida simple por consola
- Uso de variables básicas
- Comentarios explicativos

### 3.2 Caso Intermedio
Archivo: `caso2_intermedio.py`
- Funciones personalizadas
- Manejo de entrada del usuario
- Formateo de strings

### 3.3 Caso Avanzado
Archivo: `caso3_avanzado.py`
- Clases y objetos
- Manejo de excepciones
- Logging básico

## Parte 4: Flujo de Trabajo Completo

### 4.1 Inicialización del Proyecto
1. Crear directorio del proyecto
2. Inicializar entorno virtual
3. Configurar VS Code
4. Crear estructura de archivos

### 4.2 Desarrollo y Pruebas
1. Escribir código
2. Ejecutar pruebas
3. Depurar errores
4. Documentar cambios

### 4.3 Gestión de Dependencias
```bash
# Con pip tradicional
pip freeze > requirements.txt

# Con uv
uv export --format requirements-txt --output-file requirements.txt
```
TODO: hacer énfasis en que el primero es un método muy utilizado pero el segundo es medialte el framework

## Ejercicios Prácticos

### Ejercicio 1: Configuración Básica
- Instalar VS Code y extensiones
- Crear primer entorno virtual
- Ejecutar caso1_basico.py

### Ejercicio 2: Gestión Avanzada
- Comparar virtualenv vs uv
- Crear proyecto con uv
- Instalar y gestionar dependencias

### Ejercicio 3: Desarrollo Completo
- Implementar los 3 casos Hello World
- Configurar debugging en VS Code
- Crear documentación del proyecto

## Recursos Adicionales
- [Documentación oficial de uv](https://docs.astral.sh/uv/)
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)

## Próximos Pasos
Este laboratorio establece las bases para todos los proyectos futuros. En el siguiente capítulo exploraremos estructuras de datos y algoritmos básicos usando este mismo entorno.