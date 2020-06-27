def get_score(l):
    scoreSystem = {1: 40, 2: 100, 3: 300, 4: 1200}
    score = 0
    level = 0
    lines = 0
    for i in l:
        lines += i
        score += (level + 1) * scoreSystem[i]
        if int(lines / 10) > level:
            level += 1
    return score


print(get_score([4, 2, 2, 3, 3, 4, 2]))
