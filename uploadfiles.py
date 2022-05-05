import dropbox 
import os

class transferdata :
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken

    def uploadfile (self,file_from,file_to) :
        db=dropbox.Dropbox(self.accesstoken)
        f=open(file_from,'rb')
        db.files_upload(f.read(),file_to)

        for root,dirs,files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root,filename)
            relative_path=os.path.relpath(local_path,file_from)
            dropbox_path=os.path.join(file_to,relative_path)
            with open(local_path,'rb') as f:
                db.files_upload(f.read,dropbox_path,mode=WriteMode('overwrite'))


def main():
    token='sl.BG6ujmu_YzzpHoGASNYJSawiaAOzPqZ9R_ic9QVE3FI-Sq8669QZ3BdnM3XV02GM4Fe2Zu7XEuJW7I9TghDVjITYZxN98hNq7Lvo9GaNJvurYmTEIMiMhpOGIP57sn2yelzshrVwQkoe'
    tran=transferdata(token)
    file_from=input('enter the file to be transfered')
    file_to=input('enter the path where you want to transfer')
    tran.uploadfile(file_from,file_to)
    print('file has been moved!')
    
main()