import random
import string

# Initialize an empty list to store dictionaries
randomDictsList = []
# Initialize an empty list to store dictionaries
numOfDicts = random.randint(2, 10)
# Generate a random number of keys (1 to 26) for each dictionary, by the number of characters in the alphabet.
numOfKeys = random.randint(1, 26)

# Loop to create random dictionaries and append them to randomDictsList
for i in range(numOfDicts):
    values = []
    # Generate random lowercase letters
    keys = random.choices(string.ascii_lowercase, k=numOfKeys)
    # Generate random values (integers between 0 and 100) for each key
    for x in range(numOfKeys):
        values.append(random.randint(0, 100))

    # Create a dictionary by zipping keys and values, sorted by keys, and append to randomDictsList
    randomDictsList.append(dict(sorted(zip(keys, values))))

# Initialize a temporary dictionary to store processed data
tempDict = {}

# Loop through each dictionary in randomDictsList along with its index
for i, separatedDict in enumerate(randomDictsList):
    # Iterate over each key-value pair in the current dictionary
    for key, value in separatedDict.items():
        # Check if the key already exists in tempDict
        if key in tempDict:
            existingValue = tempDict[key]
            # Compare values and update tempDict accordingly
            if value > existingValue[0]:
                # Create a new value [value, dictionary number, flag indicating the presence of comparison]
                tempDict[key] = [value, i + 1, True]
                # If the values are equal, the result from the first dictionary will be taken.
            elif value == existingValue[0]:
                existingValue[2] = True
        else:
            # If the key is encountered for the first time, initialize its data in tempDict
            tempDict[key] = [value, i + 1, False]

# Initialize an empty dictionary for the final result
finalDict = {}

# Process data from tempDict to create the final dictionary with unique keys
for key, value in tempDict.items():
    # If there has been a comparison, the key is changed according to the condition
    # and the technical information is removed from the value.
    if value[2]:
        finalDict[f"{key}_{value[1]}"] = value[0]
    # If there was no comparison, the key remains unchanged, technical information is removed from the value
    else:
        finalDict[key] = value[0]
# Sort the final dictionary by keys and assign it back to finalDict
finalDict = dict(sorted(finalDict.items()))
# Print the final dictionary
print(finalDict)
