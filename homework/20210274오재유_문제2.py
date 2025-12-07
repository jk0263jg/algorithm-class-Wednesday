def solve_knapsack():
    # 1. 물건 데이터 설정 (문제에 주어진 표)
    # (이름, 무게, 만족도)
    items = [
        ("노트북", 3, 12),
        ("카메라", 1, 10),
        ("책", 2, 6),
        ("옷", 2, 7),
        ("휴대용 충전기", 1, 4)
    ]
    n = len(items)

    # 2. 사용자에게 배낭 용량 W 입력받기
    try:
        W = int(input("배낭 용량을 입력 하세요 : "))
    except ValueError:
        print("올바른 숫자를 입력해주세요.")
        return

    # 3. 동적계획법 테이블 초기화 (행: 물건 개수+1, 열: 무게+1)
    # dp[i][w]는 i번째 물건까지 고려했을 때 무게 w에서의 최대 만족도
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Bottom-up 방식으로 테이블 채우기
    for i in range(1, n + 1):
        name, wt, val = items[i-1] # 현재 고려할 물건 (인덱스 조정)
        for w in range(1, W + 1):
            if wt > w:
                # 물건이 배낭 용량보다 무거우면 넣지 않음
                dp[i][w] = dp[i-1][w]
            else:
                # 넣지 않는 경우 vs 넣는 경우 중 큰 값 선택
                dp[i][w] = max(dp[i-1][w], val + dp[i-1][w-wt])

    # 4. 결과 출력: 최대 만족도
    max_satisfaction = dp[n][W]
    print(f"최대 만족도: {max_satisfaction}")

    # 5. 선택한 물건 역추적 (Backtracking)
    selected_items = []
    current_w = W
    
    for i in range(n, 0, -1):
        # 현재 값이 이전 단계 값과 다르다면, 해당 물건이 추가된 것임
        if dp[i][current_w] != dp[i-1][current_w]:
            name, wt, val = items[i-1]
            selected_items.append(name)
            current_w -= wt # 남은 용량 갱신

    # 보기 좋게 출력하기 위해 리스트 뒤집기 또는 정렬 (문제 예시는 순서 무관해 보이나 역순으로 찾았으므로)
    # 예시 출력처럼 리스트 형태로 출력
    print(f"선택된 물건: {selected_items[::-1]}") # 원래 순서대로 보려면 뒤집기

if __name__ == "__main__":
    solve_knapsack()