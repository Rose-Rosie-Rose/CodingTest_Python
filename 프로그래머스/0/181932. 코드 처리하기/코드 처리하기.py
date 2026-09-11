def solution(code):
    ret = ""
    mode = 0
    idx = 0

    while idx < len(code):

        if code[idx] == "1":
            if mode == 0:
                mode = 1
            else:
                mode = 0

        else:
            if mode == 0 and idx % 2 == 0:
                ret += code[idx]

            elif mode == 1 and idx % 2 == 1:
                ret += code[idx]

        idx += 1

    if ret == "":
        return "EMPTY"

    return ret