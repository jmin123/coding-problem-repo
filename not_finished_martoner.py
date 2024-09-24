"""
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
"""
def solution(participant, completion):
    answer = ''
    
    players = {}
    
    # 중복되는 문자열이 있을 수도 있으니 dict형태로 저장
    for player in participant:
        if player in players:
            players[player] += 1
        # 중복되는 문자열이 없으면 새로 추가
        else:
            players[player] = 1

    # completion에 player가 있으면 1씩 빼준다
    for player in completion:
        if player in players:
            # 값을 빼준다
            players[player] -= 1
            
    for player in players:
        # 만약 숫자가 0이 아니면 완주 못 했으므로
        if players[player] != 0:
            answer = player
            break

    return answer

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
