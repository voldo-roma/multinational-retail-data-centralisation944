# Context 
This demo is set to replicate the core of data engineering / cloud engineering work for a multinational company that sells various goods across the globe.

## Problem statement: 
Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team.

In an effort to become more data-driven, your organisation wants to make it's sales data accessible from one centralised location.

Your first goal will be to produce a system that stores the current company data in a database so that it's accessed from one centralised location and acts as a single source of truth for sales data.

You will then query the database to get up-to-date metrics for the business.

# Ways of Working

In this project I'm using cloud Jira to capture requirements and to-dos transferred from the AiCore program to help with structure and implement Agile ways of working. 
* The project is limited to a single contributor, however the board consists of the standard Kanban workflow: TO DO, IN PROGRESS, REVIEW, and DONE. 
* Each milestone is turned into Epics while individual tasks are turned into blue Tasks or sub-tasks depending on the size of the ticket. 
![alt text](https://github.com/voldo-roma/multinational-retail-data-centralisation944/blob/MRDC944/aicore_jira_view_MRD.png?raw=true)

=======
# Solution

***Data sources***
1. card_details.pdf
2. __
3. __

***Scripts:*** 
* data_extraction.py
  - DataExtractor within it works as a utility class, it creats methods that help extract data from different data sources. The methods contained will be fit to extract data from CSV files, an API and an S3 bucket.
* database_utils.py
  - DatabaseConnector class within will be used to connect with and upload data to the database.
* data_cleaning.py
  - contains the class DataCleaning with methods to clean data from each of the data sources.
* main.py - Orchestrates the workflow by using classes and methods from the other scripts. 
