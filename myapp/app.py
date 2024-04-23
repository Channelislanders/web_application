from functools import partial

from shiny.express import ui
from shiny.ui import page_navbar

ui.page_opts(
    title="Channel Islands Visualizations",  
    page_fn=partial(page_navbar, id="page"),  
)

with ui.nav_panel("About"):  
    "About CINMS and our collaboration with NOAA"

with ui.nav_panel("Data"):  
    "Talk a little about CESM"

with ui.nav_panel("Visualizations"):  
    "Visualizations of the Channel Islands"