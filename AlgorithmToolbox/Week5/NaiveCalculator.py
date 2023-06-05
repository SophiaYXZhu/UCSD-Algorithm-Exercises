def click_seq(n):
    num_clicks = [0 for i in range(n + 1)]
    num_clicks[1] = 1
    for i in range(2, n + 1):
        idx = [i-1]
        if i % 2 == 0:
            idx.append(i // 2)
        if i % 3 == 0:
            idx.append(i // 3)
        min_clicks = min([num_clicks[x] for x in idx])
        num_clicks[i] = min_clicks + 1

    min_value = n
    click_seq = [min_value]
    while min_value != 1:
        prev_values = [min_value - 1]
        if min_value % 2 == 0:
            prev_values.append(min_value // 2)
        if min_value % 3 == 0:
            prev_values.append(min_value // 3)
        min_value = prev_values[0]
        for value in prev_values[1:]:
            if num_clicks[value] < num_clicks[min_value]:
                min_value = value
        click_seq.append(min_value)
    return reversed(click_seq)

n = int(input())
click_seq = list(click_seq(n))
print(len(click_seq)-1)
for x in click_seq:
    print(x, end = " ")