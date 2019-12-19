for r in range(1,101):
    if r % 7 == 0:
        continue
    elif r % 10 == 7:
        continue
    elif r // 10 == 7:
        continue
    else:
        print(r)
