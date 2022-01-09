import face_recognition
def facedect():
    root = r"C:\Users\Sloth\Desktop\new1\finalv5\dash\templates\dash"

    loc1 = root + r"\2.jpeg"
    
    face_1_image = face_recognition.load_image_file(loc1)
    face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]

    #
    loc2 = root + r"\1.jpeg"

    face_2_image = face_recognition.load_image_file(loc2)
    face_2_face_encoding = face_recognition.face_encodings(face_2_image)[0]

    #small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

    #rgb_small_frame = small_frame[:, :, ::-1]

    #face_locations = face_recognition.face_locations(rgb_small_frame)
    #face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)


    check=face_recognition.compare_faces([face_1_face_encoding], face_2_face_encoding)
    

    print(check)
    if check[0]:
            print(True)
            return True

    else :
            print(False)
            return False    
facedect()