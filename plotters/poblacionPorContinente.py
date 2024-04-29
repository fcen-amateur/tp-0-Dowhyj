import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(gapminder, x="year", y = "pop", color = "continent")
        .add(so.Line(), so.Agg())
        .add(so.Dot(), so.Agg())
        .label(
            title="Población total por continente",
            x="Año",
            y="Cantidad de personas",
        )
    )
    return dict(
        descripcion="Análisis del crecimiento de la población por continente. Observamos que Asia y América presentan un crecimiento significativo, mientras que la población de Europa se encuentra planchada.",
        autor="La cátedra vaga",
        figura=figura,
    )
