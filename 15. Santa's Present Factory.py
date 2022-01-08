materials = [int(m) for m in input().split(' ')]
magics = [int(m) for m in input().split(' ')]

presents = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}

crafted_presents = {}

while materials and magics:
    c_material = materials.pop()
    c_magic = magics.pop(0)

    if c_material == 0 or c_magic == 0:
        if c_material != 0:
            materials.append(c_material)
        if c_magic != 0:
            magics.insert(0, c_magic)
    else:
        magic_level = c_magic * c_material

        if magic_level < 0:
            materials.append(c_material + c_magic)
        elif magic_level > 0:
            if magic_level in presents:
                c_present = presents[magic_level]
                if c_present in crafted_presents:
                    crafted_presents[c_present] += 1
                else:
                    crafted_presents[c_present] = 1
            else:
                c_material += 15
                materials.append(c_material)

is_pair_one = 'Doll' in crafted_presents and 'Wooden train' in crafted_presents
is_pair_two = 'Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents

if  is_pair_one or is_pair_two :
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print('Materials left: ' + ", ".join([str(m) for m in materials[::-1]]))
if magics:
    print(f'Magic left: ' + ", ".join([str(m) for m in magics[::-1]]))

crafted_presents = dict(sorted(crafted_presents.items(), key=lambda kvp: kvp[0]))

for toy_name, toy_count in crafted_presents.items():
    print(f'{toy_name}: {toy_count}')