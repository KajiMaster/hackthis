source = "tis, could, your, its, not, than, them, him, can, almost, because, our, for, like, across, what, nor, either, \
          will, let, get, should, with, where, about, this, neither, whom, least, other, you, was, then, own, did, they\
          , says, cannot, his, any, dear, ever, why, after, rather, also, there, most"

def split_string(source, splitlist):
    splits = []
    output = []
#    print source
    count = -1
    for char in source:
        count += 1
        for chara in splitlist:
            if char == chara:
                splits.append(count)
    value = source[0:splits[0]]
    output.append(value)
 #   print splits
    for i in range(len(splits)-1):
        val1 = splits[i]
        val2 = splits[i+1]
        value = source[val1+1:val2]
        if value != '':
            output.append(value)
    val3 = splits[len(splits)-1]+1
    value = source[val3:len(source)]
    if value != '':
        output.append(value)

    return output


out = split_string(source, " ,")

out.sort()
new_line = ", ".join(out)

print new_line


