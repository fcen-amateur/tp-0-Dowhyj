import seaborn.objects as so
from gapminder import gapminder

#Filtro los datos por el continente deseado
datosAmerica = gapminder[(gapminder['continent'] == "Americas")].copy()

# Analizo los paises que tenemos
paises = datosAmerica["country"].unique()
#print(paises)

# Agrupo por region
sur_america = ["Colombia", "Venezuela", "Guyana", "Suriname", "Ecuador", "Peru", "Bolivia", "Brazil", "Paraguay", "Chile", "Argentina", "Uruguay"]
norte_america = ["Canada", "United States", "Mexico"]
central_america = ["Guatemala", "Belize", "Honduras", "El Salvador", "Nicaragua", "Costa Rica", "Panama", "Cuba", "Puerto Rico", "Trinidad and Tobago", "Dominican Republic", "Haiti", "Jamaica"]


# Función para asignar subregión a cada país
def asignar_subregion(pais):
    if pais in norte_america:
        return "América del Norte"
    elif pais in central_america:
        return "América Central"
    elif pais in sur_america:
        return "América del Sur"
    else:
        return "Otro"

# Aplico la función y modifico la tabla agregando su columna
datosAmerica['subregion'] = datosAmerica['country'].apply(asignar_subregion)

# Realizo el promedio de gdpPercap en cada subregion por año
datos_region = datosAmerica.groupby(['subregion','year'])["gdpPercap"].mean().reset_index()


def plot():
    figura = (
        (
        so.Plot(data = datos_region, x = "year", y = "gdpPercap", color = "subregion")
        .add(so.Bar()).facet("subregion",wrap = 3).layout(size = (12,8))
        .label(x = "year", y = "PBI", title = "Promedio de PBI por región", color = "Regiones de América")
        )
    )
    return dict(
        descripcion="PBI promedio de los paises americanos agrupados por regiones",
        autor="Damián Radiziviluk",
        figura=figura,
    )
