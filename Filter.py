import re


with open("English.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]


def curseWordRegex(UserChat):
    UserChat = UserChat.lower()
    for i in content:
        regex = re.compile(i)
        mo = regex.search(UserChat)
        if mo == None:
            pass
        else:
            return True


def replaceCurseWords(UserChat):
    UserChat = UserChat.lower()
    for i in content:
        regex = re.compile(i)
        WordLen = len(i)
        UserChat = regex.sub('#' * WordLen, UserChat)
    return UserChat


if __name__ == "__main__":
    while True:
        UserChat = input('>')
        HaveCurse = curseWordRegex(UserChat)
        if HaveCurse:
            print(replaceCurseWords(UserChat))
        if not HaveCurse:
            print(UserChat)
