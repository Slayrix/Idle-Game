import operator as op

ops = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.truediv,
    ">": op.gt,
    ">=": op.ge,
    "<": op.lt,
    "<=": op.le,
    "=": op.eq,
    "!=": op.ne
}

list = [1, "<=", 0]

result = ops[list[1]](list[0],list[2])
print(result)