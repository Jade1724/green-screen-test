import cv2

video = cv2.VideoCapture("green-screen-video.mp4")
image = cv2.imread("japanese-garden.jpg")


def nothing():
    pass


cv2.nameWindow("Trackbars")
cv2.resizeWindow("Trackbars", 300, 300)

cv2.createTrackbar('L - H', "Trackbars", 0, 179, nothing)
cv2.createTrackbar('L - S', "Trackbars", 0, 225, nothing)
cv2.createTrackbar('L - V', "Trackbars", 0, 225, nothing)
cv2.createTrackbar('U - H', "Trackbars", 179, 179, nothing)
cv2.createTrackbar('U - S', "Trackbars", 225, 225, nothing)
cv2.createTrackbar('U - V', "Trackbars", 225, 225, nothing)

while True:
    ret, frame = video.read()
    frame = cv2.resize(frame, (640, 480))
    frame = cv2.resize(image, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos('L - H', "Trackbars")
    l_s = cv2.getTrackbarPos('L - S', "Trackbars")
    l_v = cv2.getTrackbarPos('L - V', "Trackbars")
    u_h = cv2.getTrackbarPos('U - H', "Trackbars")
    u_s = cv2.getTrackbarPos('U - S', "Trackbars")
    u_v = cv2.getTrackbarPos('U - V', "Trackbars")
    
    mask = cv2.inRange(hsv, )
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.detroyAllWindows()
