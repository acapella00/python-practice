print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요?") # Python,Java?무엇이 더 재밌을까요?
import sys
print("Python", "Java", file=sys.stdout) # 표준 출력
print("Python", "Java", file=sys.stderr) # 표준 에러
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
