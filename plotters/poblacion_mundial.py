import seaborn.objects as so
from gapminder import gapminder
from IPython.display import display


datos_china = gapminder[gapminder.country == "China"]
datos_india = gapminder[gapminder.country == "India"]
datos_arg = gapminder[gapminder.country == "Argentina"]
datos_asia = gapminder[gapminder.continent == "Asia"]

datos_asia = datos_asia[datos_asia.country != "China"]
datos_asia = datos_asia[datos_asia.country != "India"]

def plot():
    figura = (
        so.Plot()
        .add(so.Line(color = "Red"),
             x = datos_china["year"],
             y = datos_china["pop"],
             label="China")
        .add(so.Line(color = "Orange"),
             x = datos_india["year"],
             y = datos_india["pop"],
             label = "India")
        .add(so.Line(color = "Grey"),
             data = datos_asia,
             x = "year",
             y = "pop",
             group = "country",
             label = "Resto del mundo")
        .add(so.Line(color = "Lightblue"),
             x = datos_arg["year"],
             y = datos_arg["pop"],
             label = "Argentina")
        .label(title = "Países más poblados del mundo",
               x = "Año",
               y = "Población")
        #.scale()
    )
    return dict(
        descripcion="Evolución de la población de los países más poblados vs el resto del mundo",
        autor="Santiago Oviedo",
        figura=figura,
    )


res = plot()
graf = res.get("figura")
graf.show()
