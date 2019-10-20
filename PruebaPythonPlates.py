#!/usr/bin/python
# encoding: utf-8
import beanstalkc
import json
from pprint import pprint

beanstalk = beanstalkc.Connection(host='localhost', port=11300)
TUBE_NAME='alprd'

# For diagnostics, print out a list of all the tubes available in Beanstalk
print (beanstalk.tubes())


# For diagnostics, print the number of items on the current alprd queue
try:
    pprint(beanstalk.stats_tube(TUBE_NAME)) 
except beanstalkc.CommandFailed:
    print ("Tube doesn't exist")

# Watch the "alprd" tube, this is where the plate data is.
beanstalk.watch(TUBE_NAME)

# Loop forever
while True:

    # Wait for a second to get a job.  If there's a job, process it and delete it from the queue.  
    # If not, go back to sleep
    job = beanstalk.reserve(timeout=1.0)

    if job is None:
        print ("No plates available right now, waiting...")

    else:
        print ("Found a plate!")
        plates_info = json.loads(job.body)


        # Print all the info about this plate to the console
      ## imprimia todo el body  pprint(plates_info)
        #print(plates_info["os"])
        if 'best_plate_number'  in plates_info:
            print (plates_info["best_plate_number"])
       # pprint(plates_info)
       #Parámetro de la foto --> openalpr plate_crop_jpeg

        # Do something with this data (e.g., match a list, open a gate, etc.)
      #  if 'data_type' not in plates_info:
      #      print ("This shouldn't be here... all OpenALPR data should have a data_type")
       # elif plates_info['data_type'] == 'alpr_results':
        #    print ("This is a plate result")
        #elif plates_info['data_type'] == 'alpr_group':
        #    print ("This is a group result")

        # Delete the job from the queue now that we have processed it
        job.delete()


 # 'plate_index': 0,
 #                'processing_time_ms': 111.26599884033203,
 #                'region': '',
 #                'region_confidence': 0,
 #                'requested_topn': 10,
 #                'vehicle_region': {'height': 256,
 #                                   'width': 256,
 #                                   'x': 712,
 #                                   'y': 375}},
 # 'best_plate_number': 'CFH764',
 # 'best_region': '',
 # 'best_region_confidence': 0,
 # 'best_uuid': 'UGQSFML9B428DQYQYSUDJAR6CTT88YO9VPEPE12T-610071606-1571599424626',
 # 'camera_id': 610071606,
 # 'candidates': [{'confidence': 92.9171142578125,
 #                 'matches_template': 1,
 #                 'plate': 'CFH764'}],
 # 'company_id': 'unspecified',
 # 'country': 'ar',
 # 'data_type': 'alpr_group',
 # 'epoch_end': 1571599431250L,
 # 'epoch_start': 1571599424397L,
 # 'frame_end': 67988,
 # 'frame_start': 67865,
 # 'is_parked': True,
 # 'is_preview': False,
 # 'matches_template': True,
 # 'plate_indexes': [0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0,
 #                   0],
 # 'travel_direction': 227.64227294921875,