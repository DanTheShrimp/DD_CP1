#DD Period 7 for fun :D

import random

def display_hangman(tries):
    stages = [
        # final state: head, torso, both arms, both legs, hair
        """
           -----
           |   |
          \\|/  |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        # head, torso, both arms, one leg, hair
        """
           -----
           |   |
          \\|/  |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        # head, torso, both arms, hair
        """
           -----
           |   |
          \\|/  |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        # head, torso, one arm, hair
        """
           -----
           |   |
          \\|/  |
           O   |
          /|   |
               |
               |
        =========
        """,
        # head, torso, hair
        """
           -----
           |   |
          \\|/  |
           O   |
           |   |
               |
               |
        =========
        """,
        # head and hair
        """
           -----
           |   |
          \\|/  |
           O   |
               |
               |
               |
        =========
        """,
        # hair
        """
           -----
           |   |
          \\|/  |
               |
               |
               |
               |
        =========
        """,
        # mostly hair
        """
           -----
           |   |
          \\|   |
               |
               |
               |
               |
        =========
        """,
        # almost gone
        """
           -----
           |   |
           |   |
               |
               |
               |
               |
        =========
        """,
        # initial empty state
        """
           -----
           |   |
               |
               |
               |
               |
               |
        =========
        """
    ]
    return stages[9 - tries]

def hangman():
    word = random.choice(["pizza", "minecraft", "modder", "pain", "school", "computer", "python", "phone", "java", "javascript", "hangman", "programming", "code", "fun", "game", "player", "keyboard", "mouse", "monitor", "laptop", "desktop", "internet", "website", "application", "software", "hardware", "technology", "science", "math", "history", "geography", "art", "music", "movie", "book", "story", "adventure", "fantasy", "mystery", "horror", "comedy", "drama", "romance", "action", "thriller", "sci-fi", "fiction", "nonfiction", "education", "learning", "knowledge", "wisdom", "friendship", "family", "love", "life", "happiness", "success", "failure", "challenge", "opportunity", "future", "dream", "goal", "ambition", "passion", "creativity", "imagination", "inspiration", "motivation", "determination", "perseverance", "resilience", "courage", "bravery", "strength", "hope", "trust", "honesty", "integrity", "respect", "kindness", "compassion", "empathy", "generosity", "gratitude", "humility", "patience", "forgiveness", "understanding", "acceptance", "tolerance", "diversity", "inclusion", "equality", "justice", "freedom", "peace", "harmony", "unity", "community", "society", "world", "environment", "nature", "earth", "universe", "space", "time", "energy", "matter", "lifeform", "organism", "cell", "gene", "evolution", "adaptation", "survival", "ecosystem", "biodiversity", "conservation", "sustainability", "climate", "weather", "disaster", "emergency", "crisis", "conflict", "war", "peacekeeping", "diplomacy", "negotiation", "collaboration", "partnership", "teamwork", "leadership", "management", "strategy", "planning", "organization", "productivity", "efficiency", "innovation", "creativity", "design", "development", "testing", "deployment", "maintenance", "support", "service", "customer", "client", "user", "experience", "interface", "interaction", "feedback", "improvement", "growth", "expansion", "globalization", "localization", "marketing", "advertising", "branding", "sales", "revenue", "profit", "investment", "finance", "economy", "business", "industry", "market", "competition", "trend", "opportunity", "risk", "challenge", "solution", "decision", "action", "result", "outcome", "impact", "influence", "change", "transformation", "evolution", "progress", "development", "advancement", "breakthrough", "discovery", "invention", "creation", "innovation", "exploration", "adventure", "journey", "quest", "mission", "purpose", "vision", "goal", "dream"])
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 9
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

hangman()