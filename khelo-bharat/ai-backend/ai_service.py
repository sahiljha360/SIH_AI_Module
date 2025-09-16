from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
import cv2
import mediapipe as mp
import numpy as np
import tempfile
import os

app = FastAPI()

# Initialize MediaPipe Pose
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

@app.post("/analyze_video/")
async def analyze_video(
    video: UploadFile = File(...),
    age: int = Form(...),
    height: float = Form(...),
    weight: float = Form(...)
):
    # Save uploaded video to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
        temp_video.write(await video.read())
        temp_video_path = temp_video.name

    # Open video file
    cap = cv2.VideoCapture(temp_video_path)
    pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    rep_count = 0
    tampering_detected = False
    # TODO: Add your posture detection, rep counting, and tampering logic here
    # For now, just count frames as dummy reps
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        # Example: Dummy rep count
        rep_count += 1
        # TODO: Add tampering detection logic
    cap.release()
    pose.close()
    os.remove(temp_video_path)

    # Example scoring logic
    score = rep_count + age + int(height) + int(weight)
    return JSONResponse({
        "reps": rep_count,
        "tampering": tampering_detected,
        "score": score
    })

@app.get("/")
def root():
    return {"message": "AI Posture Analysis API is running."}
