import sys

raw_Id = input("Enter ID without Check Digit. must be 8 letter!: ")
str_Lenght = (len(raw_Id))
if str_Lenght != 8:
    sys.exit("Must enter 8 numbers")
else:
    print("Starting calculations\n")

id_list = []
for ind in range(8):

    if ind % 2 == 0:
        sum_digit1 = (int(raw_Id[ind]) * 1)
        id_list.append(sum_digit1)
    else:
        sum_digit2 = (int(raw_Id[ind]) * 2)
        if sum_digit2 >= 10:
            digit_s = str(sum_digit2)
            digit10 = (digit_s[0])
            digit11 = (digit_s[1])
            sum_digit3 = (int(digit10) + int(digit11))
            id_list.append(sum_digit3)
        else:
            id_list.append(sum_digit2)

id_sum = (sum(id_list))

id_check = (id_sum * 9) % 10
print(f"your check digit is {id_check}")
full_id = raw_Id + str(id_check)
print(f"Your full ID is {full_id}")
