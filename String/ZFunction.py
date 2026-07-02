def zFunction(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0

    for i in range(1, n):
        if i <= r:
            k = i - l

            z[i] = min(r - i + 1, z[k])

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1

    return z


def search(text, pattern):
    s = pattern + '$' + text
    z = zFunction(s)
    pos = []
    m = len(pattern)

    for i in range(m + 1, len(z)):
        if z[i] == m:

            pos.append(i - m - 1)

    return pos


if __name__ == '__main__':
    text = 'aabxaabxaa'
    pattern = 'aab'

    matches = search(text, pattern)

    for pos in matches:
        print(pos, end=' ')
