def editDistance(text, target):
    lenText = len(text)
    lenTarget = len(target)

    # Initialize DP values
    dp = [[0] * (lenText+1) for _ in range(lenTarget + 1)] 

    for i in range(1, lenTarget):
        dp[i][0] = i
    for j in range(1, lenText):
        dp[0][j] = j

    for i in range(1, lenTarget+1):
        for j in range(1, lenText+1):
            if target[i-1] == text[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1

    return dp[lenTarget][lenText]

listOfCountries = [
    "India", 
    "Indiana",
    "USA",
    "Australia",
]

# i = input("Enter the country: ")

# for country in listOfCountries:
#     if(editDistance(i, country) < 3):
#         print(country)
    
# Current working directory
# os.getcwd()

# Change working directory
# os.chdir("C://")

# List directories
# os.listdir() ## Base
# os.lostdir("C://") ## C pe

# Make directory
# os.mkdir("This") # Make a folder named -> This

# Make directories (sub directory ban jaaye)
# os.makedirs("This/that") # Make a folder named -> This uske andar -> that

# Rename a file
# os.rename()
import os
print(os.environ.get('Path'))