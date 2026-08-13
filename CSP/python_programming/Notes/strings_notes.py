#DD Period 7 Strings Notes

import time
#Examples
name = input("WHO ARE YOU?!\n").strip().title()
print("Oh, you're", name + ", hello!")

time.sleep(3)
sentence = 'The quick brown fox jumps over the lazy dog.'
print(sentence.find("jumps"))
print(sentence[20:25]) #slicing
print(sentence[sentence.find("lazy"): len("lazy")+sentence.find("lazy")])
time.sleep(2)
print("Welcome to my program, HUMAN!!!")

#sanitization and stupid proofing!1!11!1!1!1!11!!!1!
#sanitization is cleansing things like capitals, lowercases, numbers, etc (this is step one of stupid proofing)

#debugging is fixing code!1!!111!1!!!1!
