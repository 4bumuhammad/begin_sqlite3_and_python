from googleapiclient.discovery import build
from google.oauth2 import service_account



SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('drive', 'v3', credentials=creds)

# results = service.files().list(fields="*", corpora='drive', supportsAllDrives=True, driveId="1g6IOzSdKce1KFA0mgD7IZKW35GZB2mRb", includeItemsFromAllDrives=True).execute()
# items = results.get('files', [])
# results = service.files().list(pageSize=5, fields="nextPageToken, files(id, name, mimeType, size, parents, modifiedTime)").execute()



response = service.files().list(q="mimeType='application/octet-stream'",
                                spaces='drive',
                                fields='nextPageToken, '
                                        'files(id, name)',
                                pageToken=None).execute()

items = response.get('files', [])

print(items)

print("Done")
