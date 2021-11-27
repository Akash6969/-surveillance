import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img= cv2.imread('assets/qr.jpg')
# test=decode(img)
# print(test)
cap= cv2.VideoCapture(0)
cap.set(3,720)
cap.set(4,1080)


while True:
    success,img=cap.read()
    for barcode in decode(img):
        print(barcode.data)
        mydate=barcode.data.decode('utf-8')
        print(mydate)
        pts=np.array([barcode.polygon],np.int32)
        pts= pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(0,255,13),5)
        pts2=barcode.rect
        cv2.putText(img,mydate,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(13,76,98),1)
    cv2.imshow('win',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
            break    

    
    
    

    
  
  