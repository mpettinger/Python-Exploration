print("""Welcome to the pig latin program! \n
Enter a few words and we will translate it into pig latin""")
input_string = input("Your input here: \n")
input_string_lower = input_string.lower()

string_list = input_string_lower.split()
output_list = []

def pig_translate(wordinput):
    wordoutput = ""
    worday = wordinput[0] + "ay"
    wordinput = wordinput[1::]
    wordoutput = wordinput + "-" + worday
    return wordoutput

for word in string_list:
    if word[0] in 'aeiou':
        output_list.append(word)
    if word[0] not in 'aeiou':
        output_list.append(pig_translate(word))
        

print(" ".join(output_list))