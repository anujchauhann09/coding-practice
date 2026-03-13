import re

pattern = r"(?<=[\:\, ])+[#]+([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})"

for _ in range(int(input())):
    line = input()
    res = re.findall(pattern, line)
    
    if res:
        [print("#"+i) for i in res]
    else:
        pass