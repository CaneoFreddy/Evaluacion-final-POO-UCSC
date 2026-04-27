# Sistema de Gestion Academica

Sistema de consola en Python para gestionar estudiantes, docentes, inscripciones, calificaciones y pagos de una universidad.

## Lenguaje y tecnologias

- Python 3.10+ (abc, datetime, enum)
- PlantUML para el diagrama de clases

## Estructura

```
.
├── main.py
├── README.md
├── sistema_academico.png
└── sistema_academico.puml
```

## Instalacion

```bash
git clone https://github.com/CaneoFreddy/Evaluacion-final-POO-UCSC.git
cd Evaluacion-final-POO-UCSC
```

## Como ejecutar

### Por Terminal (Recomendado)

```bash
python main.py
```

**En Windows (PowerShell o CMD):**
```powershell
python main.py
```

**En macOS o Linux:**
```bash
python3 main.py
```

Al ejecutar, se muestra un menu interactivo en la consola para navegar entre las opciones.

## Con Visual Studio Code (Opcional)

### Extensiones recomendadas

1. **Python** (Microsoft) - `ms-python.python`
   - Ejecuta y depura codigo Python

2. **PlantUML** (jebbs) - `jebbs.plantuml`
   - Visualiza el diagrama de clases (.puml)
   - Atajo: `Ctrl + Shift + P` → render PlantUML

3. **Markdown All in One** (Yu Zhang) - `yzhang.markdown-all-in-one` (Opcional)
   - Mejora la edicion del README

### Ejecutar en VSCode

- Abre `main.py` → Click derecho → "Run Python File in Terminal"
- O presiona `Ctrl + F5` (Windows) / `Cmd + F5` (Mac)

## Funcionalidades

- Listar estudiantes y docentes
- Inscribir estudiante en seccion pero valida los choques de horario
- Registrar notas parciales y el examen
- Calcular la nota final y el estado si esta aprobado o reprobado
- Gestionar pagos del arancel pero si tiene beca le descuenta
- Consultar horarios por seccion

## Notas

- El sistema es una simulacion basica pensada para consola
- En un futuro se podria mejorar con interfaz visual con tkinker o web con flask y django pero por el tiempo y los requerimientos de la evualuacion no se experimento con estos frameworks

## Diagrama de clases

![Diagrama UML del Sistema Academico](sistema_academico.png)

