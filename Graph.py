h = dict()

def addParents(class_name, *parents):
    h[class_name] = parents

def isAncestor(ancestor, descendant):
    if ancestor == descendant:
        return True
    if ancestor in h[descendant]:
        return True
    for a in h[descendant]:
        if isAncestor(ancestor, a):
            return True
    return False

def toYesNo(b):
    return "Yes" if b else "No"

for _ in range(int(input())):
    parts = input().split(" : ")
    cl = parts[0]
    parents = [] if len(parts) == 1 else parts[1].split(" ")
    addParents(cl, *parents)

for _ in range(int(input())):
    parts = input().split(" ")
    a = parts[0]
    d = parts[1]
    print(toYesNo(isAncestor(a, d)))