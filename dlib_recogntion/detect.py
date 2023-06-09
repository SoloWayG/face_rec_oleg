def detect_person_in_video(encodings_,video_path):
    video = cv2.VideoCapture(video_path)

    while True:
        ret, image = video.read()

        locations = face_recognition.face_locations(image, model="hog")
        encodings = face_recognition.face_encodings(image, locations)

        for face_encoding, face_location in zip(encodings, locations):
            color=[0, 255, 0]
            for name in encodings_:
                
                result = face_recognition.compare_faces(encodings_[name], face_encoding)
                match = None

                if True in result:
                    match = name
                    print(f"Match found! {match}")
                    color = [0, 0, 255]
                else:
                    print("ACHTUNG! ALARM!")
                    #color = [0, 255, 0]

                left_top = (face_location[3], face_location[0])
                right_bottom = (face_location[1], face_location[2])
               
                cv2.rectangle(image, left_top, right_bottom, color, 4)

                left_bottom = (face_location[3], face_location[2])
                right_bottom = (face_location[1], face_location[2] + 20)
                cv2.rectangle(image, left_bottom, right_bottom, color, cv2.FILLED)
                cv2.putText(
                    image,
                    match,
                    (face_location[3] + 10, face_location[2] + 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    4
                )
        cv2.imshow("detect_person_in_video is running", image)

        k = cv2.waitKey(20)
        if k == ord("q"):
            print("Q pressed, closing the app")
            break
