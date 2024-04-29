from gapminder import gapminder
import matplotlib.pyplot as plt


def plot():
    arg_data = gapminder.query('country == "Argentina"')

    gobiernos_arg = [
        (1952, 1955, "Justicialista"),
        (1955, 1958, "Militar"),
        (1958, 1966, "Radical"),
        (1966, 1973, "Militar"),
        (1973, 1976, "Justicialista"),
        (1976, 1983, "Militar"),
        (1983, 1989, "Radical"),
        (1989, 1999, "Justicialista"),
        (1999, 2001, "Radical"),
        (2001, 2007, "Justicialista"),
    ]

    partidos_hues = {
        "Justicialista": "#318CE7",
        "Militar": "#22260b",
        "Radical": "#E10019",
    }

    for gobierno in gobiernos_arg:
        arg_data.loc[
            (arg_data["year"] >= gobierno[0]) & (arg_data["year"] < gobierno[1]),
            "gobierno",
        ] = gobierno[2]

    mean_gdpPercap = gapminder.groupby("year")["gdpPercap"].mean()
    with plt.style.context("ggplot"):
        seen = set()
        fig, ax = plt.subplots(1, 1, figsize=(11, 6))
        ax.plot(
            mean_gdpPercap,
            color="black",
            linestyle=":",
            label="PBI per cápita (Promedio mundial)",
        )
        ax.plot(
            arg_data["year"],
            arg_data["gdpPercap"],
            color="black",
            label="PBI per cápita (ARG)",
        )
        for start, stop, gobierno in gobiernos_arg:
            label = (
                (
                    f"Partido {gobierno}"
                    if gobierno != "Militar"
                    else "Militar (de facto)"
                )
                if gobierno not in seen
                else None
            )
            ax.axvspan(
                start,
                stop,
                color=partidos_hues[gobierno],
                alpha=0.35,
                label=label,
                closed=False,
                linewidth=0,
            )
            if gobierno not in seen:
                seen.add(gobierno)

        ax.set_xlim(arg_data["year"].min(), arg_data["year"].max())
        ax.set_xlabel("Año")
        ax.set_ylabel("PBI per cápita")
        ax.set_title("PBI per cápita en Argentina por gobierno")
        legend = ax.legend(
            loc="lower right",
            fancybox=True,
        )
        # set color to white with some alpha
        legend.get_frame().set_facecolor("white")
        legend.get_frame().set_alpha(0.5)
        return dict(
            descripcion="PBI per cápita en Argentina a lo largo de los años, con bandas de colores para denotar los distintos partidos políticos en el gobierno.\nTambién se indica el promedio mundial del PBI per cápita.",
            autor="Lucas Grasso Ramos",
            figura=fig,
        )
