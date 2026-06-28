import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials



def getcredentials():
    if os.path.isfile("token.json"):
        creds = Credentials.from_authorized_user_file("token.json")
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        return creds
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "client_secret.json", 
            scopes=["https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly"]
            )   
        creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
        return creds
