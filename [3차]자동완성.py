def solution(words):
    answer = 0
    
    # 단어들을 사전 순으로 정렬해놓기
    sorted_words = sorted(words)
    n = len(sorted_words)
    
    for i in range(n):
        current_word = sorted_words[i]
        prefix_length = 0
        
        if i > 0:
            prev_word = sorted_words[i-1]
            current_length = 0
            
            # 비교해서 같은 거면 더해주고
            for a, b in zip(prev_word, current_word):
                if a == b:
                    current_length += 1
                else:
                    break
            
            # 이전, 다음 단어들 중 중복되는 게 더 많은 게 있는지 또 비교
            prefix_length = max(current_length, prefix_length)
            
        if i < n - 1:
            next_word = sorted_words[i+1]
            current_length = 0
            
            for a, b in zip(next_word, current_word):
                if a == b:
                    current_length += 1
                else:
                    break
            
            prefix_length = max(current_length, prefix_length)

        if prefix_length < len(current_word):
            answer += prefix_length + 1
        else:
            answer += len(current_word)
    return answer

# 테스트 케이스
print(solution(["go","gone","guild"]))            # 예상 출력: 7
print(solution(["abc","def","ghi", "jklm"]))      # 예상 출력: 4
print(solution(["word","war","warrior","world"])) # 예상 출력: 15