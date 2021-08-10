new_file = open("CupcakeInvoices.csv")

# for line in new_file:
#     print(line)

cupcake_type = []

for line in new_file:
    line = line.rstrip('\n').split(',')
    # print(int(line[3])* float(line[4]))
    # cupcake_type.append(line[2])
    # int(line[3])
    # float(line[4])

total = 0
for line1 in new_file:
    line = line1.rstrip('\n').split(',')
    total += (int(line[3]) * float(line[4]))

# print(total)


new_file.close()

import matplotlib.pyplot as plt


plt.plot(["chocolate","Vanilla","Vanilla",],[98,140,25])
plt.ylabel('Amount Sold')
plt.xlabel("Weekday")
plt.show()