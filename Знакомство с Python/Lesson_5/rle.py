def encode(data):
    encoding = ""
    prev_char = data[0]
    count = 0
    for char in data:
        if char == prev_char:
            count +=1
        else:
            encoding += str(count) + prev_char
            count = 1
            prev_char = char
    
    encoding += str(count) + prev_char
    return encoding

def decode(enc_data):
    decode = ""
    count = ""
    for char in enc_data:
        if char.isdigit():
            count+=char
        else:
            decode += char * int(count)
            count = ""
    return decode