data = {
    'chicken kabab': 100,
    'chilli chicken': 130,
    'chicken lolipop': 170,
    'briyani': 160,
    'fry piece briyani': 180,
    'roti': 20,
    'chicken curry': 120,
    'ice cream': 60,
    'water bottle': 20
}
for i in data:
    print(i.ljust(20),data[i])

prods =  input("Enter the products: ").split()
total = 0
for i in prods:
    if i in data:
        total += data[i]
        print(f'{i} = {data[i]}')
print(f'Total bill: {total}')
