from datetime import datetime
from collections import deque

def total_minute(s1,s2):
    FMT = '%H:%M'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    total_minute = (int(tdelta[0]) *60) + int(tdelta[1])
    return total_minute

def total_vaccinated(room_capacity, total_peaple, total_time, arrival_times):
    total_vaccination = room_capacity
    room = deque()
    room = room.extendleft(arrival_times[0:room_capacity])

    last = room_capacity-1

    while (last <= total_peaple):
        if room[0] + 30 < arrival_times[last+1]:
            room.pop()
            last += 1
            room.appendleft(arrival_times[last])
    
        elif room[0] + 30 > arrival_times[last+1]:
            arrival_times
    


    pass

if __name__ == "__main__":
    
    # total room capacity
    room_capacity = int(input())
    
    # total vaccination time in minute
    start_time = ":".join(input().split("."))
    end_time = ":".join(input().split("."))
    total_time = total_minute(start_time, end_time)

    # total peaple came for vaccination
    total_peaple = int(input())

    # arrival time of different peaple
    arrival_times = list( map(int, input().split()) )
    arrival_times.sort()

    ans = total_vaccinated(room_capacity, total_peaple, total_time, arrival_times)
    print(ans, end="")