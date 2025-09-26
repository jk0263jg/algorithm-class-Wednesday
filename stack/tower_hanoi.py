#하노이 탑 문제 : 재귀적으로 문제 해결

def tower_hanoi(n, start, tmp, target):
    #1. 재귀 호출 종료(base case)
    if n == 1: #(base case)
        print(f"원반 {n}: {start} -> {target}")

    # 재귀 분할 호출
    else:
        # 위의  n-1개를 start -> tmp로 옮김(c 막대를 임시 보조)
        tower_hanoi(n-1, start, target, tmp)
        
        # 가장 큰 1개를 start -> target 으로 옮김
        print(f"원반 {n}: {start} -> {target}")

        # tmp에 놓여 있는 n-1개를 tmp-> target 옮김 (start 임시 보조)
        tower_hanoi(n-1, tmp, start, target) 

if __name__ == "__main__":
    n = int(input("원판의 개수를 입력해주세요: "))
    tower_hanoi(n, "A", "B", "C")

    total = ( 1 << n ) -1
    print(f"\n 총 이동 횟수: {total} (2^{n} -1)")