def fun(s):
    if s.count('@') != 1:
        return False
        
    username, rest = s.split('@')
    
    if rest.count('.') != 1:
        return False
    
    website, extension = rest.split('.')
    
    if not username or not website or not extension or len(extension) > 3:
        return False
    
    for c in username:
        if not (c.isalnum() or c == '_' or c == '-'):
            return False
    
    for c in website:
        if not (c.isalnum()):
            return False
            
    for c in extension:
        if not (c.isalpha()):
            return False
    
    return True
    
    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)