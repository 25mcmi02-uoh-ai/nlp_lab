# given its, segment the phrase
text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
seg1 = "0000000000000001000000000010000000000000000100000000000"
seg2 = "0100100100100001001001000010100100010010000100010010000"

def segment(text,seg):
    words = []
    cursor = 0
    for i in range(len(seg)):
        if seg[i] == '1':
            words.append(text[cursor:i+1])
            cursor = i+1
    words.append(text[cursor:])
    return words

print(segment(text, seg1))
print(segment(text, seg2))

# given its, segment the phrase
text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
seg1 = "0000000000000001000000000010000000000000000100000000000"
seg2 = "0100100100100001001001000010100100010010000100010010000"

def segment(text,seg):
    words = []
    word = ""
    for i in range(len(seg)):
        if seg[i] == '1':
            word = word + text[i]
            words.append(word)
            word = ""
        else:
            word = word + text[i]
    word = word + text[-1]
    words.append(word)
    return words

print(segment(text, seg1))
print(segment(text, seg2))