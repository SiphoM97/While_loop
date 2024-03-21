#Example 1
# i = 1
# while i <= 10:
#    print(i)
#    i += 1
#    print("done with loop")

#Example 2:
shoes = ["air max", "air force1", "jordan 3", "jordan 1", "yeezy desert boots", "fear of gods1"]
shoe_i_want = "yeezy desert boots"

length = len(shoes)
count = 0
while count < length:
    print(shoes[count])

    if shoes[count] == shoe_i_want:
        print("placing order online for shoe")
        break
count += 1