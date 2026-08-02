# Convert the messy phone number into a clean number format with only digits like "00491761234567"

phone = "+49 (176) 123-4567"
print(phone.replace("+", "00").replace("(", "").replace(")", "") .replace("-", "").replace(" ", ""))
