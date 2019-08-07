"""Example program to show how to read any LSL stream."""

from pylsl import StreamInlet, resolve_stream
import csv #write csv file
import os #change cd to store data
import sys #handle arguments for id

#participant id variable
print("This script looks for LSL Presentation event markers...")
#participant_id = raw_input('Enter participant ID:')
participant_id = sys.argv[1] #takes the name from script argument
file_name = str(participant_id) + '_events.csv'

# first resolve an EEG stream on the lab network
print("looking for Presentation eventmarker...")
streams = resolve_stream('name','eventmarker')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])
print("...found. Pulling timestamp and eventcode:")

#create CSV file and write received data to it
os.chdir(os.getcwd()+"\data") #change cd to data folder
with open(file_name, 'wb') as csvfile: #mode needs to be "wb" in python 2 to remove blank rows
    csvwriter = csv.writer(csvfile)

    #main loop
    while True:
        sample, timestamp = inlet.pull_sample()
        sample.append(timestamp*1000)
        #SAVE TO FILE
        csvwriter.writerow(sample) #change timestamp to ms format --> easier for later R import
        print(sample)
