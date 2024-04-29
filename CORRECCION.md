## Repos

### FelaBoucai FelaBoucai main
Borra los archivos originales. No está mal en un TP, pero esto es una app desarrollada en conjunto, hay que mantenerlos.

### Demianfraiman/tp-0-Demianfraiman/main et al
Archivos desactualizados de GH Classroom, desestimados.

### fcen-amateur tp-0-FatimaJordan1 main
Pisa archivos preexistentes de ejemplo

### Sisra tp-0-SantiagoIsrael main
Están mal resueltos todos los paréntesis y el indentado de `figura`, no carga sin correcciones.

### fcen-amateur tp-0-LucasGrasso feedback
Interesante propuesta! El gráfico planteado efectivamente requiere mucha flexibilidad para dibujarlo así que vale la pena permitir el uso de `matplotlib`. Lo generalicé para aceptar _otros_ objetos que devuelven figuras.

## Graficos
### lifeExpAmerica
Plagio casi absoluto del gráfico ejemplo `lifeExpOceania`, pero con menor claridad (cf. PAsia sobre escala cromática con demasiadas categorías).

### mediaPorContinente
Fatla parentesis de cierre en asignacion a `figura`

### my_plot
No corre; nunca pasa canal `y`. Pasa `x="continent"`, que tampoco se condice con la descripción de 
> 'Relación entre gdp per capita y expectativa de vida - Sin cono Norte'

### nose
Varios errores de sintaxis. De mínima sobra un paréntesis en la L13, e intenta usar `datos_oceania` sin haberlo definido.

### nuevoarchivo
Copia exacta de uno de los ejemplos, no realiza la consigna.

### PAsia
Una escala cromática con decenas de colores es ilegible (¡lo dijimos en clase!). Una escala lineal en `y` que cubra con varios órdenes de magnitud (de la pob. de China a Bahrain) es ilegible. Mejor, usar logarítmica o mostrar menos datos.

### PBIPorContinente, pbiContinental
La _suma_ del PBI per cápita de varios países no es el PBI per cápita del conjunto (`PBIPorContinente`). Tampoco el p_promedio simple_ (`pbiContinental`). Lo que buscan es el promedio del PBI per cápita, **pesado por la población de cada país**.

### nivel_de_desarrollo
Usa métodos de `numpy` sin importarlos, al igual que `sklearn.cluster.DBSCAN`. Menciona una métrica `d` en los argumentos de DBSCAN que nunca define.
Por último, no pone ni descripción ni autor del gráfico. ¡Pero gran idea para el gráfico!

### plot
Evite usar nombres tán genericos de archivos la próxima vez.

### promedioExpectativaVida
La idea no es mala, y está bien el uso de los agregados de `so.Agg`, pero cf. `PBIPorContinente, pbiContinental` a razón de los problemas en tomar promedios de promedios.

### test
Copia exacta de paisesPorContinente. Explícitamente se pidió que no repitan gráficos.

### PBI_Subregiones_América
Habla de PBI, pero la variable de estudio es PBI _per cápita_. ¡Nada mal!

### PBIpercapitaAmerica
Iría mejor representado con un gráfico de barras que un scatterplot, y ordenando las barras de mayor a menor. El canal de color es irrelevante.

### aaaaaaa
Elija un nombre razonable de archivo la próxima vez. Cf. `PBIPorContinente, pbiContinental` a razón de los problemas en tomar promedios de promedios.

### doBrito
Impecable. Sencillo, responde a la consigna, claro.

### poblacionPorContinente (lineas)
Interesante! Sería mejor una escala logarítmica para ejemplificar un crecimiento que es compuesto como el poblacional.

### promedioExpectativaVida
Ojo en tomar promedios sin ponderar cuando los diferentes países tienen poblaciones dramáticamente distintas.

### tp0-Valli
El gráfico está roto, no muestra los datos de Chile. Lo natural es pasar "country" como variable al canal "color". Ver versión corregida.
[No usen guiones en los nombres](https://stackoverflow.com/questions/761519/is-it-ok-to-use-dashes-in-python-files-when-trying-to-import-them) de módulos que se vuelve un peligro para importarlos.

### Tp_o_Finalizado
Entrega un notebook de Jupyter, en lugar de un script de Python. No cumple la consigna.

### Aporte-Francisco Battaglia
Muy confuso el gráfico, tal vez sería más claro reduciendo la cantidad de información exhibida.

### CaterinaNagela
`so.Dots` es una _clase_, a `so.add`, como primer argumento, hay que pasarle una _instancia_ de la clase, llamándola sin argumentos: `so.Dots()`, al igual que lo hace en la línea previa con `so.Line()`.