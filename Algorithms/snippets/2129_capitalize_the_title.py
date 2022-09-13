def capitalize_title(title):
    title = title.split(" ")
    for w in range(len(title)):
        if len(title[w]) <= 2:
            title[w] = title[w].lower()
        else:
            title[w] = title[w][0].upper() + title[w][1:].lower()
    return ' '.join(w for w in title)

print(capitalize_title('capiTalIze tHe titLe'))