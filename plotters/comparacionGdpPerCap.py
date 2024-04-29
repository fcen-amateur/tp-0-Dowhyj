import pandas as pd
import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
    so.Plot(
            pd.concat([gapminder[gapminder["continent"] == "Americas"], gapminder[gapminder["continent"] == "Europe"]], axis = 0),
            x="year", y="gdpPercap"
        )
        .add(so.Line(color = "grey"), group = "country")
        .add(so.Line(color = "red"), so.PolyFit(1))
        .facet("continent")
        .label(x = "Año", y = "PBI per Capita")
        )
    
    return dict(
        descripcion="Comparación entre el PBI per capita de America y Europa, se agrega una recta que aproxima los datos en cada continente para mostrar la diferencia entre los crecimientos de ambos",
        autor="Iván Agustín Bravo",
        figura=figura,
    )
