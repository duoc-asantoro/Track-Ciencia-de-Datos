# Track-Ciencia-de-Datos
Track en CITT-DUOC Viña del Mar

## Reuniones
Martes 11:00 a 12:30
CITT

## 1. Identificación de la Necesidad
La apertura de la nueva mención de Ciencia de Datos en la carrera de Ingeniería Informática genera la necesidad de habilitar espacios prácticos y transversales donde los estudiantes apliquen dichas competencias en forma avanzada.
Actualmente, se evidencia una brecha en la articulación de metodologías activas que integren herramientas analíticas y de Ciencia de Datos en proyectos reales extracurriculares.

Si bien el Centro de Innovación y Transferencia Tecnológica (CITT) ofrece una infraestructura robusta, carece de un "track" específico guiado en Ciencia de Datos que canalice el potencial de los estudiantes de esta nueva mención. Este desafío disciplinar y formativo representa una oportunidad crítica: conectar las competencias en Ciencia de Datos con las actividades de co-creación del CITT, mitigando la falta de proyectos formales en analítica y potenciando el perfil de egreso mediante un entorno de aprendizaje práctico y colaborativo.

## 2. Descripción de la iniciativa
La iniciativa consiste en el diseño y facilitación metodológica del "Track de Ciencia de Datos" alojado en el CITT. El enfoque es de aprendizaje basado en proyectos (ABP) y mentoría técnica. Las acciones principales incluyen:

a.- Planificación de un ciclo de 3 talleres de orientación donde se transferir conocimientos : procesamiento de datos, modelamiento y visualización;

b.- Coordinación de desafíos prácticos autogestionados por los alumnos de la nueva mención dentro del CITT;

c. Sesiones breves de retroalimentación a las propuestas presentadas por los estudiantes.

Esta iniciativa se vincula directamente con los conocimientos en Ciencias de Datos : traspasando didácticamente las técnicas de análisis avanzado y gestión de datos, utilizándolas para guiar, estructurar y validar la rigurosidad científica de los proyectos que los alumnos desarrollen de forma autónoma.

## 3. Bibliografía

La siguiente es una Lista de Libros que se encuentran accesibles en la Biblioteca Digital O´Really, la cual se encuentra disponible para todos los alumnos de DUOC (accediendo con su cuenta de alumno)

- https://learning-oreilly-com.webezproxy.duoc.cl/playlists/ce074b13-314a-4c60-87ed-a7a0b175fa22

## 4. Propuesta Plan de Trabajo

**4.1. Metodología**

**a. Formato : "Agile/Laboratorio de Aprendizaje"**
- estudiantes son los ejecutores
- profesor es facilitador
- trabajo en duplas
- control de versiones en Git

**b. Weekly-Meeting (Sesión Semanal)**
- rol docente actua como ScrumMaster
- Stand-ups semanales (15-20 min al inicio): Cada dupla responde en 3 minutos:
  - ¿Qué analizó, construyó la dupla durante la anterior semana?
  - ¿Con qué sesgo, error de código o ausencia de dato se encontró?
  - ¿Qué se efectuará la próxima semana?
- Evaluación cruzada : Entre semanas 6 y 8, cada dupla revisa y comenta el código del repositorio de otra dupla (chequeo cruzado)

**4.2. Gobernanza de Proyectos y Estándar Git (Semanas 1-2)**
Con duplas trabajando en paralelo sobre el mismo repositorio u organización, la gestión de código puede volverse caótica rápidamente si no hay normas claras.

Estructura de Repositorio Unificada: plantilla de proyecto base en el GitHub/GitLab del CITT.

├── data/            <- raw/, processed/, final/ (ver como resolver caso de datos pesados)

├── notebooks/       <- Exploratorios versionados (1.0-eda.ipynb)

├── src/             <- Scripts Python modulares (.py)

├── references/      <- Documentación y diccionarios de datos

└── README.md        <- Hipótesis, objetivos de la dupla y resultados

Definir casos específicos, tales como:

**Protocolo de Datos Pesados:** Como se trabajará con datos que pesan gigabytes (Caso MercadoPublico), recordar que Git no guarda datasets. Abordar uso de .gitignore y almacenamiento compartido local.

**RUTs y Privacidad:** Cuales serán las reglas de anonimización o manejo ético cuando los dataset contengan RUTs o nombres personales.

**4.3. Hitos y Transferencia Tecnológica**

- **Hito 1 (Semana 4) - Data Pitch & EDA:** Presentación de 7 minutos por dupla con la carga del dataset, diccionario de datos identificado y  3 preguntas de negocio/públicas que responderán.

- **Hito 2 (Semana 8) - MVP Analítico (Dashboard / Pipeline):** Presentación del primer modelo descriptivo funcional o panel interactivo.

- **Hito 3 (Semana 12) - Demo Day :** Cierre del Track donde las duplas efectúan presentación ante la comunidad DUOC. Cada dupla entrega un Jupyter Notebook reproducible y un resumen de hallazgos (Resumen de Politica de 2 páginas).
