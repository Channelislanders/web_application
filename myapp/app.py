from pathlib import Path

from shiny import App, Inputs, Outputs, Session, render, ui
#from shared import ds_20C
here = Path(__file__).parent

climate_variable_choices = [
    "Sea Surface Temperature",
    "Salinity",
    "Dissolved Oxygen"
]

time_series_choices = [
    "Historical",
    "20TH Century",
    "RCP 8.5"
]

app_ui = ui.page_navbar(
    ui.nav_spacer(),
    ui.nav_panel(
        "About", 
        "About CINMS and our collaboration with NOAA The Channel Islands have been a core national park, providing socal visitors a chance to visit nature in their own backyard. Unfortunately, from the pressures of various climate"
    ),
    ui.nav_panel(
        "Data", 
        "Talk about CESM 1"
    ),
    ui.nav_panel(
        "Visualizations",
        ui.input_select(
            id = "climate_variable",
            label = "Climate Variable",
            choices=climate_variable_choices
        ),
        ui.input_select(
            id = "time_series",
            label = "Time Frame",
            choices=time_series_choices
        ),
        ui.navset_card_underline(
            ui.nav_panel("Time Series", ui.output_plot("roc_curve")),
            ui.nav_panel("Vertical Profile", ui.output_plot("precision_recall")),
            ui.nav_panel("Mapping", ui.output_plot("precision_recall")),
            title="Model Metrics",
        ),
        {"class": "bslib-page-dashboard"},
    ), 
    id="tabs",
    title="Channel Islands Marine Sanctuary Climate Variability",
    fillable=True,
)



def server(input, output, session):
    @app.callback(
        Outputs("roc_curve", "figure"),
        [Inputs("climate_variable", "value")]
        [Inputs("time_series", "value")]
    )
    def update_plots(climate_variable):
        # Here you can write logic to update the plots based on the selected climate variable
        # Example: Fetch data and generate new plot based on 'climate_variable'
        # Replace this with your actual implementation
        figure = generate_plot(climate_variable)  # Replace 'generate_plot' with your function
        return figure



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