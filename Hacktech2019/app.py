from flask import Flask, request, redirect, render_template, url_for
from final1 import hacktech
import cv2
import matplotlib.pyplot as plt
app = Flask(__name__)


# def capture_image():
#     camera_port = 0
#     ramp_frames = 30
#     camera = cv2.VideoCapture(camera_port)
#
#     def get_image():
#         retval, im = camera.read()
#         return im
#
#     for i in range(ramp_frames):
#         temp = camera.read()
#
#     camera_capture = get_image()
#     filename = "capture1.jpeg"
#     cv2.imwrite(filename, camera_capture)
#     del (camera)

    # cam = cv2.VideoCapture(0)
    #
    # cv2.namedWindow("test")
    #
    # img_counter = 0
    #
    # while True:
    #     ret, frame = cam.read()
    #     cv2.imshow("test", frame)
    #     if not ret:
    #         break
    #     k = cv2.waitKey(1)
    #
    #     if k % 256 == 27:
    #         # ESC pressed
    #         print("Escape hit, closing...")
    #         break
    #     elif k % 256 == 32:
    #         # SPACE pressed
    #         img_name = "opencv_frame_{}.png".format(img_counter)
    #         cv2.imwrite(img_name, frame)
    #         print("{} written!".format(img_name))
    #         img_counter += 1
    #
    # cam.release()

    # cv2.destroyAllWindows()

def stream_video():
    # cam = cv2.VideoCapture(0)
    #
    # cv2.namedWindow("test")
    #
    # img_counter = 0
    #
    # while True:
    #     ret, frame = cam.read()
    #     cv2.imshow("test", frame)
    #     if not ret:
    #         break
    #     k = cv2.waitKey(1)
    #
    #     if k % 256 == 27:
    #         # ESC pressed
    #         print("Escape hit, closing...")
    #         break
    #     elif k % 256 == 32:
    #         # SPACE pressed
    #         img_name = "opencv_frame_{}.png".format(img_counter)
    #         cv2.imwrite(img_name, frame)
    #         print("{} written!".format(img_name))
    #         img_counter += 1
    #
    # cam.release()

    # cv2.destroyAllWindows()

    # Create a VideoCapture object and read from input file
    # If the input is the camera, pass 0 instead of the video file name
    cap = cv2.VideoCapture(0)

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video stream or file")

    # Read until video is completed
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        print(type(frame))

        if ret == True:

            # Display the resulting frame
            cv2.imshow('Frame', frame)
	    hacktech(frame)
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            break

    # When everything done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()

@app.route('/')
def display_data():
    return render_template('index.html')
    # return "nothing"

@app.route('/stream_video', methods = ['POST'])
def success():
    if request.method == "POST":
        stream_video()
        return "Thank you!"

# @app.route('/image')
# def login():
#     capture_image()
#     return redirect(url_for('success'))

if __name__ == '__main__':
   app.run(debug = True)

