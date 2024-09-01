import torch
import numpy as np
import cv2
path = 'bestn.pt'
model = torch.hub.load('ultralytics/yolov5','custom',path,force_reload=True)
cap = cv2.VideoCapture(0)


while True:
    ret,frame = cap.read()
    frame = cv2.resize(1280,720)
    results = model(frame)
    frame = np.squeeze(results.render())
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
    
cap.release()
cv2.destroyAllWindows()