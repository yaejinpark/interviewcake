def reverseWords(message):
    joinedMessage = ''.join(message).split(' ')[::-1]
    reversedMessage=""
    for words in joinedMessage:
        reversedMessage += words
        reversedMessage += ' '
    return reversedMessage

message = ['c', 'a', 'k', 'e', ' ',
           'p', 'o', 'u', 'n', 'd', ' ',
           's', 't', 'e', 'a', 'l']

print(reverseWords(message))