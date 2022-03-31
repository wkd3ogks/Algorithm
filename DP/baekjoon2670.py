n = int(input())
seq = []
maxSeq = []
for _ in range(n):
    num = float(input())
    seq.append(num)
    maxSeq.append(num)

for i in range(1, n):
    if seq[i] * maxSeq[i - 1] >= maxSeq[i]:
        maxSeq[i] = seq[i] * maxSeq[i - 1]
print("%.3f" % max(maxSeq))