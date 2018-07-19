import markovify

with open("g.txt") as f:
    text = f.read()

text_model = markovify.Text(text)

for i in range(5):
    sne = text_model.make_sentence()
    sne = sne.lower().capitalize()
    print(sne)
