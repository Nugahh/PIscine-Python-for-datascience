ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"
ft_tuple = ("Hello", "France!")
# ft_set = {"Hello", "Paris!"}
ft_set.remove("tutu!")
ft_set.add("Paris!")
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)

sorted_set = sorted(ft_set)
formatted_set = f"{{'{sorted_set[0]}', '{sorted_set[1]}'}}" # Manually format the output
print(formatted_set)
print(ft_dict)