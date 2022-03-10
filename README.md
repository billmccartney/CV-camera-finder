# CV-camera-finder

A simple function to find a connected camera list with media foundation. This is just a modified code of a sample found in https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/multimedia/mediafoundation/MFCaptureToFile to use in python.

If you are looking for a function with Directshow, see https://www.codeproject.com/Articles/1274094/Capturing-Images-from-Camera-using-Python-and-Dire.

If you want to modify it, edit cpp files and rebuild it. 

You can use it to match opencv index with camera path.

------------------------------------------
Dependency: Visual C++ Redistributable 2019

You can download it here: https://support.microsoft.com/ko-kr/help/2977003/the-latest-supported-visual-c-downloads

Tested Env: windows10, python3.9.6

simple example
``` python
from pymf import get_MF_devices
device_list = get_MF_devices()
for i, device_name in enumerate(device_list):
    print(f"opencv_index: {i}, device_name: {device_name}")

=> opencv_index: 0, device_name: Integrated Webcam
```

simple example with opencv
``` python
from pymf import get_MF_devices
import cv2

device_list = get_MF_devices()
cv_index = None
for i, device_name in enumerate(device_list):
    # find index of camera you want
    q = input(f"Wanna use {device_name}?\n")
    if q.strip() == "YES":
        cv_index = i
        break

if cv_index is None:
    print("Not found")
else:
    # make sure you use Media Foundation
    cap = cv2.VideoCapture(cv_index + cv2.CAP_MSMF)
    while (cap.isOpened):
        ret, frame = cap.read()
        if ret:
            cv2.imshow("frame", frame)
            k = cv2.waitKey(1)
            if k > 0:
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
```

OpenSelectedCamera.py(build the map of Id with Ip one by one, at the same time you can see the cameraview)
Please choose the ip: \\?\usb#vid_18ec&pid_3399&mi_00#6&213c80e0&1&0000#{e5323777-f976-4f5b-9b55-b94699c46e44}\global
0:201
1:202
choose the number(default is 0):
Please choose the ip: \\?\usb#vid_046d&pid_08e4&mi_00#6&203ec69b&0&0000#{e5323777-f976-4f5b-9b55-b94699c46e44}\global
0:202
choose the number(default is 0):
write to cameraSetting.json--> {'201': 0, '202': 1}

