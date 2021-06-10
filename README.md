
# SQL2Dashboard
****

## Working with databases and dashboards
This project aims to learn about computing in a clinical context and overcome some of the competencies of the module **Computing for Clinical Scientists**.
This work has been split into 3 main tasks/folders:

1. Folder **Covid-19**. Creation of a database and an interactive dashboard.
From datasets with Covid-19 data taken from [GOV.UK](https://coronavirus.data.gov.uk/)
a database has been created. With this database, a dashboard have designed using the library [Dash](https://dash.plotly.com/)
To allow the user to interact with the data, the design contained 2 callbacks at the top (see picture below)
in which use can select a period of time. After this, the dashboard shows covid-19 data in that selected period.
More specifically  the dashboard returns in 5 cards:

  1. The number of people vaccinated,
  2. People tested positive,
  3. Deaths within 28 days of positive test, 
  4. Patients admitted.
  
Additionally, the dashboard shows 4 graphs:

  1. A line chart showing the number of people vaccinated per day. Plot allows to filter the info by regions and do zoom in or out. Under the plot, it can be seen two buttons, one that shows the data in a table and a second that allows the user to download the data.
  2. A bar chart that shows accumulative data of people vaccinated. That is, the total number of people vaccinated since the covid vaccination program began.
  3. A pie chart showing the proportion of people vaccinated and non vaccinated in the total UK population
  4. A line chart that shows the trends of  people admitted in hospitals and deaths people by covid. 

![Alt text](https://github.com/Manuel-DominguezCBG/SQL2Dashboard/blob/main/Covid-19/Images/1.png "")


Note: If you find difficulties opening the notebooks, please used this website [nbviewer](https://nbviewer.jupyter.org/)

The content of this folder:
```sh
├── COVID-19_data_to_dashboard.ipynb                 # A JN where I explain how to create a database from CSV files
├── Data                                             # All data used to create this  COVID_19.db database
│ ├── COVID_19.db                                    # The database
│ ├── Deaths_within_28_days_of_positive.csv          # The datasets used to populate the database:
│ ├── Patients_admitted_to\ hospital.csv
│ ├── People_tested\ positive.csv
│ ├── People_vaccinated.csv
│ ├── UK_total_cases.csv
│ ├── Virus_tested.csv
│ └── vaccinated_regions.csv
├── Images                                            # Some images for the notebooks
│ ├── screen.jpg
│ ├── screenshot-aca1dabf.png
│ └── screenshot-aca1dwwabf.jpg
├── assets                                            # This folder is needed to design the dashboard
│ ├── linkedin-logo2.png
│ ├── logo_hospital.png
│ └── wrgllogohighres.png
├── db2dashboard.py                                    # The script to created the dashboard
└── tutorial.zip                                       # Many drafts and tutorial used to learn
```

2.  Folder **Fake_database** Regardless of what has been done previously, a fake data database has been created contained 4 linked tables.

The structure of the database looks like this: 

![Alt text](https://github.com/Manuel-DominguezCBG/SQL2Dashboard/blob/main/Covid-19/Images/1.png "")


In this simulation, 200000 people are stored in the table *Patient data*. 5% of these people got Covid and need to go to the hospital, *Covid-19 admission* table.
A 5% of these patients died, *Covid-19_deaths*. Finally, the last table contains info with regard to the properties of the 41 hospitals created in this simulated database.

For details of how this has been carried out, go to the Jupyter Notebook *1_Creating_the_fake_database.ipynb*. 

Then in a second Notebook (*2_Database_manipulation.ipynb*) I show the use of the most basic SQL command such as JOIN, GROUPBY among others. 
Finally, in the script *Fake_db2dashboard.py* I have combined all skills learned during the project to create a second dashboard that shows some results of this database. 

A screenshot of this dashboard
![Alt text](https://github.com/Manuel-DominguezCBG/SQL2Dashboard/blob/main/Covid-19/Images/2.png "")

The content of this folder:
```sh
├── 1_Creating_the_fake_database.ipynb                  # Where I have created the fake data and create the database
├── 2_Database_manipulation.ipynb                       # To become familiar with SQL commands (a personal tutorial)
├── 2fake_db.db                                         # The database 
├── Fake_db2dashboard.py                                # The script to created the dashboard
├── assets
│ ├── linkedin-logo2.png
│ ├── logo_hospital.png
│ └── wrgllogohighres.png
└── tutorials.zip                                        # More draft code and tutorial to practice
```


3. Folder **Testing**
In this section, I have built a WebPageTest using [Python](https://blog.testproject.io/2019/05/16/python-testing-framework-pros-cons/), [pytest](https://blog.testproject.io/2019/07/16/python-test-automation-project-using-pytest/), and [Selenium WebDriver](https://blog.testproject.io/2017/11/28/inside-selenium-webdriver/).

What I have done is to ensure that the information provided by the dashboard is accurate with respect to the data contained in the dashboard. Text, buttons, data input and data output have been tested. Details of this and an explanation of how to run the automatization test can be found in the script  *test_db2dashboard.py*. 

To run the tests go to  the directory SQL2Dashboard/Testing write ```pipenv run python -m pytest```

The results of the tests carried out are shown below.

```sh
**====================================== test session starts =======================================**
platform darwin -- Python 3.8.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /Users/monkiky/.local/share/virtualenvs/python-webui-testing-JXNJ2lAn/bin/python
cachedir: .pytest_cache
rootdir: /Users/monkiky/Desktop/SQL2Dashboard/For_testing/python-webui-testing
**collected 4 items**
tests/test_db2dashboard.py::test_text PASSED
tests/test_db2dashboard.py::test_buttons PASSED
tests/test_db2dashboard.py::test_dates PASSED
tests/test_db2dashboard.py::test_card_values PASSED
======================================= **4 passed** in 28.68s =======================================
```
The content of this folder:
```sh
├── README.md                                           # Some personal reflections that are arised during and after the work of this project 
├── Pipfile
├── Pipfile.lock
├── chromedriver                                        # Needed for Selenium to automatized the tests
├──Test
│ ├── test_db2dashboard.py                              # The code of the tests
│ ├──  __pycache__
│ ├── assets
```
