
### 컴퓨터에게 몇 가지 알려 줍시다.
출력해주세요 = print
범위 = range

################### 컴퓨터에게 일을 시켜 볼까요?
담는곳 = 0
끝수 = 10000000000000

출력해주세요("계산 시작합니다")
for i in 범위(1,끝수+1) :
    담는곳 = 담는곳 + i
    if i % 10000000 is 0 :
        얼마나했나 = 100*i/끝수
        출력해주세요(얼마나했나, "% 계산했어요")

출력해주세요("1부터", 끝수 , "까지 더하니 ", 담는곳)
출력해주세요("계산 끝났습니다.")