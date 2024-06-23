# Copy_to_BackUp_HD

## Pasos para crear el proyecto
1. Creo el directorio del proyecto e ingreso en él
mkdir Copy_to_BackUp_HD
cd Copy_to_BackUp_HD

2. Creo el entorno virtual
python -m venv venv

3. Activo el entorno virtual
- En Windows:
.\venv\Scripts\activate
- En macOS/Linux:
source venv/bin/activate

4. Configurar el Entorno Virtual en VS Code
- Abre la paleta de comandos con Ctrl+Shift+P y escribe "Python: Select Interpreter".
- Selecciona el intérprete que corresponde a tu entorno virtual (debería tener la ruta de tu entorno venv).

5. Crear y Configurar el Script
- Creo un nuevo archivo en el proyecto llamado respaldo_mensual.py.

6. (Opcional) Crear un Archivo requirements.txt
pip freeze > requirements.txt

Este archivo contendrá todas las dependencias instaladas en tu entorno virtual. Otros usuarios o entornos pueden instalar estas dependencias con:
pip install -r requirements.txt
