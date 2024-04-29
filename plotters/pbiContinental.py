import seaborn.objects as so
from gapminder import gapminder
import numpy as np #para poder calcular la media

gdpmean = gapminder.groupby(["year","continent"])["gdpPercap"] #agrupo por año y continente todos los paises de gapminder y luego tomo solo los valores del pbi
gdpmean = gdpmean.agg(np.mean) # calculo la media del pbi de los paises en cada continente
gdpmean = gdpmean.reset_index() # ya que groupby no me deja un dataframe, reseteo los indexs para que puedan ser leidos en el plot.

def plot():
    figura = (
        (
            so.Plot(gdpmean, x="year",y="gdpPercap",color="continent") 
            .add(so.Line())
            .label(title="Pbi per capita por continente a lo largo del tiempo",x="Año",y="Pbi Per Capita",color="continente")
        )
    )
    return dict(
        descripcion="Pbi per capita continental lo largo del tiempo",
        autor="Tomas Mateos",
        figura=figura,
    )
