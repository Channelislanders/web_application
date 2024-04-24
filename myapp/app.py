from functools import partial
from pathlib import Path

from shiny import App, Inputs, Outputs, Session, render, ui
from shiny.express import input, ui
from shiny.ui import page_navbar
here = Path(__file__).parent

ui.page_opts(
    title="Channel Islands Visualizations",  
    page_fn=partial(page_navbar, id="page"),  
)

# interactivity to let user input their daterange of interest
ui.input_date_range("daterange", "Date range", start="2020-01-01") 

#interactivity to let the user input their depth of interest
ui.input_numeric("numeric", "Numeric input", 0) 

#create a nav panel for the about's page
with ui.nav_panel("About"):  
    "About CINMS and our collaboration with NOAA The Channel Islands have been a core national park, providing socal visitors a chance to visit nature in their own backyard. Unfortunatly, from the pressures of various climate"


with ui.nav_panel("Data"):  
    "Talk a little about CESM"

with ui.nav_panel("Visualizations"):  
    "Visualizations of the Channel Islands"

@render.plot(alt = "Time series line plot")
def plot():
    #slice for particular timeframe
    test_2 = ds_20C.sel(time=slice(input.daterange()["0"], input.daterange()["1"]))

    #select the TEMP column and set z_t, which is depth to 0 for sea surface temeperature
    test_2000_2 = test_2.TEMP.sel(z_t = input.numeric(), method = "nearest")

    #select a member_id
    point_2 = test_2000_2.sel(member_id = 2)

    #select just one point on the graph (this point is closest to channel islands)
    point_3 = point_2.isel(nlat=(280), nlon=(240))

    return point_3.plot()