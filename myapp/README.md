## Contents available in the myapp folder:

**cinms_py**: This folder holds all the shapefiles that are used to outline the Channel Islands on the mapping visualization. Packages such as `geopandas` are able to extract and effectively read and decipher these files.

**(data folder)**: This folder holds all the files needed to create the visualizations. These datasets are in .nc format and are subsetted to the Channel Islands from the CESM dataset.

**app.py**: This file holds all the code that is used to create the webpage. Included here is how user can call in the data, the different choices created for the user to choose from, creating the layout of the website, creating the interactivity of the website, and rendering the plots to show up on the visualization tab. All syntax were sourced from the [Shiny for Python](https://shiny.posit.co/py/) webpage.

**ch_poster.jpg**: An image of the Channel Island that is featured on the About's page.

**climate_model.jpeg**: An image of a climate model that is featured on the Data page.

**styles.css**: A file that holds the style type of the webpage.
