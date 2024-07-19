heros=['spider man','thor','hulk','iron man','captain america']


print("1: ", len(heros) )


heros.append("black panter")
print("2: ", heros )


heros.pop()
heros.insert(3, "black panther")


print("3: ", heros )



heros[1:3] = ["doctor strange"]
print("4: ",heros )


heros.sort()

print("5: ",heros )