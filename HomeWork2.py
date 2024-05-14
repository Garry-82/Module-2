# list_=["one", "two", "three", "four"]
# print(list_)
# for i in range(len(list_)):
#     list_[i] = ":)"
# print(list_)
#
# for i in range(1,11):
#     for j in range (1,11):
#         print(f"{i} * {j} = {i*j}")
#     print('----------')

cars_list=['BMW','MB','LADA','KIA','HONDA']
for i in cars_list:
    print("я езжу на автомобиле марки ", i)
cars_count = 0
for i in cars_list:
    cars_count += 10
    print("я ездил на ", cars_count," автомобилях марки ", i)