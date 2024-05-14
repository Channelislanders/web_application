from pathlib import Path
import matplotlib.pyplot as plt
import xarray as xr

from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui
#from shared import ds_20C
#from plots import time_series
#from shared import temp
here = Path(__file__).parent


#load and combine arrray's here:
temp = xr.open_dataset(here / 'time_series_1990_2000_temp.nc'
)
o2 = xr.open_dataset(here / 'time_series_1990_2000_o2.nc'
)
salt = xr.open_dataset(here / 'time_series_1990_2000_salt.nc'
)
#merge arrays here
merge_test = xr.merge([temp, o2, salt])
merge_array = merge_test#.to_array()


climate_variable_choices = [
    "Sea Surface Temperature",
    "Salinity",
    "Dissolved Oxygen",
    "O2",
    "TEMP"
]

time_series_choices = [
    "Historical",
    "20TH Century",
    "RCP 8.5"
]

climate_experiment_choices = [
    "mean",
    "max",
    "min"
]

app_ui = ui.page_navbar(
    ui.nav_spacer(),
    ui.nav_panel(
        "About", 
        ui.output_image("ch_image"),
        ui.markdown(
        """
        The Channel Islands have been a core national park, providing socal visitors a chance to visit nature in their own backyard. Unfortunately, from the pressures of various climate, the Channel Islands faces increased vulnerability to climate-induced 'shock' events, threatening diverse marine species and habitats. These events can include marine heat waves, and extreme increases (or decreases) in pH or dissolved oxygen. A collaborative project between UCSB and CINMS, funded by the National Oceanic and Atmospheric Association (NOAA), aims to develop climate-based indicators to enhance understanding and management. [link](www.youtube.com)
         ![](ch_poster.jpg)
        """
    ),
    ),
    ui.nav_panel(
        "Data", 
        "A comprehensive Earth system model that simulates various components of the Earth's climate system, including the atmosphere, ocean, land surface, and sea ice."
    ),
    ui.nav_panel(
        "Visualizations",
        ui.navset_card_underline(
             #time series nav panel
            ui.nav_panel("Time Series", 
                ui.input_select(
                id = "climate_variable_time",
                label = "Climate Variable",
                choices=climate_variable_choices
        ),
            ui.input_select(
                id = "experiment_choice_time",
                label = "Experiment Choice",
                choices=climate_experiment_choices
        ),
                ui.output_plot("time_series")),
#vertical profile nav panel
            ui.nav_panel("Vertical Profile",
                ui.input_select(
                id = "time_series_vertical",
                label = "Time Frame",
                choices=time_series_choices
        ),
                ui.input_select(
                id = "climate_variable_vertical",
                label = "Climate Variable",
                choices=climate_variable_choices
        ),
                ui.input_select(
                id = "experiment_choice_vertical",
                label = "Experiment Choice",
                choices=climate_experiment_choices
        ),
                ui.output_plot("vertical_profile")),
#mapping nav panel
            ui.nav_panel("Mapping",        
                ui.input_select(
                id = "time_series_map",
                label = "Time Frame",
                choices=time_series_choices
        ),
                ui.input_select(
                id = "climate_variable_map",
                label = "Climate Variable",
                choices=climate_variable_choices
        ),
                ui.input_select(
                id = "experiment_choice_map",
                label = "Experiment Choice",
                choices=climate_experiment_choices
        ),
            ui.output_plot("mapping")),
        title="Model Visualization",
        ),
        {"class": "bslib-page-dashboard"},
    ), 
    id="tabs",
    title="Channel Islands Marine Sanctuary Climate Variability",
    fillable=True,
)


#test to see if output can be stored here
# output_test = input.climate_variable_time()
# merge_test_2 = merge_test.output_test

def server(input, output, session):

#used to run application with passing the arguments below:
#pass

#render the time series plot
    @render.plot
    #define time_series (goes into output)
    def time_series():
# define x as the reactive input
        x = input.climate_variable_time()
#define y as subsetting for whatever variable is picked
        y = merge_test[x]
    #experiment choice input using an if else statement
        if (input.experiment_choice_time() == 'mean'):
            a = y.mean("member_id")
        elif (input.experiment_choice_time() == 'max'):
            a = y.max("member_id")
        elif (input.experiment_choice_time() == 'min'):
            a = y.min("member_id")
#create plot (maybe try to see if changing the title works?)
        plot = (
            a.plot(),
            plt.title(f"{x} Time Series")
        )
        #returns plot
        return plot
    


#render the vertical profile plot
    @render.plot
    #define vertical_profile (goes into output)
    def vertical_profile():
# define x as the reactive input
        x = input.climate_variable_vertical()
#define y as subsetting for whatever variable is picked
        y = merge_test[x]
#experiment choice input using an if else statement
        if (input.experiment_choice_vertical() == 'mean'):
            a = y.mean("member_id")
        elif (input.experiment_choice_vertical() == 'max'):
            a = y.max("member_id")
        elif (input.experiment_choice_vertical() == 'min'):
            a = y.min("member_id")
#create plot (maybe try to see if changing the title works?)
        plot = (
            a.plot(),
            plt.title(f"{x} Time Series")
        )
        #returns plot
        return plot

#render image to appear in web dashboard
    @render.image
    def ch_image():
        img = {"src": here / "ch_poster.jpg", "width": "100px"}
        return img




app = App(app_ui, server)





#     @reactive.calc()
#     def filtered_dataset():
        #filter for what the user wants by time interest
        
    



    # @render.plot(timeseries)
    # @render.plot(verticalProfile)
    # @render.plot(mapping)



    # @app.callback(
    #     Outputs("roc_curve", "figure"),
    #     [Inputs("climate_variable", "value")]
    #     [Inputs("time_series", "value")]
    # )
    # def update_plots(climate_variable):
    #     # Here you can write logic to update the plots based on the selected climate variable
    #     # Example: Fetch data and generate new plot based on 'climate_variable'
    #     # Replace this with your actual implementation
    #     figure = generate_plot(climate_variable)  # Replace 'generate_plot' with your function
    #     return figure


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