import pickle
import os.path as path

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://mail.google.com/'] # Scope for total control of your gmail account

def __get_credentials(fsecrets, ftoken=None):
    creds = None
    flow = InstalledAppFlow.from_client_secrets_file(
    fsecrets,
    scopes=SCOPES)
    if not ftoken == None:
        if path.exists(ftoken):
            with open(ftoken, 'rb') as token:
                creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                fsecrets, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(ftoken, 'wb') as token:
            pickle.dump(creds, token)
        
    service = build('gmail', 'v1', credentials=creds)
    return service
if __name__ == '__main__':
    print('ERROR: This script cannot be run directly')
    print('WARNING: The direct execution of this script is strongly discouraged')