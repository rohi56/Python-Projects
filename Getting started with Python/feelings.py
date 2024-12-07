# List of all feelings
feelings = ['Joy', 'Contentment', 'Delight', 'Excitement', 'Amusement', 'Satisfaction', 'Optimism', 'Pride', 'Gratitude',
            'Affection', 'Caring', 'Compassion', 'Warmth', 'Trust', 'Appreciation', 'Calm', 'Relaxation', 'Serenity', 
            'Tranquility', 'Empowerment', 'Assurance', 'Accomplishment', 'Self-worth', 'Grief', 'Loneliness', 
            'Disappointment', 'Hopelessness', 'Regret', 'Frustration', 'Resentment', 'Irritation', 'Annoyance', 
            'Outrage', 'Anxiety', 'Worry', 'Insecurity', 'Nervousness', 'Panic', 'Embarrassment', 'Remorse', 
            'Self-doubt', 'Humiliation', 'Shock', 'Amazement', 'Confusion', 'Jealousy', 'Envy', 'Longing', 'Nostalgia', 
            'Concern', 'Sympathy', 'Understanding']

# Ask the user if they want to know the feeling type
print('Do you want to know your feeling type (Yes/No):')
ans = input().capitalize()

# If the user says Yes
if ans == 'Yes':
    # Prompt user to enter a feeling
    print('Enter the feeling:')
    feeling = input().capitalize()  # Capitalize the input for consistent comparison

    # Check the feeling and categorize it
    if feeling in ['Joy', 'Contentment', 'Delight', 'Excitement', 'Amusement', 'Satisfaction', 'Optimism', 'Pride', 'Gratitude']:
        print(feeling, ': Its a Positive feeling called HAPPINESS')

    elif feeling in ['Affection', 'Caring', 'Compassion', 'Warmth', 'Trust', 'Appreciation']:
        print(feeling, ': Its a Positive feeling called LOVE')

    elif feeling in ['Calm', 'Relaxation', 'Serenity', 'Tranquility']:
        print(feeling, ': Its a Positive feeling called PEACEFULNESS')

    elif feeling in ['Empowerment', 'Assurance', 'Accomplishment', 'Self-worth']:
        print(feeling, ': Its a Positive feeling called CONFIDENCE')

    elif feeling in ['Grief', 'Loneliness', 'Disappointment', 'Hopelessness', 'Regret']:
        print(feeling, ': Its a Negative feeling called SADNESS')

    elif feeling in ['Frustration', 'Resentment', 'Irritation', 'Annoyance', 'Outrage']:
        print(feeling, ': Its a Negative feeling called ANGER')

    elif feeling in ['Anxiety', 'Worry', 'Insecurity', 'Nervousness', 'Panic']:
        print(feeling, ': Its a Negative feeling called FEAR')

    elif feeling in ['Embarrassment', 'Remorse', 'Self-doubt', 'Humiliation']:
        print(feeling, ': Its a Negative feeling called GUILT/SHAME')

    elif feeling in ['Shock', 'Amazement', 'Confusion']:
        print(feeling, ': Its a Mixed feeling called SURPRISE')

    elif feeling in ['Jealousy', 'Envy', 'Longing', 'Nostalgia']:
        print(feeling, ': Its a Mixed feeling called LOVE/HATE')

    elif feeling in ['Concern', 'Sympathy', 'Understanding']:
        print(feeling, ': Its a Mixed feeling called EMPATHY')

    else:
        print(feeling, ': Not a Valid feeling')

# If the user says No
elif ans == 'No':
    print('Thanks for your response.')

# If the input is neither Yes nor No
else:
    print('Invalid input. Please enter Yes or No.')
