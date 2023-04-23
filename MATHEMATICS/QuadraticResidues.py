# tìm các số là thặng dư bình phương phương modulo p bt trong ints chỉ có 1 số là tdbp
p = 29
ints = [14, 6, 11]
Square_root = []
for item in ints: # Duyệt từng phần tử trong mảng
    for i in range(1,p): # xét từ 1 tới p - 1
        if i**2 % p == item: # nếu tồn tại i sao cho i^2 = item [p]
            Square_root.append(i) # append tất cả những square_root 

print(min(Square_root)) # Trả về số nhỏ nhất : 8

