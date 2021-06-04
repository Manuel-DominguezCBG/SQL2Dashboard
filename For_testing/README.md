
# A short personal reflections of what I have learn in this project
****

<b>Table of contents</b><br>

1. [Data quality managements](#Data)

2. [What is a good database design](#bases)


<a id="Data"></a>

### Data quality managements
This training project has allowed me to understand the importance of ensuring  that the results shows in the dashboard are faithful to the data contained in the database. When we are called to analyse and display data, users (medical staff or executives) will not look at the accuracy of our procedure. In a clinical context, wrong decisions can be made from errors in the representation or analysis of the data having as consequence a negative impact in the patient. So as bioinformaticians we are responsable for data quality management.

For that reason I have wanted to ensure that the data display is correct. To do that and also discover defects or bugs in the software I have applied some tests. The idea is quite simple but put this into practice is very complicate especially for someone who has not applied testing in software development before.

Reading about this I have learnt that many steps can be made to solve this.

1. Identification of right data sources. In this learning project mistakes in the selection of the data (for example taking Covid data from Spain instead of the UK) would provide a different output in the graphics. Incorrect data may result from migration of data from one database to another, presence of incorrect values, or even time-bound data changes. It is important to identify the cause and fix it.

2. Reviewing is an efficient way to check the correctness of the data. That is in fact what I have tried to do by appliying the tests.

3. No applied in this learning project but in real scenarios I have reading about

    * Secure and reliable systems for data storage, backups, and transfers

    * Documented processes to reduce human error

    * Adherence to data protection regulations such as GDPR

    * Check constraints to require new data to be inputted in a certain form

Apart from all informatic skill in computing and databases manipulation, I have gained a better understanding of the importance of this and I will be aware in the future if I need to work with real databases



<a id="bases"></a>

### What is a good database design

A great proportion of the time spent in this project has been related to the creation of databases. Before I did that I wanted to know more about this because I haven´t done this before. I show here some important ideas that I will remember:

* A good database does not have to have duplicate information (redundant data). This is because it waste space and increse the likehhod of errors and inconsistencies. In my project, to avoid this I spent time thinking on how divide the information into subject-based tables to reduce repetition. I have also specify primary keys to uniquely identify each row and set up the table relationship.


* The correctness and the completeness of information are important. If our database contains incorrect information, any report (ie. the dashboard) that pulls information from the database very probably will show incorrect information. In clinical context misinformed report might have a negative impact in the health of our patients.

* Normalization rules. To see if my tables are structure correctly I have learned this through the errors that SQL reported to me when for instance I wanted to select one column as the primary key when this column had duplicate tuples. I have understood what is an atomic value and the advantages and disadvantages of unnormalized form over normalized. I have not applied the 11 normalizations steps I have found in the literature because my databases created here are not complex enough to applied this but I am aware of this for future projects.


