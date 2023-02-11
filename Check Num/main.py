def func(num):
    a = zip(['个', '十', '百', '千', '万'], [i for i in str(num)[::-1]])
    str_list = []
    for i, j in a:
        str_list.append(f'print("{i}位数是： {j}")')
    return '\n    '.join(str_list)


with open('checknum.py', 'w') as f:
    f.write('num = input("请输入一个不多于5的正整数： ")\n')
    f.write('num = int(num)\n\n')
    for i in range(100000):
        f.write(f"""if num == {i}:
    print("这个数是{len(str(i))}位数")
    {func(i)}
    print("倒过来数是{str(i)[::-1]}")
""")
