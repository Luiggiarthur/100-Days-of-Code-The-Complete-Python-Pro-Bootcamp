#TODO: Create a letter using starting_letter.txt 

with open(".\Input\Letters\starting_letter.txt") as file:
    content = file.read()
    with open(".\Input/Names\invited_names.txt") as names:
        lines = names.readlines()
        for name in lines:
            text = name.strip()
            new_letter = content.replace('[name]', name)
            with open(f".\Output\ReadyToSend\letter_for_{text}.txt", mode="w") as final_letter:
                final_letter.write(new_letter)

