# Daniel DeLong, Password Checker Pseudocode


# GET player password input

# HAVE a list of ALL UPPERCASE letters
# HAVE a list of ALL lowercase letters
# HAVE a list of ALL numbers
# HAVE a list of ALL special characters

# CHECK IF the length is greater than 8
# CHECK IF there is a capital in the player input
# CHECK IF there is a lowercase in the player input
# CHECK IF there is a number in the player input
# CHECK IF there is a special character in the player input

# IF no CHECKS pass LOOP back to the start and GET player password input again
    # also DISPLAY that their password was too weak, and tell them what they need to add to make it stronger
# DEPENDING on how many CHECKS pass we increase a variable's value (strength_level)
# DEPENDING on the VALUE of strength_level we SET it to either "weak" "medium" or "strong"

# DISPLAY their password's strength level
# DISPLAY what they need to add to make their password stronger