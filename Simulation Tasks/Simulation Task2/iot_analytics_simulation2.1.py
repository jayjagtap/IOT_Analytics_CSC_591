# -*- coding: utf-8 -*-
"""
IOT_analytics_simulation task 2.1
Author: Jay Jagtap
"""

def simulation(simulation_values):

  mc = simulation_values["mc"]
  rtcl = simulation_values["rtcl"]
  non_rtcl = simulation_values["non_rtcl"]
  q_rt = simulation_values["q_rt"]
  q_nonrt = simulation_values["q_nonrt"]
  scl = simulation_values["scl"]
  system_state=simulation_values["system_state"]
  remaining_service_time=simulation_values["remaining_service_time"]
  interarrivaltime_rt = simulation_values["interarrivaltime_rt"]
  interarrivaltime_nonrt = simulation_values["interarrivaltime_nonrt"]
  servicetime_rt = simulation_values["servicetime_rt"]
  servicetime_nrt = simulation_values["servicetime_nrt"]

  compare_clock = [rtcl , non_rtcl, scl]

  print '{0}\t {1}\t{2}\t\t{3}\t{4}\t\t{5}\t{6}\t{7}\t'.format("mc" , "rtcl", "non_rtcl", "q_rt", "q_nonrt", "scl", "system_state", "remaining_service_time")
  print '{0}\t {1}\t{2}\t\t{3}\t{4}\t\t{5}\t{6}\t{7}\t'.format(mc , rtcl, non_rtcl, q_rt, q_nonrt, scl, system_state, remaining_service_time)

  
  while mc <= 200:
    compare_clock = [scl, rtcl , non_rtcl]
    """
      index
      0: scl,
      1: rtcl
      2: non_rtcl
    """

    index = compare_clock.index(min(compare_clock))

    scl = compare_clock[0]
    rtcl = compare_clock[1]
    non_rtcl = compare_clock[2]

    if index == 1:
      mc = rtcl
      rtcl += interarrivaltime_rt
      system_state = 1
      if scl - mc > 0:
        remaining_service_time = scl - mc
        q_nonrt+=1
      scl = mc + servicetime_rt
    elif index == 0:
      mc = scl 
      if non_rtcl == scl:
          non_rtcl += interarrivaltime_nonrt
          q_nonrt+=1
      elif scl == rtcl:
        rtcl += interarrivaltime_rt
        scl += servicetime_rt
        system_state=1
      else:
        if remaining_service_time != 0:
          if q_nonrt!=0:
            q_nonrt-=1
          scl+=remaining_service_time
          remaining_service_time=0
          system_state=2
        else:
          if q_nonrt !=0:
             q_nonrt-=1
          scl+=servicetime_nrt
          system_state=2 
    else:
      mc = non_rtcl
      non_rtcl += interarrivaltime_nonrt
      q_nonrt+=1

    print '{0}\t {1}\t{2}\t\t{3}\t{4}\t\t{5}\t{6}\t{7}\t'.format(mc , rtcl, non_rtcl, q_rt, q_nonrt, scl, system_state, remaining_service_time)
    

if __name__ == '__main__':
  
  simulation_values ={
      "mc": 0,
      "rtcl":3,
      "non_rtcl":5,
      "q_rt":0,
      "q_nonrt":0,
      "scl":4,
      "system_state":2,
      "remaining_service_time":0,
  }

  # simulation_values2 ={
  #     "mc": 0,
  #     "rtcl":3,
  #     "non_rtcl":5,
  #     "q_rt":0,
  #     "q_nonrt":0,
  #     "scl":4,
  #     "system_state":2,
  #     "remaining_service_time":0,
  #     "interarrivaltime_rt":5,
  #     "interarrivaltime_nonrt":10,
  #     "servicetime_rt": 4,
  #     "servicetime_nrt":2
  # }
  
  simulation_values["interarrivaltime_rt"] = int(input("Please Enter inter-arrival time of RT messages: "))
  simulation_values["interarrivaltime_nonrt"] = int(input("Please Enter  inter-arrival time of nonRT messages: "))
  simulation_values["servicetime_rt"] = int(input("Please Enter  service time of RT messages: "))
  simulation_values["servicetime_nrt"] = int(input("Please Enter service time of nonRT messages: "))
  
  simulation(simulation_values)
 