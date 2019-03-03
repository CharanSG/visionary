import cv2

# cv2.namedWindow("preview")
# vc = cv2.VideoCapture(0)
#
# if vc.isOpened():
#     rval, frame = vc.read()
# else:
#     rval = False
#
# while rval:
#     cv2.imshow("preview", frame)
#     rval, frame = vc.read()
#     key = cv2.waitKey(20)
#     if key == 27:
#         break
#
# cv2.destroyWindow("prevew")
# vc.release()

camera_port = 0
# ramp_frames = 30
# camera = cv2.VideoCapture(camera_port)
# def get_image():
#     retval, im = camera.read()
#     return im
#
# for i in range(ramp_frames):
#     temp = camera.read()
#
# camera_capture = get_image()
# filename = "capture.jpeg"
# cv2.imwrite(filename, camera_capture)
# del(camera)

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()

# for videos

# camera = cv2.VideoCapture(0)
#
# if(camera.isOpened() == False):
#     print("Error opening video file")
#
# while(camera.isOpened()):
#     ret, frame = camera.read()
#     if ret == True:
#         cv2.imshow('Frame', frame)
#
#         if(cv2.waitKey(25) & 0xFF == ord('q')):
#             break
#
#     else:
#         break
#
# camera.release()
#
# # Save the video
# import numpy as np
#
# camera1 = cv2.VideoCapture(0)
#
# if(camera1.isOpened() == False):
#     print("Unable to read camera")
#
# frame_width = int(camera1.get(3))
# frame_height = int(camera1.get(4))
#
# out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
#
# while(True):
#     ret, frame = camera1.read()
#
#     if ret == True:
#         out.write(frame)
#         cv2.imshow('frame', frame)
#
#         if(cv2.waitKey(1) & 0xFF == ord('q')):
#             break
#
#     else:
#         break
#
# camera1.release()
# out.release()
# cv2.destroyAllWindows()