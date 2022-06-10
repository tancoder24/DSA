def time(hr, min, add):
    if add > 60:
        min = add-60
        hr += 1 
    elif min+add > 60:
        hr += 1
        min = min + add - 60
    else:
        min += add

    return hr, min  

def total_vacinated(room_capacity, total_peaple, start_hr, start_min, end_hr, end_min, arrival_times):
    current_capacity = 0
    vaccinated = 0
    
    

    room = []



if __name__ == "__main__":
    
    room_capacity = int(input())
    start_hr, start_min = list( map(int, input().split(".")) )
    end_hr, end_min = list( map(int, input().split(".")) )
    
    # total peaple came for vaccination
    total_peaple = int(input())

    # arrival time of different peaple
    arrival_times = list( map(int, input().split()) )
    arrival_times.sort()

    ans = total_vacinated(room_capacity, total_peaple, start_hr, start_min, end_hr, end_min, arrival_times)
    print(ans, end="")
