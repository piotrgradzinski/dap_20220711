day_of_leaving_shoes = int(input("Provide the number of a day shoes were left: "))
day_of_repair = int(input("Provide how many days the repair will take: "))
day_of_taking_shoes = day_of_leaving_shoes + day_of_repair

# how can we get rid of all of the 'ifs' (using a list)
#        0          1         2            3           4        5           6
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# print(days[day_of_taking_shoes - 1])
print(f"Take shoes back on {days[day_of_taking_shoes - 1]}")

# if day_of_taking_shoes == 1:
#     print(f"Take shoes back on Monday") # 0
# elif day_of_taking_shoes == 2:
#     print(f"Take shoes back on Tuesday") # 1
# elif day_of_taking_shoes == 3:
#     print(f"Take shoes back on Wednesday")
# elif day_of_taking_shoes == 4:
#     print(f"Take shoes back on Thursday")
# elif day_of_taking_shoes == 5:
#     print(f"Take shoes back on Friday")
# elif day_of_taking_shoes == 6:
#     print(f"Take shoes back on Saturday")
# elif day_of_taking_shoes == 7:
#     print(f"Take shoes back on Sunday")