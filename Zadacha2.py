# 18. *Реализуйте алгоритм перемешивания списка.

import random
list = [random.randint(0,5) for i in range(random.randint(3,10))]
print(f'исходный список:\n {list}')
random.shuffle(list)
print(f'список после перемешивания:\n{list}')

