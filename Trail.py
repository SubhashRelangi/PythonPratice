import cv2

video = cv2.VideoCapture("Videos/testing.mp4")

if not video.isOpened():
    print("Error in opening video file!")
    exit()

fps = 20

output = cv2.VideoWriter("Videos/output2.mp4", 
                         cv2.VideoWriter_fourcc(*"MJPG"), 
                         fps, 
                         (640, 480))   

while True:
    ret, frame = video.read()

    if not ret:
        print("Stream Disconnected / Video Ended")
        break

    frame1 = cv2.resize(frame, (1000, 500))

    # print shapes here safely
    print("Original shape:", frame.shape)
    print("Resized shape:", frame1.shape)

    output.write(frame1)
    cv2.imshow("Output", frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
output.release()
cv2.destroyAllWindows()
