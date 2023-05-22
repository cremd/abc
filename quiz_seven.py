#字典如何删除键和合并两个字典

a={"name":"lihua","age":"18"}
print(f"原本的字典是{a}")
del a["age"]
print(f"删除年龄后的字典{a}")
b={"shenggao":"180"}
b.update(a)
print(f"合并后字典是{b}")

