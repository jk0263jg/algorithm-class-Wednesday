import time

# 전역 테스트 데이터
TEST_VALUES = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

# ---------------------------
# 1) 함수 구현
# ---------------------------

def factorial_iter(n: int) -> int:
    """반복문으로 n! 계산 (n < 0이면 ValueError 발생)"""
    if n < 0:
        raise ValueError("음수는 팩토리얼을 계산할 수 없습니다.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_rec(n: int) -> int:
    """재귀로 n! 계산 (n < 0이면 ValueError 발생)"""
    if n < 0:
        raise ValueError("음수는 팩토리얼을 계산할 수 없습니다.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)


def run_with_time(func, n: int):
    """주어진 함수(func)를 n에 대해 실행하고 (결과, 경과시간) 반환"""
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    return result, end - start


# ---------------------------
# 2) 메뉴 기반 콘솔 UI
# ---------------------------

def menu():
    while True:
        print("\n📌 팩토리얼 계산기 (반복/재귀 비교)")
        print("1. 반복문으로 계산")
        print("2. 재귀로 계산")
        print("3. 두 방식 비교")
        print("4. 테스트 데이터 일괄 실행")
        print("5. 종료")

        choice = input("👉 메뉴를 선택하세요: ").strip()

        if choice == "5":
            print("프로그램을 종료합니다.")
            break

        elif choice in ["1", "2", "3"]:
            n_str = input("정수 n을 입력하세요: ").strip()
            if not n_str.isdigit():
                print("❌ 정수를 입력해야 합니다.")
                continue
            n = int(n_str)

            if choice == "1":
                try:
                    result, t = run_with_time(factorial_iter, n)
                    print(f"✅ 반복문 결과: {result}")
                    print(f"⏱ 실행 시간: {t:.8f}초")
                except ValueError as e:
                    print("❌ 오류:", e)

            elif choice == "2":
                try:
                    result, t = run_with_time(factorial_rec, n)
                    print(f"✅ 재귀 결과: {result}")
                    print(f"⏱ 실행 시간: {t:.8f}초")
                except ValueError as e:
                    print("❌ 오류:", e)

            elif choice == "3":
                try:
                    iter_result, iter_time = run_with_time(factorial_iter, n)
                    rec_result, rec_time = run_with_time(factorial_rec, n)
                    print("\n🔍 결과 비교")
                    print(f"반복문 결과: {iter_result}")
                    print(f"재귀 결과: {rec_result}")
                    print("✅ 일치 여부:", "✅ 일치" if iter_result == rec_result else "❌ 불일치")
                    print(f"반복문 실행 시간: {iter_time:.8f}초")
                    print(f"재귀 실행 시간: {rec_time:.8f}초")
                except ValueError as e:
                    print("❌ 오류:", e)

        elif choice == "4":
            print("\n📊 테스트 데이터 실행 결과")
            for n in TEST_VALUES:
                print("-" * 50)
                print(f"n = {n}")
                try:
                    iter_result, iter_time = run_with_time(factorial_iter, n)
                    rec_result, rec_time = run_with_time(factorial_rec, n)
                    match = "✅" if iter_result == rec_result else "❌"
                    print(f"반복문 결과: {iter_result}")
                    print(f"재귀 결과: {rec_result}")
                    print(f"결과 일치 여부: {match}")
                    print(f"반복문 시간: {iter_time:.8f}초")
                    print(f"재귀 시간: {rec_time:.8f}초")
                except RecursionError:
                    print("❌ 재귀 오류: RecursionError (너무 깊은 재귀)")
                except ValueError as e:
                    print("❌ 오류:", e)

        else:
            print("❌ 잘못된 입력입니다. 1~5 중에서 선택하세요.")


# ---------------------------
# 프로그램 시작점
# ---------------------------
if __name__ == "__main__":
    menu()
