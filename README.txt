## This is a short guide to co-registrate EEG and EyeTracking data with lab streaming layer (lsl). ##

DESCRIPTION:
The EEG data can be mapped to eyetracking data by local timestamps.
Timestamps will be delivered with 1.) eventcodes sent by Presentation and 2.) Eye Tracking Data sent by the EyeTracker.
This information is pushed and pulled by lab streaming layer (lsl).
Data will be received by python interface with lsl (pylsl).
It requires installations of lsl, pylsl with required modules, and presentation.
It is configured for running on the machine that concurrently processes Presentation and EyeTracking data as coregistration will be done by local timestamps.
For running on different system, this needs to be adapted (can be done in pylsl).
timestamps are converted to a millisecond format, less precision than provided microsecond format.

Tested on windows 10 64bit with Visual Studio 2017

TO DO:
- implement calibration routine --> (workaround: do with Tobii Pro Spectrum)
  -- use pygame for calibration point presentation
  -- build loop to recalibrate failed calibration points

1. ## INSTALL LABSTREAMING LAYER
# info: need to create a build from source (see: https://github.com/sccn/labstreaminglayer/wiki/INSTALL)
# - clone source files with GITHUB
# - create BUILD with CMAKE in admin/sudo mode (creates VisualStudio Files from Source)
# - build INSTALLATION (install) with MSVC (implemented in Visual Studio C++ Tools)
---> now lab streaming layer should be installed according to the system

2. ## INSTALL PYTHON 2.7 and required modules (see: https://www.python.org/download/releases/2.7/)
# info: this specific version is needed as Tobii Pro SDK (tobi-research module) required for tobiilsl is only available in 2.7 and 3.5 and python only provides installer for 2.7
# - DEPENDENCIES: install required packages in python (with PIP)
#  	- numpy: 'pip install numpy'
# 	- tobii research: 'pip install tobii-research' (this contains the required new Tobii Pro SDK)
#	  - python lab streaming layer: 'pip install pylsl' (python communication iwth lsl)

3. ## PRESENTATION: ACTIVATE "send event data to LSL"
# info: enable option that Presentation sends eventmarker
# - found in: Settings/General/Lab Streaming Layer
# - make sure to name stream 'eventmarker'
# - option under Properties: only send event codes
# - check 'open stram outlet when experiment is loaded'
# - save for specific experiment (in this case: Posner task)

4. --> copy project files
# - contains tobiilsl (lsl server that sends eyetracking data to lsl is now in project files)
# - ALTERNATIVELY: clone source from GITHUB (https://github.com/baekgaard/tobiilsl.git)

5. ## TO START CO-REGISTRATION OF EEG AND ET: run batch file: LSL_EEG+ET
# - change within batch file path to directory where files have been copied to
# IMPORTANT: Run calibration procedure in Tobii Pro Eye Tracker Manager before
# RUN batch file (double click):
# -- Enter participant ID
# -- Wait till Presentation is setup
# -- Press enter to start the three required scripts:
# ---- 1. tobiilsl: sends EyeTracking Data to LSL
# ---- 2. ReceiveEyeTrackingData: captures LSL EyeTRacking data and saves to file
# ---- 3. ReceivePresentationEventmarker: captures LSL Presentation Events and saves to file
