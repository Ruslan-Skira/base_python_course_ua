bool(32)
bool(0)
bool('')  # no any symbols

any([1, 2, 3])
any([1, 2, 3, ''])
all([1, 2, 3, ''])

# список ответов от пользователя
standart = [18, 'Mark', 'Engineer']

age, name, profession = input('Fill up your age, name, profession').split(', ')

condition_1: bool = int(age) == 18
condition_2: bool = name == 'Mark'
condition_3: bool = profession == 'Engineer'

print(all([condition_1, condition_2, condition_3]))
print(any([condition_1, condition_2, condition_3]))
