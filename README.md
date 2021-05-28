
# SQL2Dashboard
****

## Working with databases and dashboards
This project aims to learn about computing in a clinical context and overcome some of the competencies of the module **Computing for Clinical Scientists**. This work has been split into 4 main tasks/folders:
1. Folder **Covid-19**. Creation of a database and an interactive dashboard.From datasets with Covid-19 data, I have created a simple database. With this database, I have designed a dashboard.  To allow the user to interact with the data, the design contained 2 two callbacks at the top (see picture below) in which the user can select a period of time. After this, the dashboard provides covid-19 data in the selected period. More specifically what the dashboard returns in 5 cards are the number of people vaccinated, people who were tested positive, death of people who were tested positive up to 28 days before death, and the number of patients admitted in hospitals.
Additionally, the dashboard shows 4 graphs. The first is a line chart and shows the number of people vaccinated per day by the 4 regions of the UK. In this plot, the user can select what regions he wants to show in the plot and can zoom in or out. Behind the plot, there are two buttons, one that shows the data in a table and a second that allows the user to download the data. The second graph is a bar chart that shows people vaccinated accumulative data. That is, the total number of people vaccinated since the covid vaccination program began but only showing these data in the period of time selected by the user. The third one is a pie chart that shows the proportion of people vaccinated in the total UK population.  The last plot is a line chart that shows the relationship between people admitted and deaths people by covid or its consecuenses. 

![Alt text](https://github.com/Manuel-DominguezCBG/SQL2Dashboard/blob/main/Covid-19/Images/db2dashboard.png "")

The content of this folder:
```sh
├── COVID-19_data_to_dashboard.ipynb                 # A JN where I explain how to create a database from CSV files
├── Data                                             # All data used to create this  COVID_19.db database
│ ├── COVID_19.db
│ ├── Deaths_within_28_days_of_positive.csv
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

2.  Folder **Fake_database** A fake data database has been created contained 4 linked tables in order to work and get familiar with SQL commands. . Briefly I have populated the first table with people data (NHS number, name, gender...). In this simulation, 5% of these people got Covid and needed to be admitted to hospitals, this information has been store in a second table. This table has the patient ID, the hospital where each patient was admitted (41 in total, one per county) plus additional data such as date of admission and discharge. A 5% of these patients died, this info has been saved in another table. And finally the last table with some properties of these 41 hospitals such as the number of beds, staff and so on. For details of how this has been carried out, go to the Jupyter Notebook *1_Creating_the_fake_database.ipynb*. Then in a second Notebook (*2_Database_manipulation.ipynb*) I show the use of the most basic SQL command such as JOIN, GROUPBY and so on. Finally, in a script *Fake_db2dashboard.py* I have combined all these skills to show in a dashboard some results from the different tables of the database. 

A screenshot of this dashboard
![Alt text](https://github.com/Manuel-DominguezCBG/SQL2Dashboard/blob/main/Covid-19/Images/second_dashboard.png "")

And the content of this table
```sh
├── 1_Creating_the_fake_database.ipynb # Where I have created the fake data and create the database
├── 2_Database_manipulation.ipynb  # To become familiar with SQL commands
├── 2fake_db.db  # The database 
├── Fake_db2dashboard.py # The script to created the dashboard
├── assets
│ ├── linkedin-logo2.png
│ ├── logo_hospital.png
│ └── wrgllogohighres.png
└── tutorials.zip # More draft code and tutorial to practice`
