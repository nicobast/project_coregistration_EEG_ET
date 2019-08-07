"""Example program to show how to read any LSL stream."""

from pylsl import StreamInlet, resolve_stream #lab streaming layer
import csv #write csv file
import os #change cd to store data
import sys #handle arguments for id

#predefined variables
last_report = 0 #define variable for printing of ET data

#participant id variable
print("This script looks for LSL Eye Tracking data...")
#participant_id = raw_input('Enter participant ID:')
participant_id = sys.argv[1] #takes the name from script argument
filename = str(participant_id) + '_ETdata.csv'

# first resolve an EEG stream on the lab network
print("looking for EyeTracking LSL stream...")
streams = resolve_stream('name','Tobii')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])
print("...found. Pulling data:")

#create CSV file and write received data to it
os.chdir(os.getcwd()+"\data") #change cd to data folder
with open(filename, 'wb') as csvfile: #mode needs to be "wb" in python 2 to remove blank rows
    csvwriter = csv.writer(csvfile)

    #main loop
    while True:
        ETdata, timestamp = inlet.pull_sample()
        ETdata.append(timestamp*1000) #change timestamp to ms format and add to ET data list
        csvwriter.writerow(ETdata)

        sts = ETdata[31] #local timestamp

        if sts > last_report + 250: #printspupillometry data to screen every 250ms
            print([round(ETdata[29],3), round(ETdata[30],3)])
            last_report = sts
