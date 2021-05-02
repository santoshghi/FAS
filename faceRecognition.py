import cv2
import mysql.connector
import pyttsx3


def voice_message(Name_of_Student):

    voice = pyttsx3.init()
    # rate = engine.getProperty('rate')   # getting details of current speaking rate
    # print(rate)
    volume = voice.getProperty('volume')
    voice.setProperty('volume', volume + 1.25)
    # voices = voice.getProperty('voices')  # getting details of current voice
    # voice.setProperty('voice', voices)  # changing index, changes voices. 1 for female

    voice.setProperty('rate', 170)  # setting up new voice rate
    voice.say(Name_of_Student + 'is Present')
    voice.runAndWait()


def faceRecog():
    def getStatus(status, id):
        con = mysql.connector.connect(host='localhost', database='sms', user='root', password='S9843529908')
        cursor = con.cursor()
        # insert_face_query0 = ("update face set Status = %s, Date=CURDATE(), Time = CURTIME() where Student_ID =%s") %(status, id)
        insert_face_query1 = ("insert into face(Status, Date, Time, Student_ID) values (%s, CURDATE(), CURTIME(), %s) on duplicate key update "
                              "Student_ID = values(Student_ID)") % (status, id)
        cursor.execute(insert_face_query1)
        cursor.close()
        con.commit()
        con.close()

    IDS = []

    def draw_boundary(image, classifier, scalefactor, minNeighbours, color, classifier1):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_feature = classifier.detectMultiScale(gray, scalefactor, minNeighbours)

        status = False

        for x, y, w, h in face_feature:
            cv2.rectangle(image, (x, y), (x + w, y + h), (100, 100, 200), 2)

            id, predict_value = classifier1.predict(gray[y:y + h, x:x + w])
            # print(id)
            # print(predict_value)

            # confidence_level = int(100*(1-predict_value/100))
            # print(confidence_level)

            confidence_level = int(predict_value)
            # print(confidence_level)

            if confidence_level < 50:
                confidence = round(confidence_level)
                # print(confidence)
                con = mysql.connector.connect(host='localhost', database='sms', user='root', password='S9843529908')
                cursor = con.cursor()

                query = 'select Student_ID, Name from sms_table'
                cursor.execute(query)
                column = cursor.fetchall()
                # print(column)

                for i in column:
                    if id == i[0]:
                        cv2.putText(image, i[1] + '[' + str(confidence) + '%' + ']', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1.3, (100, 200, 200), 2)

                        IDS.append(i[0])
                        # print(IDS)
                        Id_set = set(IDS)
                        # print(Id_set)

                        for a in Id_set:
                            if IDS.count(a) == 100:
                                print(IDS.count(a))
                                voice_message(i[1])

                                status = True
                                getStatus(status, a)

                        con.commit()
                con.close()

            else:
                cv2.putText(image, 'Unknown', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 0, 255), cv2.LINE_4)

        return image

    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    classifier2 = cv2.face.LBPHFaceRecognizer_create()
    classifier2.read('classifier.yml')

    # url = 'http://192.168.1.81:8080/video'
    # cam = cv2.VideoCapture('http://192.168.88.16:8080/video')
    # cam = cv2.VideoCapture(url)
    cam = cv2.VideoCapture(-1)

    while True:
        check, frame = cam.read()
        # print(check)
        cv2.putText(frame, "Press 'Q' to exit!!", (0, 25), cv2.FONT_HERSHEY_COMPLEX, 1, (100, 150, 200), 2)
        cv2.putText(frame, "Lower the % greater the accuracy.", (0, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (100, 150, 200), 2)

        frame = draw_boundary(frame, faceCascade, 1.3, 3, (0, 255, 0), classifier2)
        cv2.imshow('Face Detecting Start', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

# faceRecog()
