from picamera import PiCamera
from time import sleep

camera = PiCamera()

print("Hello there! We are going to take pictures")
num_pictures = int(input("How many pictures should we take? \n"))

camera.start_preview(alpha=255)
camera.rotation = 180
camera.annotate_text= f"We are going to take {num_pictures} pictures"
sleep(10)
for i in range(1,num_pictures+1):
    sleep(.5)
    camera.annotate_text= f"Picture: {i}"
    camera.capture(f'/home/pi/Desktop/Convolution_Exp/from_camera/camerarev2_{i}.jpg', resize=(100,100))
camera.stop_preview()

print("All done!")