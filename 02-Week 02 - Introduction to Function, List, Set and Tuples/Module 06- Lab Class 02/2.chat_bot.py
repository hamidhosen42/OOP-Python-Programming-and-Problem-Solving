""" Chatboat.

step:
1. input/listen
2. process/decide
3. output/talkback

"""

greet_words = ['hi','hello','you']
bye_words = ['bye','tata','hasta la vista']
bad_words = ['dog','pocha']

def listen():
    return input("Say something: ")

def decide(command):
    # print(common)
    command  = command.lower()
    broken_word = command.split(" ")
    # print(broken_word)
    for words in broken_word:
        if words in greet_words:
            # print("He said greetings")
            talkback("He Man")
            break

        elif words in bye_words:
            # print("He said bey")
            print("He said bey")
            break

        elif words in bad_words:
            print("Behave yourself!")
            break

def talkback(respons):
    print(respons)

while True:
    command = listen()
    # print(command)
    decide(command)