import cv2
import os
import time
import threading

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
rtsp="rtsp://admin:admin@14.241.209.185:555/ucast/11"
rtsp1="rtsp://admin:admin@14.241.209.169:554/ucast/11"
rtsp2="rtsp://admin:admin@14.241.209.175:554/ucast/11"

def getPicture(url,id):      

    cam = cv2.VideoCapture(url)

    while True:        
        ret, frame = cam.read()
        if not ret:
            print("mat ket noi")
            break
        print(frame)
        small_frame = cv2.resize(frame, (100,100))
        #small_frame = cv2.cvtColor(small_frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("camera"+str(id),small_frame)

        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break

    # When everything done, release the video capture object
    cam.release()


        # Closes all the frames
    cv2.destroyAllWindows() 

if __name__ == '__main__':
    getPicture(rtsp,1)
    # t1 = threading.Thread(target=getPicture, args=(rtsp,1,))
    # #t2 = threading.Thread(target=getPicture, args=(rtsp1,2,))

    # t1.start()
    #t2.start()