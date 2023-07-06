import sys
sys.setrecursionlimit(1000000)


class Joseph:
    def __init__(self, total_number, interval):
        self.total_number = total_number
        self.interval = interval

    def method1(self) -> int:  # 列表
        people_list = [i for i in range(0, self.total_number)]
        list_counter = 0
        interval_counter = 0
        while (len(people_list) > 1):
            interval_counter += 1
            if interval_counter == self.interval:
                people_list.pop(list_counter)
                interval_counter = 0
            else:
                list_counter += 1
            if (list_counter >= len(people_list)):
                list_counter = 0
        return people_list[0]

    def method2(self, total_number, interval) -> int:  # 递归
        if total_number == 0:
            return 0
        counter = self.method2(total_number-1, interval)
        return (interval+counter) % total_number

    def method3(self) -> int:  # 递推
        counter = 0
        for i in range(2, self.total_number + 1):
            counter = (counter + self.interval) % i
        return counter


if __name__ == "__main__":
    total_number = int(input("Please enter the total number:"))
    interval = int(input("Please enter the interval:"))
    solution = Joseph(total_number=total_number, interval=interval)
    print(solution.method3())
    assert solution.method3() == solution.method1()
    assert solution.method3() == solution.method2(total_number, interval)
