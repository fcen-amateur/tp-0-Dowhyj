import seaborn.objects as so
from gapminder import gapminder


def plot():
    datos_year = gapminder[(gapminder['year'] == 2007)]
    figura = (
        so.Plot(data=datos_year, x = 'lifeExp', y = 'gdpPercap')
        .add(so.Dot(), color = 'continent')
        .label(
            title="Datos del año 2007",
            x="Esperanza de vida",
            y="PBI per Capita",
    )
)

    return dict(
        descripcion="Un grafico que muestra la relación entre el PBI per capita y la esperanza de vida",
        autor="Mauricio Boscolo",
        figura=figura.limit(x=(30,90)),
    )