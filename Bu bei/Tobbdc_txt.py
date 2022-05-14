import re

word_list = []
with open('text.txt', 'r') as f:
    str = f.read().lower()
    for line in str.split('\n'):
        patten = re.compile(r'([a-zA-Z]{3,})')
        word_list += patten.findall(line)

with open('output.txt', 'w') as f:
    a = [(f.write(f'{i}\n'), print(i)) for i in sorted(word_list)]
