string = '35, 35, 35, 35, 35, 35, 35, 35, '

normal = ''
normal_raw = string
if normal_raw != '':
    normal = [int(x) for x in normal_raw.strip(', ').split(',')]
proceed_normal = (normal, normal != '' and type(normal) != str)

print(proceed_normal)