def alternate_string(text):
    combined_letters = [];
    
    for idx in range(len(text)):
        if idx % 2:
            combined_letters.append(text[idx].upper())
        else:
            combined_letters.append(text[idx].lower())

    return "".join(combined_letters)

print(alternate_string("odunayo"))

