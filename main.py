import cv2
import win32api, win32con
import time


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
eyechecker = 3
first_read = True
blinkchecker = [3,3,3,3,3,3]


def click(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
click(10,10)

def Right_click(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
click(10,10)


while cap.isOpened():


    ret, frame1 = cap.read()
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    faces1 = face_cascade.detectMultiScale(gray1, 1.1, 4)

    for (x,y,w,h) in faces1:

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (253, 153, 255), 2, )
        roi_gray = gray1[y:y+h, x:x+w]
        roi_color = frame1[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10)
        time.sleep(0.075)
        win32api.SetCursorPos((5*x-200, 5*y-500 ))

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey), (ex+ew, ey+eh), (255, 255, 0), 3)

            if (len(eyes) == 2):

                if (first_read):
                    cv2.putText(frame1,
                                "Blink detected",
                                (70, 70),
                                cv2.FONT_HERSHEY_PLAIN, 3,
                                (0, 255, 0), 2)
                else:
                    cv2.putText(frame1,
                                "Eyes open!", (70, 70),
                                cv2.FONT_HERSHEY_PLAIN, 2,
                                (255, 0, 255), 2)

        if (len(eyes) == 1):
            print("wink detected--------------")
            Right_click(5 * x - 200, 5 * y - 500)
            first_read = True
            time.sleep(0.25)


    for i in range (6):
        blinkchecker[i] = len((eyes))
        print(blinkchecker)
        if (blinkchecker[1] and blinkchecker[2] and blinkchecker[0] and blinkchecker[3] and blinkchecker[4] and blinkchecker[5]==0):
            print("BLINK detected--------------")
            click(5 * x - 200, 5 * y - 500)
            first_read = True
            time.sleep(0.25)


    cv2.imshow("feed", frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    first_read = False
    eyechecker=len(eyes)
    print(eyechecker, len(eyes))


cap.release()
cv2.destroyAllWindows()


