from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.staticfiles import StaticFiles
import cv2
import dlib
import pyautogui
import numpy as np

# Initialize FastAPI app
app = FastAPI()

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Optionally, add static file handling (for CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Add middleware for security (optional)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

# Home route that renders the index.html template
@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello, FastAPI!"})

@app.get("/mars", response_class=HTMLResponse)
async def get_mars_page(request: Request):
    return templates.TemplateResponse("mars.html", {"request": request})

@app.post("/start-face-tracking")
async def start_face_tracking(background_tasks: BackgroundTasks):
        # Initialize face detector (Dlib)
    detector = dlib.get_frontal_face_detector()

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    # Variables to store the previous position of the face
    previous_x = None

    # Get screen width and height for boundary checks
    screen_width, screen_height = pyautogui.size()

    # Variables for mouse movement sensitivity
    base_sensitivity = 5  # Base sensitivity for mouse movement (can be adjusted)
    movement_threshold = 10  # Minimum change in position to trigger mouse movement

    # Flag to track whether mouse is down (for dragging)
    mouse_down = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = detector(gray)

        # Loop through all detected faces (in case there are multiple faces)
        for face in faces:
            # Get the coordinates of the face bounding box
            x1, y1, x2, y2 = (face.left(), face.top(), face.right(), face.bottom())

            # Draw a rectangle around the face
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Track face movement
            face_center_x = (x1 + x2) // 2

            if previous_x is not None:
                # Calculate the difference in face position
                movement = face_center_x - previous_x

                # Check if the movement is above the threshold
                if abs(movement) > movement_threshold:
                    if not mouse_down:
                        pyautogui.mouseDown()  # Start dragging when head turns
                        mouse_down = True

                    # Scale the mouse movement based on the difference in face position
                    scaled_movement = movement * base_sensitivity  # Exaggerate movement
                    pyautogui.moveRel(scaled_movement, 0)  # Move mouse horizontally

                    if movement > 0:
                        print(f"Moving Right (Dragging) by {scaled_movement}")
                    else:
                        print(f"Moving Left (Dragging) by {scaled_movement}")
                else:
                    if mouse_down:
                        pyautogui.mouseUp()  # Release the mouse when face stops moving
                        mouse_down = False
                    print("Stopping Drag")

            # Update previous position of the face
            previous_x = face_center_x

        # Display the frame
        cv2.imshow("Face Movement Tracker", frame)

        # Break on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release webcam and close windows
    cap.release()
    cv2.destroyAllWindows()