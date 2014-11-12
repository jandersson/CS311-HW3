user_input = "hello /*world*/."
char_list = []
state = "start"
comment = ""
for char in user_input:
    char_list.append(char)
def parse(char):
    global state, comment
    if state is "start":
        if char is "/":
            state = "slash"
            return
    if state is "slash":
        if char is "/":
            state = "slash"
            return
        if char is "*":
            state = "comment"
            return
    if state is "comment":
        if char is "*":
            state = "comment-star"
            return
        comment += char
    if state is "comment-star":
        if char is "/":
            state = "start"
            return
        else:
            comment += "*"
            state = "comment"
            return
    
for char in char_list:
    print("state: " + state + " | next char: " + char)
    parse(char)
print("Comment: " + comment)    
