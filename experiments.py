# items = [{'name':'Ali'}, {'age':22}, {'birth date':2004}]
# answer = input('')
# for i in items:
#     for k,v in i.items():
#         print(f"{k}: {v}")

items = [{'name': 'Ali'}, {'age': 22}, {'birth date': 2004}]

for i in items:
    input("Press Enter to see next item...")
    for k, v in i.items():
        print(f"{k}: {v}")