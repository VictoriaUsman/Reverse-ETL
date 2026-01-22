
<img width="1556" height="776" alt="F5A09B30-8503-406B-B117-CEB7AB1019FB" src="https://github.com/user-attachments/assets/39e6f613-81ee-42c9-9c64-17f95484e23e" />
<img width="1968" height="596" alt="438468B0-59DB-4A15-9DC9-5AB9F70E04F8" src="https://github.com/user-attachments/assets/9e017c22-aeb1-4b95-b597-c30bae5abf89" />
<img width="2938" height="1536" alt="5F40420D-C325-4CBB-840E-A8F3AAF3E8BF" src="https://github.com/user-attachments/assets/321c266a-7eb1-471c-9f7a-d93b790993a7" />

BigQuery to HubSpot Data Sync Pipeline
📌 Overview

This project implements a data integration pipeline that extracts data from Google BigQuery, processes it using Python, and loads it into HubSpot CRM.
The pipeline is designed to be cloud-deployable, scalable, and easy to automate.

It is ideal for syncing analytics or operational data from BigQuery into HubSpot for sales, marketing, or customer insights.

🏗 Architecture
BigQuery  →  Python ETL (Cloud Service)  →  HubSpot CRM

Flow Description

BigQuery

Acts as the source of truth for analytical or processed data

Can contain customers, transactions, leads, or metrics

Python ETL Service

Extracts data from BigQuery

Transforms/cleans data (formatting, mapping, validation)

Sends data to HubSpot using HubSpot APIs

Can be deployed on cloud services (Cloud Run, VM, ECS, Lambda, etc.)

HubSpot CRM

Receives data as contacts, companies, deals, or custom objects

Keeps CRM data in sync with the data warehouse

☁️ Deployment Options

The Python service can be deployed to:

GCP Cloud Run

AWS Lambda / ECS

Azure Functions

Docker container on any VM

On-prem scheduler (cron)

🛠 Tech Stack

Python 3.x

Google BigQuery

HubSpot API

Cloud Services (GCP / AWS / Azure)

Optional: Docker, Scheduler (cron, Dagster, Airflow)

📂 Project Structure (example)
.
├── src/
│   ├── extract.py      # BigQuery extraction
│   ├── transform.py    # Data cleaning & mapping
│   ├── load.py         # HubSpot API loader
│   └── main.py         # Pipeline runner
├── config/
│   └── settings.yaml
├── requirements.txt
├── Dockerfile
└── README.md

🔐 Authentication
BigQuery

Uses Service Account JSON

Set GOOGLE_APPLICATION_CREDENTIALS

HubSpot

Uses Private App Access Token

Stored as environment variable:

HUBSPOT_ACCESS_TOKEN=your_token_here

🚀 How to Run Locally
pip install -r requirements.txt
python src/main.py

⏰ Automation

This pipeline can be scheduled using:

Cron jobs

Dagster

Cloud Scheduler

Airflow (optional)

GitHub Actions

📈 Use Cases

Sync customers from BigQuery to HubSpot

Push analytics results to CRM

Update deal properties automatically

Enrich CRM with warehouse data

🔄 Future Improvements

Add retry & error handling

Incremental loads

Logging & monitoring

Schema validation

CI/CD deployment

👨‍💻 Author

Ian Tristan
Data Engineer



