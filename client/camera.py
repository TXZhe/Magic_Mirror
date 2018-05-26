import picamera
import time

camera = picamera.PiCamera()

class Camera:
    '''
    def __init__(self):
        camera = picamera.PiCamera()
    '''

    def take_photo_to_file(self, num):
        camera.brightness=60
        camera.rotation=270
        camera.resolution=(720, 1280)
        time.sleep(0.5)
        camera.exif_tags['IFDO.Artist']='Magic Mirror'
        camera.capture("/home/capstone/magic_mirror/client/" +str(num)+".jpg")
        #camera.start_preview()

if __name__ == '__main__':
    test = Camera()
    for i in range(5):
        test.take_photo_to_file(i)
