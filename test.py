from collections import deque

def create_circular_list(items):
    circular_list = deque(items)
    return circular_list

# 示例用法
my_list = [1, 2, 3, 4, 5]
circular_list = create_circular_list(my_list)
circular_list.popleft()
print(circular_list[0])
# 输出循环列表中的元素
""" for _ in range(len(circular_list)):
    print(circular_list[0])
    circular_list.rotate(-2)  """ # 继续向左循环移动一个位置