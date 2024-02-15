from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gouth = GoogleAuth()
drive = GoogleDrive(gouth)

folder = "1fZzlfzZFYE-9pAFxoH5VclY8S-C1nT54"

file1 = drive.CreateFile({'parents':[{'id': folder}], 'title': 'hello.txt'})
file1.SetContentString('Hello world!')
# file1.SetContentFile()
# file1.Upload()
