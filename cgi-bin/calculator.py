import sys


def cal(oprd1, oprd2, oprt):
    oprd1 = float(oprd1.rstrip())
    oprd2 = float(oprd2.rstrip())
    oprt = oprt.rstrip()
    if oprt == '+':
        return oprd1 + oprd2
    elif oprt == '-':
        return oprd1 - oprd2
    elif oprt == '*':
        return oprd1 * oprd2
    elif oprt == '/':
        return oprd1 / oprd2


if __name__ == "__main__":
    answer = cal(sys.argv[1], sys.argv[2], sys.argv[3])
    print(answer)
