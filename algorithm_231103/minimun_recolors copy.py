def minimumRecolors(blocks: str, k: int) -> int:
    min_cnt = k
    # 앞 기준
    for i in range(len(blocks) - k + 1):
        cnt = blocks[i:i+k].count("W")
        min_cnt = min(cnt, min_cnt)
    return min_cnt

    # 뒤 기준
    # for i in range(len(blocks) - k, len(blocks) + 1):
    #     cnt = blocks[i-k:i].count("W")
    #     min_cnt = min(cnt, min_cnt)
    # return min_cnt

blocks = "WBBWBBWBW"
k = 7
print(minimumRecolors(blocks, k))