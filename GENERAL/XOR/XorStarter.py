
label = "label"
mask='13'
mask= bin(int(mask,10))[2:] #lấy giá trị binary của 13
li_binary_string=[] #list lưu giá trị bin của label

for x in range(0,5):
    binary_string = bin(ord(label[x]))[2:] 
    #lấy từng kí tự trong label -> chuyển thành kí tự unicode -> chuyển thành binary
    li_binary_string.append(binary_string)  # lưu từng kí tự vào list
flag=""

for x in li_binary_string:
#xor từng chuỗi binary của list với 13
    tmp=int(x,2)^int(mask,2)
    flag+=chr(tmp)
print(flag)
