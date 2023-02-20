import requests


r = requests.get('https://stamp.family.com.tw/api/maps/MapClassificationInfo?ProjectCode=202106302')
family = r.json()
print(family)

riceball = family['data'][0]['categories']
rice = family['data'][1]['categories']
noodle = family['data'][2]['categories']
soup = family['data'][3]['categories']
sandwich = family['data'][4]['categories']
vegetable = family['data'][5]['categories']
bread = family['data'][6]['categories']
cake = family['data'][7]['categories']

cat = [riceball, rice, noodle, soup, sandwich, vegetable, bread, cake]
tag = ["riceball", "rice", "noodle", "soup", "sandwich", "vegetable", "bread", "cake"]

data_all = {}

for i in range(len(cat)):
    for x in cat[i]:
        x_list = x['products']
        for item in x_list:
            #tmp = [item['productCode'], item['productName']]
            #print(tmp)
            data_all.update( {item['productCode'] : item['productName']} )

print(data_all)
