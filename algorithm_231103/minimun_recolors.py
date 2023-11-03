def minimumRecolors(blocks: str, k: int) -> int:
    count = 0
    first_blocks = list(blocks[:k])
    check_blocks = []
    
    for i in range(len(blocks) - k+1):
        check_blocks = first_blocks[i:i + k]
        print(check_blocks)
        for j in range(1,k - 1):
            if check_blocks[j-1] == check_blocks[j]:
                count += 1
            else:
                continue
    return count

blocks = "WBBWBBWBW"
k = 7
print(minimumRecolors(blocks, k))