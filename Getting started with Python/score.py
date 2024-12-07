# Prompt the user to input their score
score = input("Enter Score: ")

# Convert the score from string to float for numerical comparison
score = float(score)

# Check if the score is below 0.0, which is not valid
if score < 0.0:
    print("Not Valid : Score should not be below 0.0")

# Check if the score is above 1.0, which is not valid
elif score > 1.0:
    print("Not Valid : Score should not be above 1.0")

# Check if the score is greater than or equal to 0.9
elif score >= 0.9:
    print('A')  # Grade A for scores 0.9 or higher

# Check if the score is greater than or equal to 0.8
elif score >= 0.8:
    print('B')  # Grade B for scores 0.8 to less than 0.9

# Check if the score is greater than or equal to 0.7
elif score >= 0.7:
    print('C')  # Grade C for scores 0.7 to less than 0.8

# Check if the score is greater than or equal to 0.6
elif score >= 0.6:
    print('D')  # Grade D for scores 0.6 to less than 0.7

# If the score is less than 0.6, assign grade F
elif score < 0.6:
    print('F')  # Grade F for scores below 0.6
