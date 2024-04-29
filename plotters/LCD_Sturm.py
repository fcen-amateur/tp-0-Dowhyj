import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(
            gapminder[gapminder["year"] == 2002],
            x="gdpPercap",
            y="lifeExp",
            color="continent",
        )
        .add(so.Dot())
        .label(
            title="Desarrollo Económico y Expectativa de Vida en 2002",
            x="Producto Bruto Interno Per Cápita",
            y="Expectativa de vida",
            color="Continente",
        )
    )
    return dict(
        descripcion="Relación entre el Producto Bruto Interno y la Expectativa de vida por continente en el año 2002",
        autor="Candelaria Sturm",
        figura=figura,
    )
