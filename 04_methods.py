#split
sample_str = "This is a sample string"
str_split = sample_str.split()
print(str_split, type(str_split))
#join
join_str = " ".join(str_split)
print(join_str, type(join_str))
#count
count_a = sample_str.count('a')
print(count_a)
#strip
strip_str = "   devops is teached by shiva    "
print(strip_str.strip())