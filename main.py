import cv2

if __name__ == '__main__':
    # OpenCV를 이용하여 비디오를 불러옵니다.
    cap = cv2.VideoCapture("IMG_1758.MOV")

    # 첫 번째 프레임을 가져옵니다.
    ret, frame = cap.read()

    # 사용자로부터 객체를 선택받습니다. (ROI: Region of Interest)
    roi = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
    x, y, w, h = roi

    # 선택된 ROI를 초기 바운딩 박스로 사용하여 추적기를 초기화합니다.
    tracker = cv2.TrackerKCF_create()
    tracker.init(frame, (x, y, w, h))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 현재 프레임에서 객체 추적을 업데이트합니다.
        success, box = tracker.update(frame)
        if success:
            x, y, w, h = map(int, box)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
