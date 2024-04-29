import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(gapminder, x="year", y='gdpPercap', color='continent')
        .add(so.Line(marker='D'), so.Agg(), so.Norm(where="x == x.min()", percent=True), so.Shift(y=-100))
        .scale(x=so.Continuous().tick(at=gapminder['year'].unique()))
        .label(
            title="Cambio relativo a 1952 de PBI per capita promedio por continente",
            x="Año",
            y="Cambio porcentual de PBI promedio respecto a 1952",
            color='Continente'
        )
    )
    return dict(
        descripcion="Para cada continente se grafica la variación el PBI per capita promedio en términos "
                    "porcentuales respecto a su PBI per capita promedio de 1952. Entre otros aspectos, se oberva que "
                    "el PBI per capita promedio de Europa aumentó casi un 350% desde 1952 y que el aumento promedio "
                    "relativo a 1952 en Asia en ligeramente inferior que el de África.",
        autor="Naza",
        figura=figura,
    )