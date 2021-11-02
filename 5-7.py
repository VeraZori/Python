import json

res_json = []
with open("samples/text_7.txt", "r", encoding="utf-8") as f:
    av_profit = 0
    pr_sum = 0
    k = 0
    res = {}
    res_profit = {}
    for i in f:
        name, form, v, iz = i.split()
        pr = int(v) - int(iz)
        if pr >= 0:
            pr_sum += pr
            k = k + 1
        res[name] = pr
    res_json.append(res)
    av_profit = pr_sum / k
    res_profit["average_profit"] = av_profit
    res_json.append(res_profit)
print(res)
print(res_profit)
with open("task7.json", "w", encoding="utf-8") as f:
    json.dump(res_json, f)
