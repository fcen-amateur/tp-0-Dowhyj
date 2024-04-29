import numpy as np
import seaborn.objects as so
from gapminder import gapminder
from sklearn.cluster import DBSCAN, KMeans
from sklearn.preprocessing import StandardScaler


def plot():
    paises = gapminder.groupby("country").aggregate(
        {"lifeExp": "mean", "gdpPercap": "mean", "continent": "first"}
    )
    paises = paises[paises["gdpPercap"] < 40000]  # saco un outlier

    x = np.array(paises["lifeExp"])
    y = np.array(paises["gdpPercap"])
    data = np.column_stack([x, y])
    scaled = StandardScaler().fit_transform(
        data
    )  # no olvidarse de normalizar los datos

    desarrollo = KMeans(n_clusters=3, random_state=0, n_init="auto").fit_predict(scaled)
    desigualdad = DBSCAN(eps=0.2, min_samples=3).fit_predict(scaled)

    # nombro cada cluster
    mapeo = {0: "alto", 1: "bajo", 2: "medio"}
    paises["nivel de desarrollo"] = desarrollo
    paises["nivel de desarrollo"] = paises["nivel de desarrollo"].map(mapeo)

    mapeo2 = {0: "equitativa", -1: "desigual"}
    paises["distribucion de la riqueza"] = desigualdad
    paises["distribucion de la riqueza"] = paises["distribucion de la riqueza"].map(
        mapeo2
    )

    figura = (
        so.Plot(data=paises, x="lifeExp", y="gdpPercap")
        .add(so.Dots(pointsize=7), color="nivel de desarrollo", marker="continent")
        .scale(color="rocket")
        .label(x="Expectativa de vida media", y="Producto bruto interno medio")
    )
    return dict(
        descripcion="Un sofisticado gráfico con el número de países en cada continente",
        autor="La cátedra",
        figura=figura,
    )
