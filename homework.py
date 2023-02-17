# Excercise 1
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

def filter_out(strings):
    if strings == ' ':
        return False
    elif strings == '':
        return False
    elif strings == '  ':
        return False
    else:
        return True

print(list(filter(filter_out, places)))

# Excercise 2
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

author.sort(key=lambda last: last.split()[-1].lower())

print(author)

# Excercise 3
# F = (9/5)*C + 32

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

#lambda num: (9/5)*num + 32

new_list = list(map(list, places))
  
new_list[0].pop()
new_list[1].pop()
new_list[2].pop()
new_list[3].pop()

newer_list = new_list[0]+new_list[1]+new_list[2]+new_list[3]

variables = list(map(lambda var: (9/5) * var[1] + 32, places))

final_list = list(zip(newer_list, variables))

print(final_list)