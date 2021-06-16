def sum(upstream):
    get = upstream['get']
    return get[0] + get[1]


def multiply(upstream):
    get = upstream['get']
    return get[0] * get[1]


def combine(upstream):
    sum_ = upstream['sum']
    multiply_ = upstream['multiply']
    return sum_ * multiply_
