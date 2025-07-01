# CodexMachina Project

Una herramienta para extraer y procesar texto de varios formatos de documentos.

## Roadmap del Proyecto

### Fase 1: MVP (Producto Mínimo Viable)
- Extracción básica de texto de múltiples formatos de documentos (PDF, DOCX)
- Detección simple de bloques de código
- Interfaz funcional con Streamlit
## Primeros Pasos

### Requisitos Previos
- Python 3.8 o superior
- Paquetes requeridos (instalar usando `pip install -r requirements.txt`):
  - streamlit
  - PyPDF2
  - pdfplumber
  - python-docx
  - pandas
  - spacy
  - python-magic-bin

### Instalación

1. Clona el repositorio:

git clone https://github.com/tuusuario/CodexMachina-Project.git cd CodexMachina-Project


2. Instala las dependencias:

pip install -r requirements.txt

3. Descarga el modelo de spaCy:

python -m spacy download es_core_news_sm

### Ejecutando la Aplicación

Inicia la aplicación Streamlit:

streamlit run codexmachina/src/app.py

## Características

- **Procesamiento de Documentos**: Extracción de texto de archivos PDF y DOCX
- **Detección de Código**: Identificación de bloques de código dentro de documentos
- **Interfaz Interactiva**: Interfaz amigable con Streamlit para análisis de documentos

## Estructura del Proyecto

CodexMachina-Project/
├── codexmachina/
│   ├── src/
│   │   ├── app.py                  # Aplicación principal de Streamlit
│   │   ├── extraction/             # Módulos de extracción de documentos
│   │   │   ├── docx_parser.py      # Analizador de archivos DOCX
│   │   │   ├── pdf_parser.py       # Analizador de archivos PDF
│   │   ├── processing/             # Módulos de procesamiento de texto
│   │   │   ├── code_detector.py    # Detección de bloques de código
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Documentación del proyecto

## Próximos Pasos

### Fase 2: Mejoras de Procesamiento

- NLP para identificar secciones (instalación, configuración, ejemplos)
- Reconocimiento de comandos de terminal
- Clasificación de fragmentos (Python, Bash, SQL)

### Fase 3: Funcionalidades Avanzadas

- Generación automática de APIs
- Integración con LLMs para explicar código
- Exportación a Jupyter Notebooks