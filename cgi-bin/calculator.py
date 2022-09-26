import sys


def cal(oprd1, oprd2, oprt):
    oprd1 = float(oprd1)
    oprd2 = float(oprd2)
    if oprt == '+':
        return oprd1 + oprd2
    elif oprt == '-':
        return oprd1 - oprd2
    elif oprt == '*':
        return oprd1 * oprd2
    elif oprt == '/':
        return oprd1 / oprd2


if __name__ == "__main__":
    c = cal(sys.argv[1], sys.argv[2])
    # print(c)
