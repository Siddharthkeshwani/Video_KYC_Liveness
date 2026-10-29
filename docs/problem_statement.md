## Selfie Liveness Check for Indian Video-KYC

### 1. Project Title

Selfie Liveness Check for Indian Video-KYC (inspired by RBI V-CIP liveness requirements)

### 2. Problem Statement

Banks and payment apps in India now open accounts over video. The person never walks into a branch. This makes it easy for a fraudster to cheat. They can hold up a printed photo, play a photo or video on a phone screen, wear a mask, or use a deepfake face.

A single selfie check cannot catch this, because a photo of a photo still looks like a face. The system needs to know two things: is a real person in front of the camera right now, and does the skin in the image look real?

Who loses money: the bank or fintech company. If a fake account gets opened, it can be used for loan fraud or for moving stolen money through mule accounts. The bank pays for the fraud, the investigation and the penalty risk.

### 3. Business Objective

Build a two-layer check for Indian banks and fintech apps.

Layer 1 (geometry): MediaPipe finds 468 points on the face in 3D. The user is asked to turn their head and then come back to the centre. If the head really moves in 3D, a flat photo or flat screen fails.
Layer 2 (texture): an ANN looks at the image features and decides if the face has real skin texture or shows signs of a spoof, like screen glare, print patterns or a mask surface.

A user is verified only if both layers pass.

### 4. Expected Output
A label: Real Live Person or Spoof Attack Detected
A confidence score in percent
In webcam mode, the result of the head-turn challenge (passed or failed)

### 5. Target Variable

y = 0 for real, y = 1 for fake/spoof.

The positive class (1) is fake. This matters for the metrics later, because "recall" will mean "out of all the fake attempts, how many did we catch".

### 6. Input Features
Feature set	        Size	    What it is
Flattened pixels	12,288	    A 64 x 64 colour image turned into one long row (64 x 64 x3)
MediaPipe landmarks	1,404 + 3	468 face points with x, y, z each (468 x 3), plus 3 distances: nose to left cheek, nose to right cheek, eye aspect ratio
CNN features	    1,280	    A vector from MobileNetV2 that describes the texture of the face

### 7. Cost Logic
A spoof accepted as real is the expensive mistake. The bank may lose money.
A real user rejected is the annoying mistake. They have to try again.

So the most important metric is recall on the fake class. Precision on the fake class tells us how many real users we wrongly reject.

Data and Models (short)
Data: Roboflow (real faces and print, screen and mask attacks), Kaggle (Indian real faces), Hugging Face (Indian deepfakes). Target is 3,000 to 5,000 clean images.
Models: Simple ANN, Deep ANN, Landmarks ANN, and the main model, CNN features + ANN.

### Notes on wording and privacy
This project is inspired by RBI V-CIP liveness requirements. It is not an RBI-approved system.
Only public datasets are used. The app does not save uploaded or webcam images.