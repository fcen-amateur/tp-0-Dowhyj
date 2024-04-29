import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(data=gapminder, x="gdpPercap", y="lifeExp")
        .add(so.Dot(),color="year").scale(x="log")
        .facet("continent", wrap = 3)
        .layout(size=(12,10))
        .label(x= "PBI", y="Expectativa de vida", title="PBI vs. Expectativa de vida | {}".format)
        
    )
    return dict(
        descripcion="Graficos de dispersion donde se observa la relacion entre el PBI y la expectativa de vida en los paises de cada continente",
        autor="Francisco Battaglia",
        figura=figura,
    )
