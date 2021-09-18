# input
matrix = [
    [89, 7921, 96],
    [72, 5184, 74],
    [94, 8836, 87],
    [69, 4761, 78]
]

feature1 = [matrix[i][0] for i in range(4)]
feature2 = [i**2 for i in feature1]
feature = [feature1, feature2]

# mean
def m(li):
    ans = sum(li)/len(li)
    print('mean = '+ str(ans))
    return ans

# range
def r(li):
    ans = max(li) - min(li)
    print('range = '+str(ans))
    return ans

# normalize
def nm(i, j, method):
    # 1-index --> 0-index
    i-=1
    j-=1
    global matrix
    global feature
    val = matrix[i][j]
    print('value = ' + str(val))

    # method: mean/range/both
    if method == 'm' or method == 'b':
        val -= m(feature[j])
    if method == 'r' or method == 'b':
        val /= r(feature[j])
    return val

print('normalized feature = ' + str(nm(int(input('i: ')),int(input('j: ')),input('m/r/b: '))))