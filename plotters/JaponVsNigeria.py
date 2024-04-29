import seaborn.objects as so
import matplotlib.pyplot as plt
from gapminder import gapminder

def plot():
    from matplotlib import style
    jap = gapminder[gapminder.country == "Japan"]
    nig = gapminder[gapminder.country == "Nigeria"]

    figura = (
        so.Plot(
            data = gapminder[(gapminder.country == "Japan") | (gapminder.country == "Nigeria")],
            x = "year",
        )

        .add(so.Dot(color = "orange", edgecolor = ".1", edgewidth = .5), data = jap, y ="pop")
        .add(so.Line(color = "orange"), so.PolyFit(2), label = "Japón", data = jap, y ="pop")

        .add(so.Dot(color = "g", edgecolor = ".1", edgewidth = .5), data = nig, y ="pop")
        .add(so.Line(color = "g", fillcolor = "blue"), so.PolyFit(2), label = "Nigeria", data = nig, y ="pop")

        .layout(extent=[0, 0, .9, 1], engine = 'constrained')
        .theme(style.library["fivethirtyeight"])


        .limit(x = (1950, 2010), y = (0, 1.5*1e8))
        .label(
            x="Año",
            y="Población",
            title= 'Comparación de poblaciones entre Japón y Nigeria'
        )

        


    )

    return dict(
        descripcion="Crecimiento poblacional de Japón contra Nigeria. En este gráfico podemos ver que el crecimiento en Nigeria es mucho mayor. Tambíen podemos predecir que la población de Nigeria va a superar a la de Japón ampliamente.",
        autor="fela!",
        figura=figura,
    )
