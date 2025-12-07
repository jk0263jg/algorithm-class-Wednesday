def solve_stairs():
    # 1. 사용자에게 계단 수 n을 입력받는다.
    try:
        n = int(input("계단의 개수를 입력하시오: "))
    except ValueError:
        print("올바른 숫자를 입력해주세요.")
        return

    # 예외 처리: 계단이 0 이하일 경우
    if n <= 0:
        print("계단의 수는 1 이상이어야 합니다.")
        return

    # 2. 동적계획법을 위한 DP 테이블 초기화 (인덱스 편의를 위해 n+1 크기 할당)
    # dp[i]는 i번째 계단을 오르는 방법의 수를 저장
    dp = [0] * (n + 1)

    # 초기값 설정 (Base Case)
    dp[1] = 1
    if n >= 2:
        dp[2] = 2

    # 3. 반복문을 이용한 Bottom-up 방식
    # 3번째 계단부터 n번째 계단까지 점화식 적용
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    # 4. 계산된 결과를 화면에 출력한다.
    print(f"{n}개의 계단을 오르는 방법의 수는 {dp[n]}가지입니다.")

# 프로그램 실행
if __name__ == "__main__":
    solve_stairs()