import dropbox

class TransferData:

    def __init__(self,access_token):
        self.access_token= access_token

    def upload_files(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_from)
        
def main():
    access_token ='sl.BG7j2AJw1XuG5d92grFe0mLpmDR2pj4am0w8qe-7bdXhecQU0YPv1x-on99xcI0P8Qfvru07CVzGOYZ6gC2avvWYfUPUqoMSiF3ky5cuV7HyZhtJ4dELwCoADu0wI3icw8bzJss'
    transfer_data= TransferData(access_token)
    file_from = input("enter the path to transfer files")
    file_to = input("enter full path to upload to dropbox")
    transfer_data.upload_files(file_from,file_to)
    print("the file has been moved")


main()