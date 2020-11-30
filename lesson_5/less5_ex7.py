import json
with open('text_7.txt', encoding='utf-8') as f_obj:
    n = 0
    all_profit=0
    us_dict={}
    list2 = []
    for line in f_obj:
        line1 = line.split()
        profit = int(line1[2]) - int(line1[3])
        if profit > 0:
            all_profit += profit
            dict2 = {}
            n += 1
            dict1 = {line1[0]:profit}
            us_dict.update(dict1)
        else:
            dict1 = {line1[0]:(str(profit) + ' убытки')}
            us_dict.update(dict1)

    average_profit = all_profit/n
    print(int(average_profit))
    res_list=[us_dict,{'average_profit':average_profit}]
    print(us_dict)
    print(res_list)
with open('text_7.json', 'w', encoding='utf-8') as output:
    json.dump(res_list, output)

