import sys

result = 0
active = True


def handle_line(line):
    global result, active
    i = 0
    while i < len(line):
       
        if line[i] == '=':
            print(result)
            i += 1
        
        elif ((line[i] == '-') or line[i].isdigit()):
            
            sign = 1
            if line[i] == '-':
                sign = -1
                i += 1
           
            
            num = 0
            found_digit = False
            while i < len(line) and line[i].isdigit():
                found_digit = True
                num = num * 10 + int(line[i])
                i += 1
            if found_digit and active:
                result += sign * num
        
        elif line[i].isalpha():
            start = i
            while i < len(line) and line[i].isalpha():
                i += 1
            word = line[start:i].lower()  
            
            ###Maybe implement here a fuction to check if a string  has a on or off on it?

            if word == "on":
                active = True
            elif word == "off":
                active = False
           
        else:
           
            i += 1



for line in sys.stdin:
    handle_line(line)
