import random


class Dataset:
    def __init__(self, data, target) -> None:
        self.data = data
        self.target = target

    def sizeofdata(self):
        data_size = [len(self.data), len(self.data[0])]
        target_size = [len(self.target), len(self.target[0])]
        return data_size, target_size

    def idx_data(self, idx):
        m = idx[0]
        n = idx[1]
        return self.data[m][n]


# data = [[random.randint(1, 40), random.randint(1, 30)]
#         for j in range(11) for i in range(15)]
data = []
for i in range(15):
    data_line = []
    for j in range(10):
        data_line.append(random.randint(1, 30))
    data.append(data_line)
print(data)

target = [[random.randint(0, 1)] for i in range(15)]
# print(target)

object = Dataset(data, target)
data_size, target_size = object.sizeofdata()
print("Size of data: ", data_size)
print("target size: ", target_size)

x, y = input("Enter the index: ").split(" ")
idx = [int(x), int(y)]
# print(idx)
print(object.idx_data(idx))
