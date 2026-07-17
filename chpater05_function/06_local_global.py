# 지역 변수
gun = 10

def checkpoint(soldiers): # 경계 근무
    gun = 20 # 지역 변수
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun)) # 18로 지역변수에서 2개 제외

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun)) #결과값은 10으로 외부 변수에 영향이 없기에 10

# 전역 변수
gun = 10

def checkpoint(soldiers): # 경계 근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun)) 

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun)) 

# return 사용 (권장)
gun = 10

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))