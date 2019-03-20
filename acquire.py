from picamera import PiCamera
from time import sleep
from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
import datetime
import os

# Setting Parameters

ACCOUNT_NAME = "coffeemonitor"

ACCOUNT_KEY = "JELAV+MyTbiKW3iTWN5cwG6Z09gYsAAFrwfIqhnkI2NViuW6uI1PpCEHWf2Q2O2T4aUMNNwg9vepvBYtvPeSOA=="

CONTAINER_NAME = "devimages"


blob_service = BlockBlobService(account_name=ACCOUNT_NAME, account_key=ACCOUNT_KEY)

try:
    camera = PiCamera()
    #camera.rotation = 180
    #camera.start_preview(fullscreen=False, window = (100, 20, 640, 480))
    while True:
        local_file_name = 'coffee{date:%Y%m%d%H%M%S}.jpg'.format( date=datetime.datetime.now() )
        full_path_to_file = '/home/pi/Desktop/%s' % local_file_name
        camera.capture(full_path_to_file)
        sleep(2)
        blob_service.create_blob_from_path(CONTAINER_NAME, local_file_name, full_path_to_file)
        #camera.stop_preview()
        print('Pushed %s to blob storage' % local_file_name);
        os.remove(full_path_to_file)
        sleep(30)
        
except Exception as e:
    #camera.stop_preview()
    s = str(e)
    print(s)
