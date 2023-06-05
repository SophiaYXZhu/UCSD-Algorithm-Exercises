def check_seq(seq):
    stack = []
    closing_idx = -1
    opening_idx = -1
    for i in range(len(seq)):
        if seq[i] in ["(", "{", "["]:
            stack.append(seq[i])
            opening_idx = i
        elif seq[i] in [")", "}", "]"]:
            if len(stack) == 0:
                closing_idx = i
                return closing_idx+1
            char = stack.pop(len(stack)-1)
            if seq[i] == ")" and char != "(" or \
                seq[i] == "}" and char != "{" or \
                    seq[i] == "]" and char != "[":
                closing_idx = i
                return closing_idx+1
            else:
                opening_idx -= 1
    if len(stack) == 0:
        return "Success"
    elif closing_idx != -1:
        return closing_idx+1
    return opening_idx+1

seq = input()
print(check_seq(seq))
