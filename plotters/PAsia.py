import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(
            gapminder[gapminder.continent == "Asia"],
            x="year",
            y="pop",
            color="country",
        )
        .add(so.Line())
        .label(
            title="Poblacion Asia",
            x="Año",
            y="Poblacion",
            color="País",
        )
    )
    return dict(
        descripcion="Poblacion de los paises de Asia a lo largo del tiempo",
        autor="Bautista Berardi",
        figura=figura,
    )