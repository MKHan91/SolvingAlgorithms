import re

def solution(new_id):
    answer = ''

    new_id = new_id.lower()
    new_id = "".join(char for char in new_id if char in "-_.abcdefghijklmnopqrstuvwxyz1234567890")
    
    p = re.compile("\.\.+")
    while re.findall(p, new_id):
        for expr in re.findall(p, new_id):
            new_id = new_id.replace(expr, ".")

    if new_id != "":
        if new_id[0] == ".":
            new_id = new_id.strip(".")
            if new_id == "":
                new_id += "a"
                
        if new_id[-1] == ".":
            new_id = new_id.strip(".")
    else:
        new_id += "a"
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id.strip(".")
    
    if len(new_id) <= 2:
        new_id += (new_id[-1] * (3 - len(new_id)))
    
    answer = new_id
    return answer

def solution2(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

if __name__ == "__main__":
    # new_id = "abcdefghijklmn.p"
    new_id = "....!@B.a.T...#*......y.abcde..fgh....ij........klm......................."
    # new_id = ""
    result = solution(new_id)
    print(result)