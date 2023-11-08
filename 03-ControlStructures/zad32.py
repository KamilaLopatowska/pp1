interested_in_computer_science = False
like_playing_computer_games = False
has_instagram_account = False
 
interested_in_computer_science_answer = input("Are you interested in computer science? (Y/N): ")
if interested_in_computer_science_answer == "y" or interested_in_computer_science_answer == "Y":
    interested_in_computer_science = True

like_playing_computer_games_answer = input("Do you like playing computer games? (Y/N): ")
if like_playing_computer_games_answer == "y" or like_playing_computer_games_answer == "Y":
    like_playing_computer_games = True

has_instagram_account_answer = input("Do you have an Instagram account? (Y/N): ")
if has_instagram_account_answer == "y" or has_instagram_account_answer == "Y":
    has_instagram_account = True

# Display the survey results
print("Interested in computer science:", "Yes" if interested_in_computer_science else "No")
print("Playing computer games:", "Yes" if like_playing_computer_games else "No")
print("Has an Instagram account:", "Yes" if has_instagram_account else "No")