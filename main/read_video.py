import cv2
from darkflow.net.build import TFNet
import numpy as np
import time

import tensorflow as tf
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.InteractiveSession(config=config)

option = {
    'model': 'cfg/tiny-yolo-voc-3c.cfg', #'cfg/v1.1/tiny-yolov1.cfg' 'cfg/tiny-yolo-voc-2c.cfg'
    'load': -1, #'bin/tiny-yolo-v1.1.weights'
    'threshold': 0.3,
    'gpu': 0.7
}

tfnet = TFNet(option)

capture = cv2.VideoCapture('gun1.mp4')
colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

while (capture.isOpened()):
    stime = time.time()
    ret, frame = capture.read()
    if ret:
        #frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
        frame = cv2.resize(frame, (700, 500))
        results = tfnet.return_predict(frame)
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            print(label, result['confidence'])
            frame = cv2.rectangle(frame, tl, br, color, 7)
            frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow('frame', frame)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        capture.release()
        cv2.destroyAllWindows()
        break
