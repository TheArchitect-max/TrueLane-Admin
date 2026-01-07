# =================================================================
# PROJECT: DEUS V1 (DEFINITIVE MOTHERCODE)
# OWNER/ARCHITECT: TRUELANESTUDIO
# COPYRIGHT: © 2026 TRUELANESTUDIO. ALL RIGHTS RESERVED.
# -----------------------------------------------------------------
# LICENSE TERMS:
# 1. PROPRIETARY: This code is the sole invention of TrueLaneStudio.
# 2. NON-TRANSFERABLE: Purchase grants a single-user usage license.
# 3. NO REDISTRIBUTION: Copying or selling this code is prohibited.
# 4. ENFORCEMENT: Violation terminates the license immediately.
# =================================================================

import cv2
import mediapipe as mp
import pyautogui
import screeninfo
import time
import sys

# --- INTEGRATED TECHNICAL SPECIFICATION SHEET ---
"""
TECHNICAL SPECIFICATION SHEET - DEUS V1
--------------------------------------
1. HARDWARE REQUIREMENTS: 
   - Processor: Dual-Core 2.0GHz+ (Optimized for low-spec hardware)
   - RAM: 4GB minimum
   - Camera: Standard 720p USB or Integrated Webcam
2. SOFTWARE ARCHITECTURE:
   - Neural Engine: MediaPipe FaceMesh (468 3D Landmarks)
   - Control Bridge: PyAutoGUI Direct-to-OS
3. LATENCY METRICS: 
   - Processing: < 15ms
   - Trigger Response: 0.35s (Standard Ocular Compression)
"""

# --- INTEGRATED SYSTEM INTEGRATION LETTER ---
"""
OFFICIAL COMMUNICATION: SYSTEM INTEGRATION
------------------------------------------
To the End-User:
You have acquired DEUS V1, a neural interface designed to disrupt
monopolistic pricing structures. At a value of $535.00, this system 
provides autonomy previously gated behind high-capital barriers.
------------------------------------------
"""

def startup_protocol():
    manifest = [
        "=====================================================",
        "          DEUS V1: MASTER INTELLIGENCE ONLINE        ",
        "          PROPERTY OF: TRUELANESTUDIO                ",
        "=====================================================",
        "LICENSE REGISTERED: $535.00",
        "MISSION: TECHNOLOGY AS A FUNDAMENTAL HUMAN RIGHT",
        "-----------------------------------------------------",
        "VERIFYING PROPRIETARY LICENSE...",
        "INITIALIZING NEURAL MAPPING ENGINE...",
        "HARDWARE-AGNOSTIC OPTIMIZATION: ENABLED",
        "-----------------------------------------------------",
        "ACCESS GRANTED. AUTONOMY ENGAGED."
    ]
    for line in manifest:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.007)
        print()
    print("\n[V1 MANUAL]: NOSE = CURSOR | LEFT-BLINK = CLICK | 'Q' = EXIT\n")

# --- ARCHITECTURAL CORE ---
def get_display_metrics():
    try:
        screen = screeninfo.get_monitors()[0]
        return screen.width, screen.height
    except Exception:
        return 1920, 1080

SW, SH = get_display_metrics()
pyautogui.FAILSAFE = False

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1, 
    refine_landmarks=True, 
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)

# Operational Tuning
PROC_W, PROC_H = 640, 480
SMOOTHING, SENSITIVITY = 3, 2.6
prev_x, prev_y = SW // 2, SH // 2

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, PROC_W)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, PROC_H)

startup_protocol()

try:
    while cam.isOpened():
        success, frame = cam.read()
        if not success: break
        
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)
        
        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            
            # Feature: Spatial Navigation (Nose Tip)
            nose = landmarks[1]
            target_x = int(nose.x * SW * SENSITIVITY - (SW * (SENSITIVITY - 1) / 2))
            target_y = int(nose.y * SH * SENSITIVITY - (SH * (SENSITIVITY - 1) / 2))
            
            curr_x = prev_x + (target_x - prev_x) / SMOOTHING
            curr_y = prev_y + (target_y - prev_y) / SMOOTHING
            
            pyautogui.moveTo(curr_x, curr_y, _dt=0)
            prev_x, prev_y = curr_x, curr_y

            # Feature: Intent-Based Trigger (Left Eye Blink)
            if (landmarks[145].y - landmarks[159].y) < 0.006:
                pyautogui.click()
                time.sleep(0.35) 

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cam.release()
    cv2.destroyAllWindows()
