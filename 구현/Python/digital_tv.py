from collections import deque

def main():
    n = int(input())
    channels = deque()
    
    for _ in range(n):
        channels.append(input().strip())
    
    operations = []
    arrow = 0
    
    def move_arrow(target_idx):
        nonlocal arrow
        while arrow < target_idx:
            operations.append('1')
            arrow += 1
        while arrow > target_idx:
            operations.append('2')
            arrow -= 1
         
    def swap_up():
        nonlocal arrow
        # 0이면 더 이상 올라갈 수 없으니 예외문 처리
        if arrow == 0:
            return
        
        channels[arrow], channels[arrow-1] = channels[arrow-1], channels[arrow]
        operations.append('4')
        arrow -= 1
    
    def swap_down():
        nonlocal arrow
        # 채널 개수를 넘어갈 순 없으니
        if arrow >= len(channels) - 1:
            return 0
        
        channels[arrow], channels[arrow+1] = channels[arrow+1], channels[arrow]
        operations.append('3')
        arrow += 1
     
    
    kbs1_idx = channels.index('KBS1')
    
    move_arrow(kbs1_idx)
    
    while arrow != 0:
        swap_up()
     
    kbs2_idx = channels.index('KBS2')

    if kbs2_idx != 1:
        move_arrow(kbs2_idx)
        while arrow < 1:
            swap_down()
        while arrow > 1:
            swap_up()
    
    print(''.join(operations))
    
if __name__ == "__main__":
    main()