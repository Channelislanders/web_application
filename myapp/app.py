from functools import partial
from pathlib import Path

from shiny import App, Inputs, Outputs, Session, render, ui
#from shiny.express import input, ui
#from shiny.ui import page_navbar
from shared import ds_20C
here = Path(__file__).parent

app_ui = ui.page_navbar(
    ui.nav_spacer(),
        ui.nav_panel(
        "About",
        ui.layout_columns(
            ui.value_box(title="Row count", value=ui.output_text("row_count")),
            ui.value_box(
                title="Mean training score", value=ui.output_text("mean_score")
            ),
            fill=False,
        ),
        ui.card(ui.output_data_frame("data")),
        {"class": "bslib-page-dashboard"},
    ),
    ui.nav_panel(
        "Training Dashboard",
        ui.navset_card_underline(
            ui.nav_panel("ROC Curve", ui.output_plot("roc_curve")),
            ui.nav_panel("Precision/Recall", ui.output_plot("precision_recall")),
            title="Model Metrics",
        ),
        ui.card(
            ui.card_header("Training Scores"),
            ui.output_plot("score_dist"),
        ),
        {"class": "bslib-page-dashboard"},
    ),
    sidebar=ui.sidebar(
        ui.input_select(
            "account",
            "Account",
            choices=[
                "Berge & Berge",
                "Fritsch & Fritsch",
                "Hintz & Hintz",
                "Mosciski and Sons",
                "Wolff Ltd",
            ],
        )
    ),
    id="tabs",
    title="Model scoring dashboard",
    fillable=True,
)


def server(input: Inputs):
    @reactive.calc()
    def dat() -> pd.DataFrame:
        return scores.loc[scores["account"] == input.account()]

    @render.plot
    def score_dist():
        return plot_score_distribution(dat())

    @render.plot
    def roc_curve():
        return plot_auc_curve(dat(), "is_electronics", "training_score")

    @render.plot
    def precision_recall():
        return plot_precision_recall_curve(dat(), "is_electronics", "training_score")

    @render.text
    def row_count():
        return dat().shape[0]

    @render.text
    def mean_score():
        return round(dat()["training_score"].mean(), 2)

    @render.data_frame
    def data():
        return dat()


app = App(app_ui, server)













#ui.page_opts(
 #   title="Channel Islands Visualizations",  
  #  page_fn=partial(page_navbar, id="page"),  
#)

# interactivity to let user input their daterange of interest
#ui.input_date_range("daterange", "Date range", start="2020-01-01") 

#interactivity to let the user input their depth of interest
#ui.input_numeric("numeric", "Enter depth of interest", 0) 

#create a nav panel for the about's page
#with ui.nav_panel("About"):  
#    "About CINMS and our collaboration with NOAA The Channel Islands have been a core national park, providing socal visitors a chance to visit nature in their own backyard. Unfortunatly, from the pressures of various climate"


#with ui.nav_panel("Data"):  
#    "Talk a little about CESM"

#with ui.nav_panel("Visualizations"):  
 #   "Visualizations of the Channel Islands"

#@render.plot(alt = "Time series line plot")
#def plot():
    #slice for particular timeframe
 #   test_2 = ds_20C.sel(time=slice(input.daterange()["0"], input.daterange()["1"]))

    #select the TEMP column and set z_t, which is depth to 0 for sea surface temeperature
  #  test_2000_2 = test_2.TEMP.sel(z_t = input.numeric(), method = "nearest")

    #select a member_id
   # point_2 = test_2000_2.sel(member_id = 2)

    #select just one point on the graph (this point is closest to channel islands)
  #  point_3 = point_2.isel(nlat=(280), nlon=(240))

   # return point_3.plot()