#Write code using find() and string slicing to extract
#the number at the end of the line below. Convert the
#extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";
startPos = text.find(":")+1
newText = text[startPos:]
newText = newText.strip()
num = float(newText)
print(num)
