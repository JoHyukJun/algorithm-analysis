def solution(dirs):
    answer = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    cur = [[0, 0]]
    visit = []

    for i in range(len(dirs)):
        tmp = []
        vtmp = []

        if dirs[i] == 'U':
            tmp.append(cur[-1][0] + dx[2])
            tmp.append(cur[-1][1] + dy[2])

            if tmp[1] > 5:
                continue

            vtmp.append(cur[-1])
            vtmp.append(tmp)

            cur.append(tmp)

            if vtmp in visit:
                continue
            else:
                answer += 1
                visit.append(vtmp)
                visit.append(vtmp[::-1])

        elif dirs[i] == 'D':
            tmp.append(cur[-1][0] + dx[3])
            tmp.append(cur[-1][1] + dy[3])

            if tmp[1] < -5:
                continue

            vtmp.append(cur[-1])
            vtmp.append(tmp)

            cur.append(tmp)

            if vtmp in visit:
                continue
            else:
                answer += 1
                visit.append(vtmp)
                visit.append(vtmp[::-1])

        elif dirs[i] == 'R':
            tmp.append(cur[-1][0] + dx[0])
            tmp.append(cur[-1][1] + dy[0])

            if tmp[0] > 5:
                continue

            vtmp.append(cur[-1])
            vtmp.append(tmp)

            cur.append(tmp)

            if vtmp in visit:
                continue
            else:
                answer += 1
                visit.append(vtmp)
                visit.append(vtmp[::-1])

        elif dirs[i] == 'L':
            tmp.append(cur[-1][0] + dx[1])
            tmp.append(cur[-1][1] + dy[1])

            if tmp[0] < -5:
                continue

            vtmp.append(cur[-1])
            vtmp.append(tmp)

            cur.append(tmp)

            if vtmp in visit:
                continue
            else:
                answer += 1
                visit.append(vtmp)
                visit.append(vtmp[::-1])

    return answer
