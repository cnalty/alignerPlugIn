
# 1, 4, 7, etc is x | 2, 5, 8, etc is y | 3, 6, 9, etc is confidence
jsonArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 0 head, 1 collarbone, 2 3 4 right shoulder elbow hand, 5 6 7 left shoulder elbow hand
xPoints = []
yPoints = []
confidence = []
Index = 0

while Index < len(jsonArray):
    if Index % 3 == 0:
        xPoints.append(jsonArray[Index])

    if Index % 3 == 1:
        yPoints.append(jsonArray[Index])

    if Index % 3 == 2:
        confidence.append(jsonArray[Index])

    Index += 1


print(xPoints)
print(yPoints)
print(confidence)

