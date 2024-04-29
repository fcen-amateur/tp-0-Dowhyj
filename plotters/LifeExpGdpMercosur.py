import seaborn.objects as so
from gapminder import gapminder
data=gapminder[(gapminder['country'] == 'Argentina') |
                           (gapminder['country'] == 'Brazil') |
                           (gapminder['country'] == 'Uruguay') |
                           (gapminder['country'] == 'Paraguay') |
                           (gapminder['country'] == 'Venezuela')]

def plot():
    figura = (
        so.Plot(data,
        x = "year",
        y = "lifeExp",
        color="country")
        .add(so.Dots(), pointsize="gdpPercap").scale(pointsize=(1, 14))
        .add(so.Lines())
        .label(
            title="Relacion entre Gdp per capita y expectativa de vida en el Mercosur",
            x="Año",
            y="Expectativa de vida"
        )
    )
    return dict(
        descripcion="Comparacion de gdpPercap y Expectativa de vida a lo largo del tiempo",
        autor="Tantos Ignacio",
        figura=figura,
    )
