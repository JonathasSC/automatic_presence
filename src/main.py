import cv2
from utils import *


WEBCAM = 0
COLOR = (0, 255, 0)


def main():
    my_spreadsheet = Spreadsheet('src\spreadsheet.xlsx')
    my_spreadsheet.update_file()

    cam = cv2.VideoCapture(WEBCAM)

    sfr = SimpleFacerec()
    sfr.load_encoding_images("src\persons")

    while True:
        ret, frame = cam.read()
        faces_locations, image_names = sfr.detect_known_faces(frame)

        for location, img_name in zip(faces_locations, image_names):
            img_name = img_name.replace('_', ' ')
            upper_img_name = img_name.upper()

            y1 = location[0]
            x1 = location[1]
            y2 = location[2]
            x2 = location[3]

            name_cord = (x2, y1 - 10)
            cv2.putText(frame, img_name, name_cord,
                        cv2.FONT_HERSHEY_PLAIN, 1, COLOR, 1)
            cv2.rectangle(frame, (x1, y1), (x2, y2), COLOR, 2)

            my_spreadsheet.be_presence(upper_img_name)

        cv2.imshow("Frame", frame)

        if cv2.waitKey(5) == 27:
            break
        else:
            pass

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
