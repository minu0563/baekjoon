a = int(input())
count = 1
room = 1
room_count = 0

while True:
    room_count += 1
    
    if room < a:
        room += 6*room_count
        count += 1
    
    elif room >= a:
        print(count)
        break