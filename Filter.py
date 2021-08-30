import re


with open("English1.txt") as f:
    content = f.readlines()
content = [word.strip() for word in content]
content.reverse()


def replaceCurseWords(UserChat):
    UserChat = UserChat.lower()
    for i in content:
        wordLen = len(i)
        UserChat = re.sub(i, "#" * wordLen, UserChat)
    return UserChat


if __name__ == "__main__":
    while True:
        UserChat = input('>')
        print(replaceCurseWords(UserChat))
