import os
import pandas as pd
import requests
from google.cloud import bigquery

# =========================
# Config
# =========================
PROJECT_ID = "conductive-bot-480110-g0"
DATASET = "analytics"
TABLE = "customer"

HUBSPOT_API_KEY = ""
HUBSPOT_URL = "https://api.hubapi.com/crm/v3/objects/contacts"

HEADERS = {
    "Authorization": f"Bearer {HUBSPOT_API_KEY}",
    "Content-Type": "application/json"
}

# =========================
# 1. Extract from BigQuery
# =========================
def extract_from_bigquery():
    client = bigquery.Client(project=PROJECT_ID)
    query = f"""
        SELECT
            email,
            first_name,
            last_name,
            phone,
            company
        FROM `{PROJECT_ID}.{DATASET}.{TABLE}`
        WHERE email IS NOT NULL
    """
    df = client.query(query).to_dataframe()
    return df


# =========================
# 2. Transform
# =========================
def transform(df):
    df = df.drop_duplicates(subset=["email"])
    df["first_name"] = df["first_name"].fillna("")
    df["last_name"] = df["last_name"].fillna("")
    return df


# =========================
# 3. Load to HubSpot
# =========================
def load_to_hubspot(df):
    for _, row in df.iterrows():
        payload = {
            "properties": {
                "email": row["email"],
                "firstname": row["first_name"],
                "lastname": row["last_name"],
                "phone": row["phone"],
                "company": row["company"]
            }
        }

        response = requests.post(
            HUBSPOT_URL,
            headers=HEADERS,
            json=payload
        )

        if response.status_code not in (200, 201):
            print(f"❌ Failed for {row['email']} → {response.text}")
        else:
            print(f"✅ Synced {row['email']}")


# =========================
# Run Pipeline
# =========================
def run_pipeline():
    print("🚀 Extracting from BigQuery...")
    df = extract_from_bigquery()

    print("🔧 Transforming data...")
    df = transform(df)

    print("📤 Loading to HubSpot...")
    load_to_hubspot(df)

    print("🎉 Pipeline finished successfully")


if __name__ == "__main__":
    run_pipeline()
