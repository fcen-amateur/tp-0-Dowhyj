import seaborn.objects as so
from gapminder import gapminder

esperanza_vida = gapminder.groupby([ 'year','continent'])['lifeExp'].mean().unstack()

def plot():
    figura = (
        so.Plot(gapminder, "year", "lifeExp")
        .add(so.Line(), so.Agg("mean"), color="continent")
        .label(
            title="Promedio de la expectativa de vida en función del año",
            x="Año",
            y="Expectativa de vida",
            color="Continente"
        )
        .layout(size=(6,6))
    )
    return dict(
        descripcion="Promedio de la expectativa de vida en función del año",
        autor="Santiago Paz",
        figura=figura,
    )
