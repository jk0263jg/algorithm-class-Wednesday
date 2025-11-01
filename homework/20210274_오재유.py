# 도서 관리 프로그램
# 학번_이름.py

class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"[책 번호: {self.book_id}, 제목: {self.title}, 저자: {self.author}, 출판 연도: {self.year}]"


class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

    def append(self, new):
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self):
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def append(self, book):
        new_node = Node(book)
        if self.isEmpty():
            self.head = new_node
        else:
            p = self.head
            while p.link is not None:
                p = p.link
            p.link = new_node

    def find_by_title(self, title):
        p = self.head
        while p is not None:
            if p.data.title == title:
                return p.data
            p = p.link
        return None

    def find_pos_by_title(self, title):
        prev = None
        p = self.head
        while p is not None:
            if p.data.title == title:
                return prev
            prev = p
            p = p.link
        return None

    def remove_by_title(self, title):
        if self.isEmpty():
            return False
        # 첫 번째 노드가 해당 도서일 때
        if self.head.data.title == title:
            self.head = self.head.link
            return True
        prev = self.find_pos_by_title(title)
        if prev is not None and prev.link is not None:
            prev.popNext()
            return True
        return False

    def find_by_id(self, book_id):
        p = self.head
        while p is not None:
            if p.data.book_id == book_id:
                return True
            p = p.link
        return False

    def display_all(self):
        if self.isEmpty():
            print("현재 등록된 도서가 없습니다.")
            return
        p = self.head
        while p is not None:
            print(p.data)
            p = p.link


class BookManagement:
    def __init__(self):
        self.books = LinkedList()

    def add_book(self, book_id, title, author, year):
        if self.books.find_by_id(book_id):
            print("중복된 책 번호입니다. 추가할 수 없습니다.")
            return
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        print(f"도서 '{title}'가 추가되었습니다.\n")

    def remove_book(self, title):
        if self.books.remove_by_title(title):
            print(f"책 제목 '{title}'의 도서가 삭제되었습니다.\n")
        else:
            print("해당 제목의 도서를 찾을 수 없습니다.\n")

    def search_book(self, title):
        book = self.books.find_by_title(title)
        if book:
            print(book, "\n")
        else:
            print("해당 제목의 도서를 찾을 수 없습니다.\n")

    def display_books(self):
        self.books.display_all()
        print()

    def run(self):
        while True:
            print("=== 도서 관리 프로그램 ===")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 프로그램 종료")
            menu = input("메뉴를 선택하세요: ")

            if menu == '1':
                book_id = input("책 번호를 입력하세요: ")
                title = input("책 제목을 입력하세요: ")
                author = input("저자를 입력하세요: ")
                year = input("출판 연도를 입력하세요: ")
                self.add_book(book_id, title, author, year)

            elif menu == '2':
                title = input("삭제할 책 제목을 입력하세요: ")
                self.remove_book(title)

            elif menu == '3':
                title = input("조회할 책 제목을 입력하세요: ")
                self.search_book(title)

            elif menu == '4':
                print("현재 등록된 도서 목록:")
                self.display_books()

            elif menu == '5':
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 입력입니다. 다시 선택하세요.\n")


if __name__ == "__main__":
    manager = BookManagement()
    manager.run()
