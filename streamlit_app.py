import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Batallan Máximo
##### *Data Science, Especialista en Mercados de Capitales, Contador Público* 
''')

image = Image.open('foto cv.jpg')
st.image(image)

st.markdown('## Acerca de mí', unsafe_allow_html=True)
st.info('''
- Cientifico de datos, apasionado por la automatización de proceso y desarrollo de soluciones informaticas. 
- Experiencia en multinacionales, Auditorias externas (Sancor salud, Fideicomisos financieros, Hotel Four Seasons).
- Desarrollador de sistemas de gestión y reportes en diferentes rubros (Control de stock, Cash Flow, P&L statement).
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #212529;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/maximo-batallan-9a2508103/" target="_blank">Maximo Batallan</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#batallan-m-ximo">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#educaci-n">Educación</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#experiencia-laboral">Experiencia Laboral</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#proyectos">Herramientas Informaticas</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Redes</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Educación
''')

txt('**Data Science, Tecnología de la información**, *Henry*, Argentina',
'2022')
st.markdown('''
- Promedio: `8.00`
- Diseño de soluciones informaticas `en base a los datos con los que se va a trabajar y lo pretendido por el usuario/cliente`.
- Ingeniería de Datos `como se obtienen y transforman los datos` datawarehouse y machine learning para realizar predicciones sobre métricas en particular.
- Data Analytics `PowerBi` generación de reportes de visualización.
''')

txt('**Especialista en Mercados de Capitales**, *Universidad de Buenos Aires*, Argentina',
'2019-2021')
st.markdown('''
- Promedio: `7,50`
- Evaluación de estados financieros `Medición de Riesgos para la compra o venta de distintos activos financieros`.
- Analisis cualitativos y cuantitativos de diferentes productos financieros `Bonos, Acciones, FCI, Futuros`.
''')

txt('**Contador Público**, *Universidad de Buenos Aires*, Argentina',
'2012-2019')
st.markdown('''
- Promedio: `5,50`
- Creación de sociedades de acuerdo a la `Ley 19.550 de la República Argentina`.
- Confección de Estados Financieros `Bonos, Acciones, FCI, Futuros`.
- Matrícula Profesional emitida por el Consejo Profesional de Ciencias Economicas de Buenos Aires `Tomo: 430 Folio: 136`



''')

#####################
st.markdown('''
## Experiencia Laboral
''')

txt('**Auditor Externo, Ernst & Young**, Asistente experimentado, Bs. As., Argentina',
'2016-2018')
st.markdown('''
- Auditorias externas de servicios financieros `Fideicomisos Financieros, Fondos Comunes de Inversión` 
- Auditorias financieras de servicios Hoteleros.
- Auditorias financieras de Seguros.
**Logro**: Implementación de Macros Excel para la automatización de tareas operativas mensuales y carga automatizada de estados contables de las compañias.
''')

txt('**Administrativo Contable**, Club Inn, Bs. As., Argentina',
'2014-2016')
st.markdown('''
- Preparación de reportes mensuales. `posición contable ante los impuestos, Impuestos al valor agregado, Ingresos Brutos.` 
- Encargado de cuentas a pagar..
**Logro**: He podido afianzar mis Soft Skills, `una PYME la cual se podia aprender de todas las posiciones.`
''')





#####################
st.markdown('''
## Proyectos
''')
txt4('Henry', 'Desarrollo de Machine Learning, ETL, busqueda del mejor modelo, conexión a la API de la informacion, deploy del proyecto, testeo de la app', 'https://maximobatallan-proyectoindividual3-pi3-vatkos.streamlit.app')
txt4('Henry', 'Sistema de Recomendación de productos Amazon, NLP, proceso natural del lenguaje con reconociento de voz','https://github.com/maximobatallan/proyectofinal')
txt4('Desarrollo Freelance', 'Sistema de Gestión Gastronomica','https://www.linkedin.com/feed/update/urn:li:activity:6658862422964654080/')



#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`')
txt3('Data processing', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`')
txt3('Machine Learning', '`scikit-learn`')
txt3('GUI Projects', '`Tkinter`')
txt3('Web Scraping', '`Beautiful Soup`, `Selenium`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `Heroku`, `AWS`, `Azure`')

#####################
st.markdown('''
## Social Media y Contacto
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/maximo-batallan-9a2508103/')
txt2('GitHub', 'https://github.com/maximobatallan')
txt2('Mail', 'maximobatallan@gmail.com')

