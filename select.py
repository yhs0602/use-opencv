import cv2

def select_area(event, x, y, flags, param):
    global ref_point, crop

    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]

    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x, y))
        cv2.rectangle(frame, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("Frame", frame)

if __name__ == '__main__':
    cap = cv2.VideoCapture('IMG_1758.MOV')
    ret, frame = cap.read()

    cv2.namedWindow("Frame")
    cv2.setMouseCallback("Frame", select_area)

    while True:
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # 선택된 영역 좌표 출력
    if ref_point:
        print("Selected Area: {}".format(ref_point))


# ffmpeg -i input.mp4 -vf "crop=w:h:x:y" output.mp4
# [(317, 544), (971, 1298)]
# w: 971 - 317 = 654
# h: 1298 - 544 = 754
# x: 317
# y: 544