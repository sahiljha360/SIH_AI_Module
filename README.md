# SIH AI Module

This repository contains an AI backend service for posture detection, video tampering detection, and rep counting, designed for integration with an Expo Go (React Native) Android app and Firebase.

## Features
- Accepts video uploads and user data (age, height, weight, etc.)
- Detects exercise posture and counts legal reps
- Checks for video tampering
- Returns a score based on reps and user parameters

## How to Run the Service

1. **Clone the repository:**
   ```sh
   git clone https://github.com/sahiljha360/SIH_AI_Module.git
   cd SIH_AI_Module
   ```
2. **Create and activate a Python 3.10 virtual environment:**
   ```sh
   py -3.10 -m venv venv310
   .\venv310\Scripts\activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the FastAPI server:**
   ```sh
   uvicorn ai_service:app --reload
   ```

## API Usage

### POST `/analyze_video/`
- **Form Data:**
  - `video`: Video file (mp4)
  - `age`: int
  - `height`: float
  - `weight`: float
- **Response:**
  ```json
  {
    "reps": 10,
    "tampering": false,
    "score": 123
  }
  ```

## Integration with Expo/Firebase App
- Use `fetch` or `axios` in your React Native app to POST video and user data to the `/analyze_video/` endpoint.
- Parse the JSON response for rep count, tampering status, and score.

## Requirements
- Python 3.10
- See `requirements.txt` for dependencies

---

For any issues, open an issue on GitHub.
