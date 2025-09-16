# AI Backend for Khelo Bharat

This folder contains the AI backend service for posture detection, video tampering detection, and rep counting.

## How to Run

1. Create and activate a Python 3.10 virtual environment:
   ```sh
   py -3.10 -m venv venv310
   .\venv310\Scripts\activate
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```sh
   uvicorn ai_service:app --reload
   ```

## API Usage

POST `/analyze_video/`
- Form Data: `video` (mp4), `age`, `height`, `weight`
- Response: `{ reps, tampering, score }`

## Integration
- The Expo app should POST video and user data to this backend and use the response for scoring and validation.
