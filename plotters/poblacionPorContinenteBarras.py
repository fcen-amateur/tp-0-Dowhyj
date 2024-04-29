import seaborn.objects as so
from gapminder import gapminder

grouped1 = gapminder.groupby(["year", "continent"])["pop"].sum().reset_index()


def plot():
    figura = (
        so.Plot(data=grouped1, x="year", y="pop", color="continent")
        .add(so.Bar(), so.Dodge())
        .label(
            title="Evolucion de la poblacion por continente",
            x="Año",
            y="Poblacion",
            color="Continente",
        )
    )
    return dict(
        descripcion="Cantidad de poblacion de cada continente a lo largo del tiempo",
        autor="Santiago Israel",
        figura=figura,
    )
