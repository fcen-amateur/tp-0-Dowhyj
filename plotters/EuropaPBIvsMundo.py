import seaborn.objects as so
from gapminder import gapminder
import pandas as pd

def plot():
    #  Creo un dataframe nuevo para agrupar los datos por año ( Probablemente se pueda hacer mejor )
    data = pd.DataFrame()
    years = gapminder['year'].drop_duplicates().values # Obtengo los años

    # Comparo todos por cada año la media de cada pais contra europa (Cuento solo a los paises que la superaron)
    for year in years:
        year_data = gapminder[gapminder['year'] == year] # Obtengo los datos del año
        media_pbi_europa = year_data[year_data['continent'] == 'Europe']['gdpPercap'].mean() # Media PBI europa en el año 
        resto_de_paises = year_data[(year_data['continent'] != 'Europe') & (year_data['gdpPercap'] >= media_pbi_europa)] # Paises que superaron la media de europa
        data = pd.concat([data, resto_de_paises], ignore_index=True) # Lo agrego al nuevo dataframe

    # Ploteo un histograma de los paises que superan el PBI de Europa por año
    figura = so.Plot(data, x='year').add(so.Bar(), so.Hist(), so.Dodge(), color='continent').label(x='', y='Paises que superan PBI europeo', legend='Continentes')


    return dict(
        descripcion="Histograma de los paises que superan el PBI de Europa por año",
        autor="Corrado De Luca",
        figura=figura,
    )
