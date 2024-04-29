import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(
            gapminder[gapminder.country == "Argentina"],
            x="year",
            y="gdpPercap",
        )
        .add(so.Line())
        .label(
            title="PBI per cápita en Argentina",
            x="Año",
            y="PBI per cápita",
        )
    )
    return dict(
        descripcion="Evolución del PBI per cápita en Argentina a través de los años",
        autor="Iván A. Miguel Viola",
        figura=figura,
    )
