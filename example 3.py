n = int(input())
availableofficers = 0
untreatedcrime= 0

for _ in range(n):
    event = int(input())
    if event == -1:
        if availableofficers >0:
            availableofficers -=1
        else:
            untreated