import seaborn.objects as so
from gapminder import gapminder


def plot():
    datos = gapminder[gapminder.country.isin(["Argentina", "Chile"])]
    figura = (
        so.Plot(datos, x="year", y="gdpPercap", color="country")
        .add(so.Line())
        .label(
            title="El PBI per capita de Argentina y Chile",
            x="Año",
            y="PBI per capita",
        )
    )
    return dict(
        descripcion="Comparación del PBI per capita de Argentina y Chile a través de los años",
        autor="Francisca Valli",
        figura=figura,
    )
