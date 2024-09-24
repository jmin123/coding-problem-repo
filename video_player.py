def solution(video_len, pos, op_start, op_end, commands):
    def change_time_to_sec(time):
        m, s = time.split(':')

        return int(m) * 60 + int(s)
    
    def change_sec_to_time(sec):
        m = sec // 60
        s = sec % 60

        return f"{m:02d}:{s:02d}"

    video_len = change_time_to_sec(video_len)
    pos = change_time_to_sec(pos)
    op_start = change_time_to_sec(op_start)
    op_end = change_time_to_sec(op_end)
    
    for command in commands:
        # If pos is between op_start and op_end, then move pos to op_end
        if op_start <= pos <= op_end:
            pos = op_end
        # If pos is less than 10 then pos is 0
        if command == "prev" and pos - 10 >= 0:
            pos -= 10
        elif command == "prev" and pos - 10 < 0:
            pos = 0
        elif command == "next" and pos + 10 <= video_len:
            pos += 10
        elif command == "next" and pos + 10 > video_len:
            pos = video_len
        # After calculate pos, check if pos is between op_start and op_end
        if op_start <= pos <= op_end:
            pos = op_end

    return change_sec_to_time(pos)

print(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"]))