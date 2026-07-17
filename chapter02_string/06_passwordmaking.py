url = "http://naver.com"
my_str = url.replace("http://", "")

# print(my_str)
my_str = my_str[:my_str.index(".")] #my_str에서 처음부터 .이 처음등장하는 위치까지 끊을 것 즉, my_str[0:5] -> 0~5 직전까지(0, 1, 2, 3, 4)

# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))


url = "http://youtube.com"
my_str = url.replace("http://", "")
# print(my_str)
my_str = my_str[:my_str.index(".")] #my_str에서 처음부터 .이 처음등장하는 위치까지 끊을 것 즉, my_str[0:5] -> 0~5 직전까지(0, 1, 2, 3, 4)
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))
