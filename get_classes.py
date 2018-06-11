image_ids=[]
with open('annotations/trainval.txt') as f:
    lines = f.readlines()
    for x in lines:
        image_ids.append(x.split(' ')[0][:x.split(' ')[0].find('_')])

classes = list(set(image_ids))
classes.sort()

for x in classes:
    print(x)
print(classes)
print(len(classes))