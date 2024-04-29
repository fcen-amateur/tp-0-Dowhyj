import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(gapminder[gapminder['country'].isin(['Argentina', 'Paraguay', 'Uruguay', 'Brazil'])], "year", "gdpPercap", color = 'country')
        .add(so.Line())
        .add(so.Dots())
        .label(
            title="Países del Mercosur",
            x="Año",
            y="PBI",
        )        
    )
    return dict(
        descripcion="PBI per cápita de los países del mercosur a través de los años",
        autor="Cesar Momberg",
        figura=figura,
    )
