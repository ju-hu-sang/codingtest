def count_visible(trophies):
    count = 0
    max_height = 0
    for height in trophies:
        if height > max_height:
            count += 1
            max_height = height
    return count

N = int(input())
trophies = [int(input()) for _ in range(N)]

left_visible = count_visible(trophies)

right_visible = count_visible(trophies[::-1])

print(left_visible)
print(right_visible)