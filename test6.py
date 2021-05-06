N = int(input("피자 조각 수를 입력하세요:")) #정수 N이 주어짐
 
cache = [1, 2]
for i in range(2, N): #2부터 N까지 반복
    cache.append(cache[i-2] + cache[i-1]) #숫자 1,2로 표현할 수 있는 (i-1),(i-2)의 경우의 수를 모두 더해줌
print(cache[N-1])
