import seaborn.objects as so
from gapminder import gapminder


def plot():
    filtro5paises = gapminder[gapminder.year == 2007].sort_values("pop", ascending=False).head()
    filtro = filtro5paises["country"].tolist() 

    figura = (
        so.Plot(
            gapminder[gapminder.country.isin(filtro)],
            x="year",
            y="pop",
            color="country",
        )
        .add(so.Line())
        .label(
            title="Top 5 de Paises con mas poblacion",
            x="Año",
            y="Poblacion en escala de mil millones",
            color="País",
        )
        .limit(y=(10000000, 1400000000))
    )
    return dict(
        descripcion="Muestra el Top 5 de paises con mas poblacion en el 2007 y como fue su evoluciono su poblacion hasta ese punto",
        autor="Gallardo Ignacio (iggallardo-uba)",
        figura=figura,
    )
