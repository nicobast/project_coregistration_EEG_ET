@echo off
ECHO Co-Registration: Electroencephalography + EyeTracking
ECHO -----------------------------------------------------
ECHO Did you run CALIBRATION?
ECHO Press any key after running CALIBRATION...
PAUSE >nul

set /p id="Enter ID: "

ECHO PRESS KEY TO START LAB STREAMING LAYER SCRIPTS...
PAUSE

cd C:\Users\Nico\PowerFolders\project_coregistration_EEG_ET
start "tobiilsl" python tobiilsl.py
start "receive_presentation_eventmarker" python ReceivePresentationEventmarker.py %id%
start "receive_eyetracking_data" python ReceiveEyeTrackingData.py %id%

ECHO ARRANGE SCRIPT WINDOWS ON DISPLAY...

cmdow tobiilsl /mov 0 0
cmdow receive_presentation_eventmarker /mov 1000 500
cmdow receive_eyetracking_data /mov 1000 0

cmdow tobiilsl /siz 1000 500
cmdow receive_presentation_eventmarker /siz 1000 500
cmdow receive_eyetracking_data /siz 1000 500
