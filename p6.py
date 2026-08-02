# Convert the messy phone number into a clean number format with only digits


phone = "+49 (176) 123-4567"
print(phone.replace("+", "").replace("(", "").replace(")", "") .replace("-", ""))
