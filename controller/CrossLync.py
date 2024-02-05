# # a = "s"+3
# # print(a)

d = {"b":[1,2,3,4]}
e={k:sum(v) for k,v, in d.items()}
# e = {i:sum(d.get(i)) for i in d}

print(e)


input = "aabbbppadde"
output="a2b3p2a1d2e1"

# dict={}
# lastchar =""
# op=""
# for i in input:
#     if i in dict:
#         dict[i] = dict.get(i)+1
#     else:
#         dict[i] = 1
    
#     if lastchar == i:
#         ts = f"{i}{dict.get(i)}"
#     else:
#         op = f"{op}{ts}"

    
#     lastchar = i
        
# print(op)

# # op = []
# # count=0
# # op=""
# # lastchar = ""
# # for i in input:
# #     count+=1 #1
    
# #     if lastchar == i: # ""==a
# #         #
# #     elif count > 1:
# #         op = f"{op}{count}"
# #     else:
# #         op = op+i



# def compress_string(input_str):
#     if not input_str:
#         return ""

#     compressed_str = ""
#     current_char = input_str[0]
#     char_count = 1

#     for i in range(1, len(input_str)):
#         active_char = input_str[i]
#         if active_char == current_char:
#             char_count += 1
#         else:
#             compressed_str += current_char + str(char_count)
#             current_char = active_char
#             char_count = 1

#     compressed_str += current_char + str(char_count)

#     return compressed_str

# input_str = "aabbbppadde"
# output_str = compress_string(input_str)
# print(output_str)
# 