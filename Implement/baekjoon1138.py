# [Silver 2] 한 줄로 서기
n = int(input())
people = list(map(int, input().split()))
peopleSort = []
result = []
for p in range(len(people)):
    peopleSort.append((p + 1, people[p]))
peopleSort.sort(key=lambda x:-x[0])
for height, rank in peopleSort:
    if not result:
        result.append(height)
    else:
        for i in range(len(result)):
            if i == rank:
                if result[i] > height:
                    result.insert(i, height)
                    break
                else:
                    result.insert(i, height)
                    break
            if i + 1 == rank and i == len(result) - 1:
                result.append(height)
             
for i in result:
    print(i, end=' ')



