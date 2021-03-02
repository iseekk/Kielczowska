with open(f"Wojtek-debts.txt", "r") as f:
    lines = [i[:-1].split() for i in f.readlines()]

with open(f"Wojtek-debts.txt", "w") as f:
    dic = {}
    if lines:
        dic = {k: v for k, v in lines}
    dic["Iza"] = 2532
    dic["Natalia"] = 10
    for k, v in dic.items():
        f.write(f"{k} {v}\n")
