import random

mobile_list=[
  {'Name':'Iphone 22','Price': 150000},
  {'Name':'Nokia 25','Price': 70000},
  {'Name':'Samsung 26','Price': 250000},
  {'Name':'Huwai 27','Price': 70000},
  {'Name':'Xiaomi 8','Price': 120000},
  {'Name':'Walton 9','Price': 100000},
]

for mobile in mobile_list:
  text= [
    f'{mobile.get("Name")} Price is {mobile.get("Price")} BDT. ',
    f'The Price of {mobile.get("Name")} mobile is {mobile.get("Price")} BDT. '
    ]
  print(random.choice(text))