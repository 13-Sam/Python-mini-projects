name = input("What is your name? ")
crush_name = input("What is your crush name? ")
new_name = name.lower()
new_crush_name = crush_name.lower()

total_name = new_name + new_crush_name
t_count = total_name.count("t")
r_count = total_name.count("r")
u_count = total_name.count("u")
e_count = total_name.count("e")

true_sum = t_count + r_count + u_count + e_count

l_count = total_name.count("l")
o_count = total_name.count("o")
v_count = total_name.count("v")
e_count = total_name.count("e")

love_sum = l_count + o_count + v_count + e_count

percent_of_love = str(true_sum) + str(love_sum)

print(f"percent_of_love: {percent_of_love}%")
new_percent_of_love = int(percent_of_love)

if new_percent_of_love < 10 or new_percent_of_love > 90:
    print(f"Your score is {percent_of_love}, you go together like coke and mentos.")
elif 40 < new_percent_of_love < 50:
    print(f"Your score is {percent_of_love}, you are alright together.")
else:
    print(f"Your score is {percent_of_love}")
