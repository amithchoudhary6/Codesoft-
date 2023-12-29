import cv2
from deepface import DeepFace

# Load the known face image and its embedding
known_face = cv2.imread("WIN_20230912_12_06_30_Pro.jpg")
known_face_embedding = DeepFace.represent(known_face)

# Initialize the camera
camera = cv2.VideoCapture(0)

# Create a window for displaying the camera feed
cv2.namedWindow("Face Recognition")

while True:
    # Capture a frame from the camera
    ret, frame = camera.read()

    # Perform face recognition on the frame
    if ret:
        frame_embedding = DeepFace.represent(frame)
        distance = DeepFace.euclidean_l2(known_face_embedding, frame_embedding)

        # Set a threshold for recognition
        threshold = 0.6

        if distance < threshold:
            text = "Face Recognized"
        else:
            text = "Face Not Recognized"

        # Display the result on the frame
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Face Recognition", frame)

    # Press 'q' to exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
camera.release()
cv2.destroyAllWindows()