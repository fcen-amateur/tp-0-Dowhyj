import matplotlib.pyplot as plt
from gapminder import gapminder


def plot():
    fig = plt.figure(figsize=(11, 6))
    ax = fig.add_subplot(111)
    gapminder_2007 = gapminder[gapminder["year"] == 2007]
    gapminder_2007.groupby("continent")["pop"].sum().plot(kind="bar", ax=ax)
    ax.set_xlabel("Continente")
    ax.set_ylabel("Población")
    ax.set_title("Población por continente en 2007")

    
    return dict(
        descripcion="Un sofisticado gráfico con la población por continente en 2007",
        autor="La cátedra, Lucas Grasso Ramos",
        figura=fig,
    )
