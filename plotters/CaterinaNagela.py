import seaborn.objects as so
from gapminder import gapminder


def plot():
    America = gapminder[gapminder["continent"] == "Americas"]
    figura = (
        so.Plot(
            data=America,
            x="year",
            y="lifeExp",
            group="country",
            color=America["country"] == "Argentina",
        )
        .add(so.Line())
        .add(so.Dots())
        .label(
            title="La expectativa de vida en Argentina con respecto a los demas paises de America",
            x="Año",
            y="Expectativa de vida",
            color="Argentina",
        )
    )
    return dict(
        descripcion="El grafico refleja la expectativa de vida en Argentina con respecto del resto de los paises de America",
        autor="Caterina Nagela",
        figura=figura,
    )
