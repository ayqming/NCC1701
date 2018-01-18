em_zimu = ["a","b","c",["1","2",["3"]]]
for zimu in em_zimu :
    if isinstance(zimu, list):
        for zimuinlist in zimu:
            print(zimuinlist)
    else:
        print(zimu)
print(zimu)
count = 0 
while count < len(em_zimu):
    print(em_zimu[count])
    count = count+1
print('j"/d/\"dddd\"ddddd"j')