count = 1.44
col_vo = 100
stroka = 50
simvol = 25
sim = 4# TODO Найдите количество книг, которое можно разместить на дискете
book = col_vo*stroka*simvol*sim
book /= (1024**2)
disk = count//book
print("Количество книг, помещающихся на дискету:",round(disk))
