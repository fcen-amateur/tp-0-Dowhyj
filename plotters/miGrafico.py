import seaborn.objects as so
from gapminder import gapminder


def plot():

    longitudes = gapminder[["gdpPercap", "country", 'continent']].copy()
    longitudes['len'] = longitudes['country'].str.len()

    figura = (
        so.Plot(longitudes, x="len", y='gdpPercap', color = 'continent')
        .add(so.Dot())
        .label(
            title="PBI per cápita según el largo del nombre",
            x="Largo del nombre del país",
            y="PBI per cápita",
        )
    )
    return dict(
        descripcion="¿El tamaño del nombre importa? Claramente tener un nombre de 6 letras provoca un mayor PBI per cápita.",
        autor="Juan José García Vizioli",
        figura=figura,
    )