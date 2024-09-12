with open("100_days_of_python/day_24_file_paths/list_of_names.txt") as list_of_names:
    names = list_of_names.readlines()
with open("100_days_of_python/day_24_file_paths/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace("[name]",stripped_name)
        with open(f"100_days_of_python/day_24_file_paths/ready_to_send/letter_for_{stripped_name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)


            
