my_big_list = ["A", "A", "C", "B", "B", "A", "D", "F"]

no_dupes = set(my_big_list)
print(no_dupes)

no_dupes = list(no_dupes)
print(no_dupes)

for item in no_dupes:
    print(item, "x", my_big_list.count(item))


inventory = {"potions" : 3, "sword" : 0}

print(inventory.get("sword"))
for i in inventory:
    if int(inventory.get(i)) > 0:
        print(i)