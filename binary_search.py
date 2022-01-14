# values = [1, 3, 5, 7, 9] # список значений, из которого угадываем; len = 5
# let_guess = 9 # загаданное значение
def binary_search(list, item):
    low = 0
    high = len(list)
    # low и high - индексы минимального и максимального значений;
    while low <= high:
        mid = (low + high) // 2 # "серединка" списка;
    # # принтим mid
    #     print(f'Середина - {list[mid]}; индекс - {mid}')
    #     input()
        # теперь предположим, что серединка - наше число, тогда:
        guess = list[mid] # в примере 1 это число - 5;
    # # принтим guess
    #     print('может это число...', guess)
    #     input()
        if guess == item:
            # это число, которое загадали;
            return guess
        elif guess >= item:
            high = mid # убираем неподходящую - большую часть списка;
        else: # случай, когда число, которое предположила программа меньше, 
              # чем загаданное
            low = mid # убираем меньшую часть списка.
    return None

# print(binary_search(values, let_guess))

# ASSERTION
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 
'Jupiter', 'Saturn', 'Uranus', 'Neptune']
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums2 = [2, 4, 6, 8, 10]
family = ['Mother', 'Sister', 'Grandpa', 'Grandmom']
assert binary_search(nums1, 7) == 7
assert binary_search(nums2, 3) == None
assert binary_search(planets, 'Pluto') == None
assert binary_search(family, 'Mother') == 'Mother'