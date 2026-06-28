import streamlit as st 
from auth import getcredentials
from googleapiclient.discovery import build
import datetime

creds = getcredentials()
#service = build("fitness", "v1", credentials=creds)


today = datetime.date.today()
four_weeks_ago = today - datetime.timedelta(weeks=4)

# Google Fitness API needs time in milliseconds since epoch, not a date object
today_ms = int(today.strftime("%s")) * 1000
four_weeks_ago_ms = int(four_weeks_ago.strftime("%s")) * 1000

""" sessions = service.users().sessions().list(
    userId="me",
    startTime=four_weeks_ago.isoformat() + "T00:00:00Z",
    endTime=today.isoformat() + "T23:59:59Z",
).execute() """

import requests

headers = {"Authorization": f"Bearer {creds.token}"}
response = requests.get(
    "https://health.googleapis.com/v4/users/me/dataTypes/distance/dataPoints",
    headers=headers
)
st.write(response.status_code)
st.write(response.json())

#st.write(sessions)