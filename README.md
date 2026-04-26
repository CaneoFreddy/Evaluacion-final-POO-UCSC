Sistema de Gestion Academica
Sistema de consola en Python para gestionar estudiantes, docentes, inscripciones, calificaciones y pagos de una universidad.
Lenguaje y tecnologias
Python 3.10+(abc, datetime, enum)
PlantUML para el diagrama de clases
Estructura; 
,
main.py,
README.md
 diagrama.png,  
diagrama.puml,       
        

# 1. Clonar el repositorio
git clone origin https://github.com/CaneoFreddy/Evaluacion-final-POO-UCSC.git
cd Evaluacion-final-POO-UCSC

# 2. Ejecutar el sistema
python Evaluacion-final-POO-UCSC.py

### Por Terminal (Recomendado)

Requisito: tener Python 3.10 o superior instalado.

```bash
# 1. Navegar a la carpeta del proyecto
cd "ruta/a/tu/carpeta/Evaluación Sumativa Final-Freddy Caneo"

# 2. Ejecutar el sistema
python main.py
```

* (PowerShell o CMD):*
powershell:
python main.py




Al ejecutar, se muestra un menú interactivo en la consola para navegar entre las opciones.

### Con Visual Studio Code (Opcional)

Si usas Visual Studio Code, instala estas extensiones recomendadas:

1. **Python** (Microsoft)
   - Ejecuta y depura código Python
  

2. **PlantUML** (jebbs)
   - Visualiza el diagrama de clases (.puml)

3. **Markdown All in One** (Yu Zhang) - Opcional
   - Mejora la edición del README


**Para ejecutar en VSCode:**
- Abre `main.py` → Click derecho → "Run Python File in Terminal"
- O presiona `Ctrl + F5` (Windows) / `Cmd + F5` (Mac)
- Ctrl + shift + p : para descargar imagen de plantuml

Funcionalidades:
Lista de estudiantes y docentes
Inscribir el respectivo estudiante en su debida seccion
Registrar notas parciales y examen
Calcular nota final y estado (aprobado/eprobado)
Gestionar pagos de arancel con descuento por beca
Consultar horarios por seccion

## Diagrama de clases

![Diagrama UML del Sistema Académico](sistema_academico.png)

