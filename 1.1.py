# def searchChildren(classes, parent, child):
#
#     if parent == child:
#         return True
#
#     if child in classes[parent]:
#         return True
#
#     for grandparent in classes[parent]:
#         if searchChildren(classes, grandparent, child):
#             return True
#     return False



def searchChildren(classes, parent, child):

    if parent == child:
        return 0

    if len(classes[parent]) == 0:
        return 0

    if child in classes[parent]: # тут unhashable type: 'list'
        return 1

    for grandparent in classes[parent]:
        return 1 * searchChildren(classes, grandparent, child)
    return 1


lst = []
classes = dict()

n = int(input())
for i in range(n):
    line = input().split(" ")
    if ':' in line:
        for i in range(2, len(line)):
            if classes.get(line[0]) is not None:
                classes[line[0]] += [line[i]]
            else:
                classes[line[0]] = [line[i]]
            if classes.get(line[i]) is None:
                classes[line[i]] = []
    else:
        for i in range(len(line)):
            classes[line[i]] = []

n = int(input())
for i in range(n):
    line = input().split()
    lst += [(searchChildren(classes, line[1], line[0]))]

# print(classes)
for i in range(len(lst)):
    if lst[i] == 0:
        print("Yes")
    else:
        print("No")

