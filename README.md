# Web Application for Channel Islands variable observations
Repository housing the code needed for the interactive web application. This is a capstone project for the [Master of Environmental Data Science at Bren School of Environmental Science and Management](https://bren.ucsb.edu), University of California, Santa Barbara.

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

## **Visualizations**

After navigating through the other tabs, the user will be able to view the visualizations, separated into three different panels that produce the plots. 
Time series contains two drop down menus where the user is able to select from different climate variables and statistic.
Vertical profiles and maps will show three drop down menus where the user will be able to select from climate variables, statistic, and experiments. 




## **Structure:**

The structure of the reposotory is as follows:
```
web_application
│   README.md
│  .gitignore
|  LICENSE
|  requirements.txt
|  sheephead-kelp-forest.jpg
└───myapp
      │ app.py
      │ plots.py
      │ requirements.txt
      │ shared.py
      │ styles.css
      │ time_series_1990_2000_o2.nc
      │ time_series_1990_2000_salt.nc
      │ time_series_1990_2000_temp.nc
      │ time_series_temp_o2.nc
      │ time_series_temp_test.nc
└───images
      |  sheephead-kelp-forest.jpg
```


### Contributors
Project manager: [Patricia Park](https://github.com/p-park6)

Communications manager: [Olivia Holt](https://github.com/olleholt)

Data Manager/ Product Leader: [Diana Navarro](https://github.com/dianaxnav)

Client/Faculty Advisor: [Samantha Stevenson](https://github.com/samanthastevenson)
