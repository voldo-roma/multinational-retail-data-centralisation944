# Context 
This demo is set to replicate the core of data engineering / cloud engineering work for a multinational company that sells various goods across the globe.

## Problem statement: 
Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team.

In an effort to become more data-driven, your organisation wants to make it's sales data accessible from one centralised location.

Your first goal will be to produce a system that stores the current company data in a database so that it's accessed from one centralised location and acts as a single source of truth for sales data.

You will then query the database to get up-to-date metrics for the business.

# Approach and Ways of Working

In this project I'm using cloud Jira to capture requirements and to-dos transferred from the AiCore program to help with structure and implement Agile ways of working. 
* The project is limited to a single contributor, however the board consists of the standard Kanban workflow: TO DO, IN PROGRESS, REVIEW, and DONE. 
* Each milestone is turned into Epics while individual tasks are turned into blue Tasks or sub-tasks depending on the size of the ticket. 
![alt text](https://github.com/voldo-roma/multinational-retail-data-centralisation944/blob/MRDC944/aicore_jira_view_MRD.png?raw=true)

## How to navigate this repo:
This repository comprises scripts that all work together to perform data tasks. Namely, extract, clean, and upload - all within the same data pipeline:

* data_extraction.py: Defines DataExtractor for retrieving data from various sources, including APIs and RDS databases. It fetches raw data that might require cleaning or transformation before use.

* database_utils.py: Contains DatabaseConnector, which manages database connections, reads credentials, and interacts with the database for operations like listing tables and uploading data. It's pivotal for both initial data extraction and final data upload after cleaning.

* data_cleaning.py: Hosts DataCleaning, responsible for cleaning or transforming data fetched by DataExtractor. It ensures data quality.

* main.py: Orchestrates the workflow by using classes and methods from the other scripts. 
