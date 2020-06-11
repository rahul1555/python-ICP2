text=open('fileA.txt','r')
counts=dict()
def word_count(text):
    words = text.read().split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

word_count(text)
text.close()
result =''
for word, count in counts.items():
    result += word + ':' +str(count) + '\n'
output_file =open('output.txt','w')
output_file.write(result)
output_file.close()