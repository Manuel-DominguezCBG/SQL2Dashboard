
# SQL2Dashboard
****

## Working with databases and dashboards

  

This project aims to learn about computing in a clinical context and overcome some of the competencies of the module ** Computing for Clinical Scientists **. This work has been split into 4 main tasks/folders:

  

1. Folder **Covid-19**. Creation of a database and an interactive dashboard.From datasets with Covid-19 data, I have created a simple database. With this database, I have designed a dashboard.  To allow the user to interact with the data, the design contained 2 two callbacks at the top (see picture below) in which the user can select a period of time. After this, the dashboard provides covid-19 data in the selected period. More specifically what the dashboard returns in 5 cards are the number of people vaccinated, people who were tested positive, death of people who were tested positive up to 28 days before death, and the number of patients admitted in hospitals.
Additionally, the dashboard shows 4 graphs. The first is a line chart and shows the number of people vaccinated per day by the 4 regions of the UK. In this plot, the user can select what regions he wants to show in the plot and can zoom in or out. Behind the plot, there are two buttons, one that shows the data in a table and a second that allows the user to download the data. The second graph is a bar chart that shows people vaccinated accumulative data. That is, the total number of people vaccinated since the covid vaccination program began but only showing these data in the period of time selected by the user. The third one is a pie chart that shows the proportion of people vaccinated in the total UK population.  The last plot is a line chart that shows the relationship between people admitted and deaths people by covid or its consecuenses. 

```
![Alt text](https://github.com/Manuel-DominguezCBG/SQL2Dashboard/blob/main/Covid-19/Images/Screenshot%202021-05-28%20at%2009.14.46.png "Optional title")
```

The content of this folder can be seen here:
```sh
├── COVID-19_data_to_dashboard.ipynb  # A JN where I explain how to create a database from CSV files
├── Data  # All data used to create this  COVID_19.db database
│ ├── COVID_19.db
│ ├── Deaths_within_28_days_of_positive.csv
│ ├── Patients_admitted_to\ hospital.csv
│ ├── People_tested\ positive.csv
│ ├── People_vaccinated.csv
│ ├── UK_total_cases.csv
│ ├── Virus_tested.csv
│ └── vaccinated_regions.csv
├── Images # Some images for the notebooks
│ ├── screen.jpg
│ ├── screenshot-aca1dabf.png
│ └── screenshot-aca1dwwabf.jpg
├── assets # This folder is needed to design the dashboard
│ ├── linkedin-logo2.png
│ ├── logo_hospital.png
│ └── wrgllogohighres.png
├── db2dashboard.py # The script to created the dashboard
└── tutorial.zip  # Many drafts and tutorial used to learn
```
