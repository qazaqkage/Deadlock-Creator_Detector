import creator
deadlock_creator = creator
class DeadlockDetection:
    def __init__(self):
        self.processes = None
        self.resources = None
        self.max = None
        self.allocate = None
        self.need = None
        self.available = None

    def input(self):
        print("Enter no. of processes: ")
        self.processes = int(input())
        print("Enter no. of resources: ")
        self.resources = int(input())

        self.need = [[0] * self.resources for _ in range(self.processes)]
        self.max = [[0] * self.resources for _ in range(self.processes)]
        self.allocate = [[0] * self.resources for _ in range(self.processes)]
        self.available = [0] * self.resources

        print("Enter allocation matrix -->")
        for i in range(self.processes):
            for j in range(self.resources):
                self.allocate[i][j] = int(input())

        print("Enter max matrix -->")
        for i in range(self.processes):
            for j in range(self.resources):
                self.max[i][j] = int(input())

        print("Enter available matrix -->")
        for j in range(self.resources):
            self.available[j] = int(input())

    def show(self):
        print("Processes Allocation Max Available")
        for i in range(self.processes):
            print(f"P{i+1}")
            print("       ")
            for j in range(self.resources):
                print(f"  {self.allocate[i][j]}")
            print("       ")
            for j in range(self.resources):
                print(f"  {self.max[i][j]}")
            print("       ")
            if i == 0:
                for j in range(self.resources):
                    print(f"  {self.available[j]}")

    def call(self):
        finish = [0] * 100
        dead = [0] * 100

        for i in range(self.processes):
            for j in range(self.resources):
                self.need[i][j] = self.max[i][j] - self.allocate[i][j]

        flag = 1
        while flag == 1:
            flag = 0
            for i in range(self.processes):
                c = 0
                for j in range(self.resources):
                    if finish[i] == 0 and self.need[i][j] <= self.available[j]:
                        c += 1
                        if c == self.resources:
                            for k in range(self.resources):
                                self.available[k] += self.allocate[i][j]
                            finish[i] = 1
                            flag = 1
                            if finish[i] == 1:
                                i = self.processes
                                break

        j = 0
        flag = 0
        for i in range(self.processes):
            if finish[i] == 0:
                dead[j] = i
                j += 1
                flag = 1

        if flag == 1:
            print("\n\nSystem is in Deadlock and the Deadlock process are\n")
            for i in range(j):
                print(f"P{dead[i]}")
        else:
            print("No deadlock occurs")


if __name__ == '__main__':
    dd = DeadlockDetection()
    dd.input()
    dd.show()
    dd.call()