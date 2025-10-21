import unicodedata

def clean_international_text(text):
    # Normalize Unicode characters
    normalized = unicodedata.normalize('NFKD', text)
    # Remove non-ASCII characters
    ascii_text = normalized.encode('ASCII', 'ignore').decode('ASCII')
    return ascii_text


# Example with international text
text = "Café München — スシ"
clean_text = clean_international_text(text)
print(clean_text)  # Output: "Cafe Munchen  "
filenameIn="./Data/spam.csv"
output=clean_international_text(open(filenameIn, "r",encoding="ISO-8859-1").read())
filename="./Data/spam_clean.csv"
with open(filename, "w") as f:
    f.write(output)
    f.truncate()