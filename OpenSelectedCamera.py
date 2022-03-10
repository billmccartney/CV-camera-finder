# Setting CameraIp
import imp
from pymf import get_MF_devices
import cv2
import json
import threading

class CaptureThread(threading.Thread):
    def __init__(self,id,name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        video = cv2.VideoCapture(self.id, cv2.CAP_DSHOW)
        while (video.isOpened):
            ret, frame = video.read()
            if ret:
                cv2.imshow(self.name, frame)
                # Wait until a key is pressed.
                # Retreive the ASCII code of the key pressed
                k = cv2.waitKey(1) & 0xFF
                # Check if 'ESC' is pressed.
                if(k == 27):
                    # Break the loop.
                    break

            if (g_thread_exit_flag):
                break 

        # Release the VideoCapture object.
        video.release()

def SelectIpList(cameraName,ipList):
    index = 0
    print('Please choose the ip:',cameraName)
    for ip in ipList:
        print('{}:{}'.format(index,ip))
        index=index+1

    try:
        selectIndex = int((input('choose the number(default is 0):'.format(len(ipList) - 1))))
    except:
        selectIndex = 0

    return selectIndex

if __name__ == '__main__':
    fileUrl = 'cameraSetting.json'
    jsonData = {}
    ipList = []
    device_list = get_MF_devices()
    g_thread_exit_flag = False
    for i in range(len(device_list)):
        ipList.append(str(201+i))

    for cv_index, device_name in enumerate(device_list):
        g_thread_exit_flag = False
        cap = CaptureThread(cv_index, device_name) 
        cap.start()

        selectIndex = SelectIpList(device_name, ipList)

        while (selectIndex < 0 or selectIndex >= len(ipList)):
            selectIndex = SelectIpList(device_name,ipList)

        jsonData[ipList[selectIndex]] = cv_index
        ipList.remove(ipList[selectIndex])
        g_thread_exit_flag = True
        cap.join()

    with open(fileUrl, 'w') as f:
        print('write to {}-->'.format(fileUrl), jsonData)
        json.dump(jsonData, f)
        
    cv2.destroyAllWindows()