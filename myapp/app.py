from pathlib import Path
import matplotlib.pyplot as plt
import xarray as xr
import shinyswatch

from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui
#from shared import ds_20C
#from plots import time_series
#from shared import temp
here = Path(__file__).parent


#load and combine arrray's here:
temp = xr.open_dataset(here / '20C_rcp85_temp.nc'
)
o2 = xr.open_dataset(here / '20C_rcp85_o2.nc'
)
salt = xr.open_dataset(here / '20C_rcp85_salt.nc'
)
sst = xr.open_dataset(here / '20C_rcp85_sst.nc'
)

#merge arrays here
merge_test = xr.merge([temp, o2, salt])

#seperate into 20C and rcp85 here





climate_variable_choices_TEMP = [
    "SALT",
    "O2",
    "TEMP"
]

climate_variable_choices_SST = [
    "SALT",
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

app_ui = ui.page_navbar(shinyswatch.theme.sandstone(),
    ui.nav_spacer(),
    ui.nav_panel(
        "About", 
        ui.layout_columns(
        ui.output_image("ch_image", inline=True, fill=True),
        ui.markdown(
        """
        ## Purpose
        The Channel Islands have been a core national park, providing people a chance to visit nature in their own backyard and are home to many diverse species and habitats. These habitats are highly sensitive to climate-driven ‘shock’ events which can include marine heat waves, and extreme fluctuations in pH or dissolved oxygen. Unfortunately, there few tools that currently exist that use climate data to create these visualizations easily. Current tools are satellite based and update from data that is gathered, such as the sanctuary watch tool provided by the [Channel Islands Sanctuary Watch website](https://sanctuarywatch.ioos.us/webcr-channelislands/). These do not give a future prediction of how these variables change, leading Channel Island staff to have limited information on creating a detailed action plan for possible restoration efforts.

        A collaborative project between UCSB and [CINMS](https://channelislands.noaa.gov/), funded by the National Oceanic and Atmospheric Association [NOAA](https://www.noaa.gov/), aims to develop climate-based indicators to enhance understanding and management. This application creates three visualizations that can be found in the visualizations tab: a time series visualization, a vertical profile visualization, and a mapping visualization. Users can use the dropdown menu to pick their specifications to create a plot of their interest (ex. a time series of the sea surface temperature levels). These are meant to help aid the Channel Island staff to make educated and meaningful decisions to ensure the longevity of the island’s ecosystem.

        It should be noted that this is a stepping stone towards creating an extensive visualization page to help see what certain climate conditions may look like in the future. It will allow others to carry on this project and use this prototype to cover more detailed information that may be of interest to Channel Island staff and other climate scientists that are interested in this project.






        
        This project was led by Dr. Samantha Stevenson-Michener, who leads the [Climate Data Lab](https://climate-datalab.org/) organization, which strives to break the barriers of those interested in getting into climate science research. This project was also led by Olivia Holt, Diana Navarro, and Patricia Park.



        Image from the NOAA 50th anniversary [poster series](https://sanctuaries.noaa.gov/posters/)

        """
    ),
        col_widths=(3, 8), fillable=True
    ),
    ),
    ui.nav_panel(
        "Data", 
        ui.layout_columns(
        ui.output_image("climate_image", inline=True),
        ui.markdown(
        """
        ## Climate Model
        A comprehensive Earth system model that simulates various components of the Earth's climate system, including the atmosphere, ocean, land surface, and sea ice.

        ## Large Ensemble
        A large ensemble is a set of simulations run with a given climate model which only vary the initial conditions. In this project the large ensemble used is CESM1 which is able to give historical, present and future readings of the outcome variables.

        ## [CESM-LE](https://www.cesm.ucar.edu/community-projects/lens)
        Distinguishing between model error and natural climate variations can be tricky. To address this challenge, the CESM community developed the CESM Large Ensemble (CESM-LE) specifically to help understand climate change while considering natural fluctuations. All simulations within CESM-LE utilize a single CMIP5 model, which is the CESM with the Community Atmosphere Model version 5. The plots created in this dashboard were created using CESM version 1 (CESM1).


        A paper detailing the advantages of using CESM-LE can be found [here.](https://journals.ametsoc.org/view/journals/bams/96/8/bams-d-13-00255.1.xml)


        """
    ),
        col_widths=(3, 8)
        ),
    ),
    ui.nav_panel(
        "Visualizations",
        ui.navset_card_underline(
             #time series nav panel
            ui.nav_panel("Time Series", 
                ui.input_select(
                id = "climate_variable_time",
                label = "Climate Variable",
                choices=climate_variable_choices_TEMP
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
                choices=climate_variable_choices_TEMP
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
                choices=climate_variable_choices_SST
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
#create if else statement to put into title of graph
        if (input.climate_variable_vertical() == 'SALT'):
            a = 'Salinity'
        elif (input.climate_variable_vertical() == 'O2'):
            a = "Dissolved Oxygen"
        elif (input.climate_variable_vertical() == 'TEMP'):
            a = "Temperature"
#experiment choice input using an if else statement
        if (input.experiment_choice_time() == 'mean'):
            b = y.mean("member_id")
        elif (input.experiment_choice_time() == 'max'):
            b = y.max("member_id")
        elif (input.experiment_choice_time() == 'min'):
            b = y.min("member_id")
#create plot (maybe try to see if changing the title works?)
        plot = (
            b.sel(z_t = 0, method = "nearest").plot(),
            plt.title(f"{a} Time Series") #think about implimenting depths into our time series?
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
#create if else statement to put into title of graph
        if (input.climate_variable_vertical() == 'SALT'):
            a = 'Salinity'
        elif (input.climate_variable_vertical() == 'O2'):
            a = "Dissolved Oxygen"
        elif (input.climate_variable_vertical() == 'TEMP'):
            a = "Temperature"
#experiment choice input using an if else statement
        if (input.experiment_choice_vertical() == 'mean'):
            b = y.mean("time").mean("member_id")
        elif (input.experiment_choice_vertical() == 'max'):
            b = y.max("time").mean("member_id")
        elif (input.experiment_choice_vertical() == 'min'):
            b = y.min("time").mean("member_id")
#create plot (maybe try to see if changing the title works?)
        plot = (
            b.plot(y = 'z_t'),
            plt.gca().invert_yaxis(),
            plt.title(f"{a} Vertical Profile")
        )
        #returns plot
        return plot

#render channel Islands poster to appear in web dashboard
    @render.image
    def ch_image():
        img = {"src": here / "ch_poster.jpg", "width": "300px"}
        return img
    

#render climate model picture to appear in web dashboard
    @render.image
    def climate_image():
        img_2 = {"src": here / "climate_model.jpeg", "width": "300px"}
        return img_2




app = App(app_ui, server)

