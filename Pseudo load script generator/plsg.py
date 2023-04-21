import random as random
import time as time
import os
os.system("")
scriptline = ""

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


# Open three files and return data as list
def file_to_list():
    with open("actions.txt", "r") as acts:
        actionslist = []
        for item in acts:
            item = item.strip()
            item = item.split()
            actionslist.append(item)
    with open("subjects.txt", "r") as subjs:
        subjectlist = []
        for item in subjs:
            item = item.strip()
            item = item.split()
            subjectlist.append(item)
    with open("prepositions.txt", "r") as prps:
        preplist = []
        for item in prps:
            item = item.strip()
            item = item.split()
            preplist.append(item)
    return actionslist, subjectlist, preplist

    # Generate three random ints based on list lengths


def random_int_generator(acts: list, subs: list, prps: list):
    acts_r = random.randint(0, len(acts) - 1)
    subs_r = random.randint(0, len(subs) - 1)
    subs_r2 = random.randint(0, len(subs) - 1)
    prps_r = random.randint(0, len(prps) - 1)
    return acts_r, subs_r, subs_r2, prps_r


def sentence_generator(act, sub, pre, r1, r2,r3, r4):
    #print(act, r1)
    sentence = []
    sentence.append(act[r1])
    sentence.append(sub[r2])
    sentence.append(pre[r4])
    sentence.append(sub[r3])
    return sentence


def printer(sent):
    print(style.RESET + f"{sent[0][0]} {sent[1][0]} {sent[2][0]} {sent[3][0]}", end=' ')
    i = 0
    while i < 10:
        wait = random.random()
        print(f"...", end='')
        time.sleep(wait)
        i += 1
    message_id = random.randint(0, 9)
    if 0 <= message_id <= 6:
        print(style.GREEN + f"[COMPLETE]")
    if 7 <= message_id <= 8:
        print(style.YELLOW + f"[WARNING]")
        print(f"    ! check log.md for detailed information on issues with {sent[1][0]} !")
    if message_id == 9:
        print(style.RED + f"[FAILED]")
        print(f"Retrying: {sent[0][0]} {sent[1][0]} {sent[2][0]} {sent[3][0]}", end=' ')
        i = 0
        while i < 10:
            wait = random.random()
            print(f"...", end='')
            time.sleep(wait)
            i += 1
        print(style.GREEN + f"[COMPLETE]")



while True:
    actions, subjects, preps = file_to_list()
    ac_r, su_r, su_r2, pr_r = random_int_generator(actions, subjects, preps)
    sentence = sentence_generator(actions, subjects, preps, ac_r, su_r, su_r2, pr_r)
    printer(sentence)