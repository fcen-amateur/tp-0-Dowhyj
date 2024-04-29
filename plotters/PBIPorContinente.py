import seaborn.objects as so
from gapminder import gapminder


def plot():
    from matplotlib import style
    continentes = gapminder.groupby(['continent', 'year'])['gdpPercap'].sum()
    continentes = continentes.to_frame()

    figura = (
        so.Plot(
            data = continentes,
            x = 'year',
            y = 'gdpPercap',
            color = 'continent',
        )
        .add(so.Dot())
        .add(so.Line())
        .limit(x = (1970, 2010))
        .label(title = 'Comparación de PBI por continente',x = 'Año', y= 'PBI', color='Continentes')
        .layout(extent=[0, 0, .9, 1], engine = 'constrained')
        .theme(style.library["fivethirtyeight"])
    )





    return dict(
        descripcion="En este gráfico podemos ver la diferencia del producto bruto interno total por cada continente, y su evolución a través del tiempo.",
        autor="fela!",
        figura=figura,
    )
