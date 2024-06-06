# Web Application for Channel Islands National Marine Sanctuary
Repository housing the code needed for the interactive web application. This is a capstone project for the [Master of Environmental Data Science at Bren School of Environmental Science and Management](https://bren.ucsb.edu), University of California, Santa Barbara. To access the web application, you can click [here](https://shinyapps.bren.ucsb.edu/channelislanders/)

Getting started
To get started with shiny follow the installation instructions or just install it from pip.

```
pip install shiny
```

The web application itself is hosued within the `app.py` document in the `myapp` folder.

## **Features:**

The user is recommended to navigate through each tab within the application in the following order:

## **About**

In this section, users have the opportunity to delve deeper into the project's details and discover the fundamental purpose behind the creation of the web application. Here, they can explore comprehensive information about the project's objectives, goals, and the underlying motivation driving the development of the application. This tab serves as a valuable resource for users seeking a clearer understanding of the project's scope and significance within its domain.

## **Data**

Due to the infrequency of the data utilized in this application for sanctuary management, this section will elaborate on the details of leveraging large ensemble climate models. It will specifically describe Community Earth System Model version 1 (CESM1.0) data and explore why these models are indispensable tools, offering insights into how they enhance our understanding of complex environmental dynamics and variability.

Although we sourced the data through Amazon Web Services, we created netCDF files for this web application in order to streamline the process of producing the outputs within the interactive visualization. Unfortunately the data is too large to include in the repository, so here is the link to the netCDF files produced. This is our [DRYAD](https://doi.org/10.5061/dryad.x0k6djht9) link.

## **Visualizations**

After navigating through the other tabs, the user will be able to view the visualizations, separated into three different panels that produce the plots. 
Time series contains two drop down menus where the user is able to select from different climate variables and statistic.
Vertical profiles and maps will show three drop down menus where the user will be able to select from climate variables, statistic, and experiments. 

## **Structure:**

The structure of the repository is as follows:
```
web_application
├── LICENSE
├── README.md
├── myapp
│   ├── README.md
│   ├── app.py
│   ├── ch_poster.jpg
│   ├── climate_model.jpeg
│   ├── data
│   │   └── cinms_py
│   │       ├── cinms_py.dbf
│   │       ├── cinms_py.html
│   │       ├── cinms_py.kmz
│   │       ├── cinms_py.prj
│   │       ├── cinms_py.sbn
│   │       ├── cinms_py.sbx
│   │       ├── cinms_py.shp
│   │       ├── cinms_py.shp.xml
│   │       ├── cinms_py.shx
│   │       └── cinms_py.xml
│   └── styles.css
└── requirements.txt
```

**myapp**: This folder contains the code as well as the data that is needed to run the app.

- app.py: This contains the code of how the website is built, the interactivity of the website, and the rendering of the plots that will be outputted in the website.
- cinms_py: This contains the shapefiles needed to create the Channel Island extent found on the mapping visualization tab.



### Contributors
Project manager: [Patricia Park](https://github.com/p-park6)

Communications manager: [Olivia Holt](https://github.com/olleholt)

Data Manager/ Product Leader: [Diana Navarro](https://github.com/dianaxnav)

Client/Faculty Advisor: [Samantha Stevenson](https://github.com/samanthastevenson)


## References for Data 

Office of National Marine Sanctuaries, [06/06/2024]: Channel Islands National Marine Sanctuary Boundary (polygons) [Data Date Range], https://www.fisheries.noaa.gov/inport/item/40040., Access Constraints: None, Use Constraints: NOT FOR LEGAL USE, Distribution Liability: Digital boundary files are available for public consumption from the Office of National Marine Sanctuaies in hard copy or digital formats. See Distributor Contact Informationfor contact details.
