import seaborn.objects as so
from gapminder import gapminder
def plot():
    figura = (
        so.Plot(
            gapminder[gapminder["country"].isin(["Argentina","Japan"])],
            x="year",
            y="lifeExp",
            color="country",
        )
        .add(so.Line())
        .add(so.Dot())
        .label(
            title="Comparación de la expectativa de vida a traves de los años entre Argentina y Japon",
            x="Año",
            y="Expectativa de vida",
            color="País",
        )
    )
    return dict(
        descripcion="En esta comparación de la expectativa de vida a traves de los años entre Argentina y Japon,notamos que si bien en el 1950 ambas expectativas de vida eran similares, de alli en adelante, Japon se posiciono ampliamente por encima de Argentina ",
        autor="Malena do Brito",
        figura=figura,
    )
