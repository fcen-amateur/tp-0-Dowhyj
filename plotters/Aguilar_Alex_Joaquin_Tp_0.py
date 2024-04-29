import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn.objects as so
from gapminder import gapminder

#Para ello me quedo solo con los datos de esos paises:
limit_list = [ "Argentina",'Bolivia', 'Brazil', 'Chile', 'Paraguay','Uruguay' ]
limit_bool = gapminder["country"].isin(limit_list)
limit = gapminder[limit_bool]

#Ahora me quedo con 3 años: (1952 1977 2007):
años_list = [1952,1977,2007]
años_bool = limit["year"].isin(años_list)
limit_3_años = limit[años_bool]

#Grafico esos 3 años:

def plot():
    figura = (
              so.Plot(limit_3_años, "country","gdpPercap", edgecolor="country")
              .facet("year", wrap=0)
              .add(so.Bar(color="black", edgewidth=3 ))
              .layout(size=(15,5))
              .label(title= "Año {}".format, x="Paises") 
              .theme({ "axes.edgecolor": "black"})
              )
    return dict(
        descripcion="gdpPercap entre Argentina y sus paises limitrofes a lo largo de 3 Años (1952,1977,2007)",
        autor="Alex Joaquin Aguilar",
        figura=figura,
    )
