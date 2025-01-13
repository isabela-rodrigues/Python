# s - início da casa
# t - fim da casa
# a - posição da árvore de maçã
# b - posição da árvore de laranja
# m - quantidade de maçãs que caíram
# n - quantidade de laranjas que caíram
# apples - posição onde cada maçã caiu
# oranges - posição onde cada laranja caiu


def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apple = 0
    count_orange = 0

    for apple in apples:
        soma_apple = a + apple
        if soma_apple <= t and soma_apple >= s:
            count_apple += 1
    print(count_apple)
    for orange in oranges:
        soma_orange = b + orange
        if soma_orange <= t and soma_orange >= s:
            count_orange += 1
    print(count_orange)