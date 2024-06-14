def average(arr):
    distinct_heights = set(arr)
    
    total_height = sum(distinct_heights)
    
    average_height = total_height / len(distinct_heights)
    
    rounded_average = round(average_height, 3)
    
    return rounded_average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)