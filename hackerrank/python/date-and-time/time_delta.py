from datetime import datetime

t = int(input())

for _ in range(t):
    t1 = input().strip()
    t2 = input().strip()
    
    format_string = "%a %d %b %Y %H:%M:%S %z"
    
    dt1 = datetime.strptime(t1, format_string)
    dt2 = datetime.strptime(t2, format_string)
    
    diff = dt1 - dt2
    
    print(int(abs(diff.total_seconds())))