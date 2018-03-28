max_col = 33
where = '402室'
where = where[:-1]
len = where.__len__()
row = where[len - 2] + where[len - 1]
col = where[:len - 2]
charIntMap = {'01': 'A', '02': 'B', '03': 'C', '04': 'D', '05': 'E', '06': 'F'}
col = int(col)
col = max_col - col + 1
print(str(col) + ' ' + row)
idx = charIntMap[row] + '' + str(col)
print(idx)
