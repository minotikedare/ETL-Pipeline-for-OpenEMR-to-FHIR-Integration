# ETL-Pipeline-for-OpenEMR-to-FHIR-Integration

Group 4 - Final Project 

## Project Overview

This project focuses on developing an **ETL (Extract, Transform, Load)** pipeline specifically designed for healthcare data. It leverages **Python** and the **FHIR API** to extract data from **OpenEMR**, transform it into the standardized **FHIR format**, and load it into a healthcare system. The primary goal of this project is to automate the process of extracting healthcare data, converting it to a standard format, and loading it into a system for analysis, ultimately improving **interoperability** in healthcare.

The ETL pipeline consists of three major steps:
1. **Extract**: Retrieve healthcare data from OpenEMR using the FHIR API.
2. **Transform**: Clean, map, and convert the data into the FHIR format to ensure consistency and standardization.
3. **Load**: Load the transformed data into a healthcare system for further analysis and use.

## Tools Used

This project utilizes the following technologies:
- **Python**: The core programming language used for developing the ETL pipeline, interacting with APIs, and processing data.
- **FHIR API**: A standardized protocol for exchanging healthcare data, enabling the extraction and loading of patient resources from systems like OpenEMR and Primary Care EHR.
- **SNOMED CT**: A clinical terminology server used to retrieve and standardize medical concepts for conditions.
- **OAuth 2.0**: A protocol for secure API authentication, managing access tokens for healthcare data access.
- **HL7apy**: A Python library used for generating HL7 v2 messages to ensure interoperability across healthcare systems.
- **JSON**: A data format for representing FHIR resources, including patient and condition information.
- **OpenEMR**: A system that stores patient details and conditions, serving as the data source.
- **Primary Care Website**: The target system where the transformed data from OpenEMR is loaded for further use.

## Project Architecture

The project architecture of the ETL pipeline for extracting, transforming, and loading healthcare data:
![Project Architecture](https://github.com/minotikedare/ETL-Pipeline-for-OpenEMR-to-FHIR-Integration/blob/main/images/project_architecture.png?raw=true)

## Project Website

For more details, documentation, and to explore the project's workflow, visit the project website here:  
[ETL Final Project Website](https://pages.github.iu.edu/shurmad/group4_health_info_standards/) 

