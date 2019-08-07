@echo off
ECHO Co-Registration: Electroencephalography + EyeTracking
set /p id="Enter ID: "

PAUSE

cd C:\Users\Nico\PowerFolders\project_coregistration_EEG_ET
start py tobiilsl.py
start py ReceivePresentationEventmarker.py %id%
start py ReceiveEyeTrackingData.py %id%
