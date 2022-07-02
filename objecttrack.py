import cv2
import numpy as np
import time


tracker = cv2.TrackerKCF_create()

video = cv2.VideoCapture(0)

ok, frame=video.read()

bbox = cv2.selectROI(frame)

ok = tracker.init(frame, bbox)

while True:
    start = time.time()
    ok,frame=video.read()
    if not ok:
        break

    ok,bbox=tracker.update(frame)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x+w,y+h), (0, 255, 0), 2, 1)

    else:
        cv2.putText(frame,
                    'Error',
                    (100, 0),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255), 2)

    cv2.imshow('Tracking', frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

    end = time.time()

    fps = 1 / (end - start)

    print(round(fps))

cv2.destroyAllWindows()
