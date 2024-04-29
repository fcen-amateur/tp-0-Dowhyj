import seaborn.objects as so
from gapminder import gapminder
import pandas as pd


def plot():
    datos = gapminder
    PaisPorContinente = datos.groupby("continent")["country"].nunique()
    poblacion_2007_Oceania = datos[(datos['year'] == 2007) & (datos['continent'] == 'Oceania')]
    poblacion_total_2007_Oceania = poblacion_2007_Oceania['pop'].sum()
    poblacion_2007_Africa = datos[(datos['year'] == 2007) & (datos['continent'] == 'Africa')]
    poblacion_total_2007_Africa = poblacion_2007_Africa['pop'].sum()
    poblacion_2007_Americas = datos[(datos['year'] == 2007) & (datos['continent'] == 'Americas')]
    poblacion_total_2007_Americas = poblacion_2007_Americas['pop'].sum()
    poblacion_2007_Asia = datos[(datos['year'] == 2007) & (datos['continent'] == 'Asia')]
    poblacion_total_2007_Asia = poblacion_2007_Asia['pop'].sum()
    poblacion_2007_Europa = datos[(datos['year'] == 2007) & (datos['continent'] == 'Europe')]
    poblacion_total_2007_Europa = poblacion_2007_Europa['pop'].sum()
    poblacion_promedio_por_pais_Oceania = poblacion_total_2007_Oceania/PaisPorContinente["Oceania"]
    poblacion_promedio_por_pais_Americas = poblacion_total_2007_Americas/PaisPorContinente["Americas"]
    poblacion_promedio_por_pais_Africa = poblacion_total_2007_Africa/PaisPorContinente["Africa"]
    poblacion_promedio_por_pais_Asia = poblacion_total_2007_Asia/PaisPorContinente["Asia"]
    poblacion_promedio_por_pais_Europa = poblacion_total_2007_Europa/PaisPorContinente["Europe"]

    continentes = pd.DataFrame({"nombre":["Asia","Americas","Europa","Africa","Oceania"], "Poblacion_Promedio_Por_Pais":[poblacion_promedio_por_pais_Asia, poblacion_promedio_por_pais_Americas, poblacion_promedio_por_pais_Europa, poblacion_promedio_por_pais_Africa, poblacion_promedio_por_pais_Oceania]})

    figura = (
        so.Plot (data = continentes , x = "nombre", y = "Poblacion_Promedio_Por_Pais")
        .add (so.Bar())
        .label(title = "Población promedio por pais en cada continente", x = "Continentes", y = "Población promedio por pais (1.0 = 100 Millones)" )
        )

    return dict(
        descripcion="Este grafico muestra la diferencia que hay entre la cantidad promedio de poblacion por pais en cada continente",
        autor="Matias Cicculli",
        figura=figura,
    )
