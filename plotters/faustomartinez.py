import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(
            data=gapminder[gapminder.continent =="Americas"], 
            x="year", 
            y="gdpPercap"
        )
        .add(so.Lines(color="#bbca"),group="country")
        .add(so.Line(color="blue"),data=gapminder[gapminder.country=="Argentina"],label="Argentina")
        .label(
            title="PBI per cápita en los paises americanos",
            x="Año",
            y="PBI per cápita"
        )
    )
    return dict(
        descripcion="PBI per cápita en América vs. en Argentina",
        autor="Fausto Martínez",
        figura=figura,
    )
