def monty_hall(correct_door_number, participant_guesses):
    lose_count = len(participant_guesses) - participant_guesses.count(correct_door_number)
    return round((lose_count / len(participant_guesses)) * 100)
