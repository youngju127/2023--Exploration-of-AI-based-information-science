import numpy as np

#python list
mid = [10, 20, 30]
final = [90, 80, 70]
#numpy array
mid_scores = np.array(mid)
final_scores = np.array(final)

total = list()
avg = list()

print(mid_scores)
print(type(mid), type(mid_scores))
for i in range(len(mid)):
    total.append(mid[i] + final[i])
    avg.append(total[i]/2)
print(f"Total : {total}")
print(f"Average : {avg}")