import seaborn.objects as so
from gapminder import gapminder


def plot():
    argentina = gapminder[gapminder['country']=='Argentina']
    figura = (
    so.Plot(argentina, "pop", "gdpPercap")
    .add(so.Line())
).label(title = "Poblacion vs. PBI per cápita Argentina 1950-2007",
        x="Poblacion [decenas de millones]",
        y="PBI per cápita [USD]")

    return dict(
        descripcion="Evolución del PBI como función de la población en Argentina",
        autor="Facundo Gancedo García",
        figura=figura,
    )
