n = int(input())
set1 = set(map(int, input().split()))
set2 = None

numofOperation = int(input())

for _ in range(numofOperation):
    command = input().split()

    match command[0]:
        case 'intersection_update':
            set2 = set(map(int, input().split()))
            set1.intersection_update(set2)
            
        case 'update':
            set2 = set(map(int, input().split()))
            set1.update(set2)
            
        case 'symmetric_difference_update':
            set2 = set(map(int, input().split()))
            set1.symmetric_difference_update(set2)
            
        case 'difference_update': 
            set2 = set(map(int, input().split()))
            set1.difference_update(set2)
                
    
print(sum(set1))
        
    
        
        
        