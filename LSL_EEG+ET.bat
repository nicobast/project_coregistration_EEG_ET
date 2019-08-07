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
start python tobiilsl.py
start python ReceivePresentationEventmarker.py %id%
start python ReceiveEyeTrackingData.py %id%
