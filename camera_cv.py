import cv2

# Use the IP address and port shown by IP Webcam app
url = "http://192.168.1.1:8080/video"  # Replace with your IP and port

# Initialize the video capture
cap = cv2.VideoCapture(url)

# Initialize QR Code detector
qr_code_detector = cv2.QRCodeDetector()

# Create a set to store detected QR codes
detected_qr_codes = set()

if not cap.isOpened():
    print("Error: Could not open video stream.")
else:
    print("Connected to IP Webcam successfully.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame.")
        break

    # Detect and decode QR code
    data, bbox, _ = qr_code_detector.detectAndDecode(frame)

    # If a QR code is detected and it's not already in the set, print it
    if data and data not in detected_qr_codes:
        print("QR Code detected: ", data)
        detected_qr_codes.add(data)

    # Display the frame with a rectangle around QR code if detected
    if bbox is not None:
        for i in range(len(bbox[0])):
            # Convert coordinates to integers
            start_point = (int(bbox[0][i][0]), int(bbox[0][i][1]))
            end_point = (int(bbox[0][(i + 1) % len(bbox[0])][0]), int(bbox[0][(i + 1) % len(bbox[0])][1]))
            cv2.line(frame, start_point, end_point, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("IP Webcam Stream", frame)

    # Press 'q' to exit the video stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
