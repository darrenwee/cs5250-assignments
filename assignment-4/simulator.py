"""
CS5250 Assignment 4, Scheduling policies simulator
Sample skeleton program
Input file:
    input.txt
Output files:
    FCFS.txt
    RR.txt
    SRTF.txt
    SJF.txt


Darren Wee Zhe Yu
A0147609X
AY 2018/19 Semester 2
"""

from typing import Tuple, List


class Process:
    last_scheduled_time = 0

    def __init__(self, id, arrive_time, burst_time):
        self.id = id
        self.arrive_time = arrive_time
        self.burst_time = burst_time

    def __repr__(self):
        return '[id %d : arrival_time %d,  burst_time %d]' % (self.id, self.arrive_time, self.burst_time)


def FCFS_scheduling(process_list) -> Tuple[List[Tuple], float]:
    # store the (switching time, proccess_id) pair
    schedule = []
    current_time = 0
    waiting_time = 0
    for process in process_list:
        if current_time < process.arrive_time:
            current_time = process.arrive_time
        schedule.append((current_time, process.id))
        waiting_time = waiting_time + (current_time - process.arrive_time)
        current_time = current_time + process.burst_time
    average_waiting_time = waiting_time / float(len(process_list))
    return schedule, average_waiting_time


"""
Input: process_list, time_quantum (Positive Integer)
Output_1 : Schedule list contains pairs of (time_stamp, proccess_id) indicating the time switching to that proccess_id
Output_2 : Average Waiting Time
"""


def RR_scheduling(process_list, time_quantum) -> Tuple[List[Tuple], float]:
    return (["to be completed, scheduling process_list on round robin policy with time_quantum"], 0.0)


def SRTF_scheduling(process_list) -> Tuple[List[Tuple], float]:
    return (["to be completed, scheduling process_list on SRTF, using process.burst_time to calculate the remaining time of the current process"],
            0.0)


def SJF_scheduling(process_list, alpha) -> Tuple[List[Tuple], float]:
    return (["to be completed, scheduling SJF without using information from process.burst_time"], 0.0)


def read_input(filename):
    result = []
    with open(filename) as f:
        for line in f:
            array = line.split()
            if len(array) != 3:
                print("wrong input format")
                exit()
            result.append(Process(int(array[0]), int(array[1]), int(array[2])))
    return result


def write_output(file_name: str, schedule: List[Tuple], avg_waiting_time: float):
    with open(file_name, 'w') as f:
        for item in schedule:
            f.write(str(item) + '\n')
        f.write('average waiting time %.2f \n' % avg_waiting_time)


def main(input_file: str = 'input.txt'):
    process_list = read_input(input_file)

    print("printing input ----")
    for process in process_list:
        print(process)

    print("simulating FCFS ----")
    fcfs_schedule, fcfs_avg_waiting_time = FCFS_scheduling(process_list)
    write_output('FCFS.txt', fcfs_schedule, fcfs_avg_waiting_time)

    print("simulating RR ----")
    rr_schedule, rr_avg_waiting_time = RR_scheduling(process_list, time_quantum=2)
    write_output('RR.txt', rr_schedule, rr_avg_waiting_time)

    print("simulating SRTF ----")
    srtf_schedule, srtf_avg_waiting_time = SRTF_scheduling(process_list)
    write_output('SRTF.txt', srtf_schedule, srtf_avg_waiting_time)

    print("simulating SJF ----")
    sjf_schedule, sjf_avg_waiting_time = SJF_scheduling(process_list, alpha=0.5)
    write_output('SJF.txt', sjf_schedule, sjf_avg_waiting_time)


if __name__ == '__main__':
    main()
