def solution(skill, skill_trees):
    answer = 0

    skill_stack = list(skill)

    for v in skill_trees:
        tmp = []
        is_ok = True
        cur_skill = list(v)

        for i in range(len(cur_skill)):
            if cur_skill[i] in skill_stack:
                tmp.append(cur_skill[i])

            if tmp != skill_stack[:len(tmp)]:
                is_ok = False
                break

        if is_ok:
            answer += 1

    return answer
