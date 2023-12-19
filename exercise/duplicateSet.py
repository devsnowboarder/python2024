# This is a test

Elements =list()

Elements.append("JAVA");
Elements.append("J2EE");
Elements.append("JSP");
Elements.append("SERVLETS");
Elements.append("JAVA");
Elements.append("STRUTS");
Elements.append("JSP");

print("test")

print(Elements)
ElementsSet = set()
for elm in Elements:
    if ElementsSet.add(elm):
        print("added ")

print(ElementsSet)

# print all the duplicate items
for elm in ElementsSet:
    if Elements.count(elm) > 1:
        print(elm)

print(" this is a test ")
for elm in set(Elements):
   # print(elm)
    if ( Elements.count(elm) > 1):
        print(elm)


