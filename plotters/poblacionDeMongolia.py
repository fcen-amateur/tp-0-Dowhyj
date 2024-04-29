import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(
            gapminder[gapminder.country == "Mongolia"],
            x="year",
            y="pop",
        )
        .add(so.Line())
        .label(
            title="Evolución de la población en Mongolia",
            x="Año",
            y="Población",
        )
    )
    return dict(
        descripcion="Un sofisticado gráfico con la evolución de la población de Mongolia por año",
        autor="Santillan, Lautaro",
        figura=figura,
    )
