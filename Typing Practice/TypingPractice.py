import os
import argparse
import random


if __name__ == '__main__':
    # Argument Parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length', type=int, default=64, help='Number of section (default: 64)')
    parser.add_argument('-i', '--interval', type=int, default=8, help='Section length (default: 8)')
    parser.add_argument('-n', '--number', action='store_true', default=False, help='Generate number or not')
    parser.add_argument('-s', '--special', action='store_true', default=False, help='Generate special characters or not')
    parser.add_argument('-c', '--capital', action='store_true', default=False, help='Generate capital letter or not')
    args = parser.parse_args()

    # Character pool
    chr_pool = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    if args.number:
        chr_pool += [f'{i}' for i in range(10)]

    if args.capital:
        chr_pool += [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    if args.special:
        chr_pool += [i for i in '`!@#$%^&*_+()[]{}:;,.<>|/\\\'\"']

    result = ''
    for i, _ in enumerate(range(args.length)):
        result += ''.join(random.sample(chr_pool, args.interval))
        result += ' '

        if (i + 1) % 8 == 0:
            result += '\n'
    print(result)

    with open('output.txt', 'w') as fp:
        fp.write(result)
