
# Turn the messy string into a single clean summary with name, role, and age to "name: maria | role: data engineer | age: 27"

data = "968-Maria, ( D@t@ Engineer );; 27y.."
print(data.replace("@", "a").replace("968-", "name: ").replace("( ", "| role: ").replace(");;", "| age:").replace("y..", "").replace(",", "").lower())
