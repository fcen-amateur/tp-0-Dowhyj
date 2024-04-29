import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(
            gapminder[(gapminder.continent == "Americas") & (gapminder['year'] == 1952)],
            x= "gdpPercap",
            y= "country",
            color="country"
        )
        .add(so.Dot())
        .label(
            title="PBI per capita en America en 1952",
            x="PBI per capita en millones",
            y="Paises",
        )
    )
    return dict(
        descripcion="Un gráfico del PBI per capita en los países de América en el año 1952",
        autor="Fátima Jordán",
        figura=figura,
    )