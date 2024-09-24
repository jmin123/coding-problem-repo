def solution(book_time):
    answer = 0
    sorted_book_time = sorted(book_time, key=lambda x: (x[0], x[1]))
    return answer