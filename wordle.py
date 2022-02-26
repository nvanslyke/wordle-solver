import random
import sys
import numpy
from matplotlib import pyplot as plt 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time    
import pyautogui
import cv2 as cv
from PIL import Image

words = []

yellow = (201, 180, 88)
green = (106, 170, 100)
grey = (120, 124, 126)
xvals = [844, 912, 978, 1046, 1112]
chosenWord = ""

with open("words.txt") as file:
    for line in file:
        words.append(line)


for i in range(0, len(words)-1):
    words[i] = words[i][0:len(words[i])-1]
narrowedsim = []
for i in words:
    narrowedsim.append(i)


print(str(len(words)) + " words uploaded")

print()


def solve(narrowed):
    narrowed = narrowed 
   
    guess = select_guess(narrowed)
    if len(narrowed) == len(words):
        guess = "trace"
    print("Guess " + guess)
    print()
    print()
    entry = input("Enter the color of each box g/y/x for green/yellow/grey ")
    firstletter = entry[0]
    secondletter = entry[1]
    thirdletter = entry[2]
    fourthletter = entry[3]
    fifthletter = entry[4]

    if firstletter == "g": 
        a = 0
        while a < len(narrowed):   
            if narrowed[a][0] != guess[0]:
                narrowed.pop(a)
            else:
                a += 1
    elif firstletter == "y":
        a = 0
        while a < len(narrowed):
            if guess[0] not in narrowed[a] or narrowed[a][0] == guess[0]:
                narrowed.pop(a)
            else:
                a += 1
    else:
        a = 0
        while a < len(narrowed):
            if guess[0] in narrowed[a]:
                narrowed.pop(a)
            else:
                a += 1

    if secondletter == "g": 
        b = 0
        while b < len(narrowed):   
            if narrowed[b][1] != guess[1]:
                narrowed.pop(b)
            else:
                b += 1
    elif secondletter == "y":
        b = 0
        while b < len(narrowed):
            if guess[1] not in narrowed[b] or narrowed[b][1] == guess[1]:
                narrowed.pop(b)
            else:
                b += 1
    else:
        b = 0
        while b < len(narrowed):
            if guess[1] in narrowed[b]:
                narrowed.pop(b)
            else:
                b += 1
    if thirdletter == "g": 
        c = 0
        while c < len(narrowed):   
            if narrowed[c][2] != guess[2]:
                narrowed.pop(c)
            else:
                c += 1
    elif thirdletter == "y":
        c = 0
        while c < len(narrowed):
            if guess[2] not in narrowed[c] or narrowed[c][2] == guess[2]:
                narrowed.pop(c)
            else:
                c += 1
    else:
        c = 0
        while c < len(narrowed):
            if guess[2] in narrowed[c]:
                narrowed.pop(c)
            else:
                c += 1
    if fourthletter == "g": 
        d = 0
        while d < len(narrowed):   
            if narrowed[d][3] != guess[3]:
                narrowed.pop(d)
            else:
                d += 1
    elif fourthletter == "y":
        d = 0
        while d < len(narrowed):
            if guess[3] not in narrowed[d] or narrowed[d][3] == guess[3]:
                narrowed.pop(d)
            else:
                d += 1
    else:
        d = 0
        while d < len(narrowed):
            if guess[3] in narrowed[d]:
                narrowed.pop(d)
            else:
                d += 1
    if fifthletter == "g": 
        e = 0
        while e < len(narrowed):   
            if narrowed[e][4] != guess[4]:
                narrowed.pop(e)
            else:
                e += 1
    elif fifthletter == "y":
        e = 0
        while e < len(narrowed):
            if guess[4] not in narrowed[e] or narrowed[e][4] == guess[4]:
                narrowed.pop(e)
            else:
                e += 1
    else:
        e = 0
        while e < len(narrowed):
            if guess[4] in narrowed[e]:
                narrowed.pop(e)
            else:
                e += 1
    print()
    print()

    if len(narrowed) <= 10:
        print("Possible Words")
        print("________________________")
        for word in narrowed:
            print(word)
    print()
    print()
    if len(narrowed) > 1:
        solve(narrowed)
    
def select_guess(narrowed):
    guess = random.randint(0,len(narrowed)-1)
    guess = narrowed[guess]
    for i in range(len(guess)):
        if guess.count(guess[i]) > 1:
            if alltwos(narrowed) == True:
                return guess
            return select_guess(narrowed)

     
    return guess

def alltwos(narrowed):
    count = 0
    for word in narrowed:
        for char in word:
            if word.count(char) > 1:
                count += 1
                break
    if count == len(narrowed):
        return True
    else:
        return False
    

def main():
    global words
    choose = input("What do you want to do? solve/play/simulate/auto: ")
    if choose.lower() == "solve":
        
        print("  ______       _                _______           _       \n"
            " / _____)     | |              (_______)         | |      \n"
            "( (____   ___ | |_   _ _____    _  _  _  ___   __| |_____ \n"
            " \____ \ / _ \| | | | | ___ |  | ||_|| |/ _ \ / _  | ___ |\n"
            " _____) ) |_| | |\ V /| ____|  | |   | | |_| ( (_| | ____|\n"
            "(______/ \___/ \_)\_/ |_____)  |_|   |_|\___/ \____|_____)")
        print()
        narrowed = []
        for i in words:
            narrowed.append(i)
        solve(narrowed) 
    elif choose.lower() == "play":
        play()

    elif choose.lower() == "simulate":
        simulate()
    
    elif choose.lower() == "auto":
        driver = webdriver.Chrome()
        driver.get("https://www.nytimes.com/games/wordle/index.html")
        driver.maximize_window()
        time.sleep(1)
        pyautogui.click(300,300)
        narrowed = []
        round = 1
        for i in words:
            narrowed.append(i)
        auto(narrowed, round) 

def howclose(wordchoice, guess):
    closeness = ""
    for char in guess:
        if char in wordchoice:
            if guess.index(char) == wordchoice.index(char):
                closeness = closeness + "G"
            else:
                closeness = closeness + "Y"
        else:
            closeness = closeness + "X" 
    return closeness

def howclose2(wordchoice, guess):
    used = ""
    closenessstr = "XXXXX"
    closenesslist = []
    for char in closenessstr:
        closenesslist.append(char)
    closenessstr = ""
    i = 0
    for char in guess:
        if char == wordchoice[i]:
            closenesslist[i] = 'G'
            used = used + char
        i += 1
    c = 0
    for char in guess:    
        if char in wordchoice:
            if char != wordchoice[c]:
                if char not in used:
                    closenesslist[c] = 'Y'
                    if wordchoice.count(char) == 1:
                        used = used + char
        c += 1
    for item in closenesslist:
        closenessstr += item
    return closenessstr

def play():
    global words
    print(" _____  _               __  __           _       ")
    print("|  __ \| |             |  \/  |         | |     ")
    print("| |__) | | __ _ _   _  | \  / | ___   __| | ___ ")
    print("|  ___/| |/ _` | | | | | |\/| |/ _ \ / _` |/ _ \ " )  
    print("| |    | | (_| | |_| | | |  | | (_) | (_| |  __/") 
    print("|_|    |_|\__,_|\__, | |_|  |_|\___/ \__,_|\___|") 
    print("                 __/ |                             ")
    print("                |___/                               ")

    randnum = random.randint(0,len(words)-1)
    wordchoice = words[randnum]
    
            
        
    round = 1
    #print(wordchoice)
    print("Round # " + str(round))
    guess = input("what word do you guess? ")
    #print("you guessed" + guess)
    guess = guess.lower()
    if len(guess) != 5:
        return
    while guess != wordchoice:
        print()
        round += 1
        print("Round # " + str(round))
        print(howclose2(wordchoice, guess))
        guess = input("what word do you guess? ")
    print()
    print("   ______                          __ ")
    print("  / ____/___  _____________  _____/ /_")
    print(" / /   / __ \/ ___/ ___/ _ \/ ___/ __/")
    print("/ /___/ /_/ / /  / /  /  __/ /__/ /_  ")
    print("\____/\____/_/  /_/   \___/\___/\__/  ")
    print()
                                    
    main()

def simplay():
    global chosenWord
    global narrowedsim
    
    
        

    count = 0
    run = True
    
    while run:
      wordchoice = random.randint(0,len(words)-1)
      chosenWord = words[wordchoice]
      for char in chosenWord:
        count += chosenWord.count(char)
      if count == 5:
        run = False
      else:
        count = 0

        
            
    round = 1
    guess = "trace"
    
    going = True
    while going:
       if chosenWord == guess:
           going = False
           break
       round += 1
       simsolve(guess)
       
       if len(narrowedsim) > 0:
            guess = select_guess(narrowedsim)
       else:  
          print(chosenWord)
          print(narrowedsim) 
          break
    narrowedsim = []
    for i in words:
        narrowedsim.append(i)
    return round

def simclose(guess):   
    global chosenWord
    return howclose2(chosenWord, guess).lower()

def simsolve(guess):
    global narrowedsim
    narrowed = []
    for i in narrowedsim:
        narrowed.append(i)
   
    #print(guess)
    entry = simclose(guess)
    
    
    firstletter = entry[0]
    secondletter = entry[1]
    thirdletter = entry[2]
    fourthletter = entry[3]
    fifthletter = entry[4]

    if firstletter == "g": 
        a = 0
        while a < len(narrowed):   
            if narrowed[a][0] != guess[0]:
                narrowed.pop(a)
            else:
                a += 1
    elif firstletter == "y":
        a = 0
        while a < len(narrowed):
            if guess[0] not in narrowed[a] or narrowed[a][0] == guess[0]:
                narrowed.pop(a)
            else:
                a += 1
    else:
        a = 0
        while a < len(narrowed):
            if guess[0] in narrowed[a]:
                narrowed.pop(a)
            else:
                a += 1

    if secondletter == "g": 
        b = 0
        while b < len(narrowed):   
            if narrowed[b][1] != guess[1]:
                narrowed.pop(b)
            else:
                b += 1
    elif secondletter == "y":
        b = 0
        while b < len(narrowed):
            if guess[1] not in narrowed[b] or narrowed[b][1] == guess[1]:
                narrowed.pop(b)
            else:
                b += 1
    else:
        b = 0
        while b < len(narrowed):
            if guess[1] in narrowed[b]:
                narrowed.pop(b)
            else:
                b += 1
    if thirdletter == "g": 
        c = 0
        while c < len(narrowed):   
            if narrowed[c][2] != guess[2]:
                narrowed.pop(c)
            else:
                c += 1
    elif thirdletter == "y":
        c = 0
        while c < len(narrowed):
            if guess[2] not in narrowed[c] or narrowed[c][2] == guess[2]:
                narrowed.pop(c)
            else:
                c += 1
    else:
        c = 0
        while c < len(narrowed):
            if guess[2] in narrowed[c]:
                narrowed.pop(c)
            else:
                c += 1
    if fourthletter == "g": 
        d = 0
        while d < len(narrowed):   
            if narrowed[d][3] != guess[3]:
                narrowed.pop(d)
            else:
                d += 1
    elif fourthletter == "y":
        d = 0
        while d < len(narrowed):
            if guess[3] not in narrowed[d] or narrowed[d][3] == guess[3]:
                narrowed.pop(d)
            else:
                d += 1
    else:
        d = 0
        while d < len(narrowed):
            if guess[3] in narrowed[d]:
                narrowed.pop(d)
            else:
                d += 1
   
  
    if fifthletter == "g": 
        e = 0
        while e < len(narrowed):   
            if narrowed[e][4] != guess[4]:
                narrowed.pop(e)
            else:
                e += 1
    elif fifthletter == "y":
        e = 0
        while e < len(narrowed):
            if guess[4] not in narrowed[e] or narrowed[e][4] == guess[4]:
                narrowed.pop(e)
            else:
                e += 1
    else:
        e = 0
        while e < len(narrowed):
            if guess[4] in narrowed[e]:
                narrowed.pop(e)
            else:
                e += 1
    narrowedsim = []
    
    for i in narrowed:
        narrowedsim.append(i)

def retrieve_output(round):
    response = ""
    screenshot = pyautogui.screenshot()
    img = pyautogui.screenshot()
    screenshot = numpy.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
    yval = 0
    if round == 1:
        yval = 350
    elif round == 2:
        yval = 421
    elif round == 3:
        yval = 485
    elif round == 4:
        yval = 553
    elif round == 5:
        yval = 624
    elif round == 6:
        yval = 688
    for num in xvals:
        if img.getpixel((num,yval)) == green:
            response += "g"
        elif img.getpixel((num,yval)) == yellow:
            response += "y"
        elif img.getpixel((num,yval)) == grey:
            response += "x"
        else:
            print(img.getpixel((num,yval)))
    print(round)
    print(response)
    return response
    

def input_guess(guess):
   
    for char in guess:
        pyautogui.write(char)
    pyautogui.press("enter")



def auto(narrowed, round):
    narrowed = narrowed 
   
    guess = select_guess(narrowed)
    if len(narrowed) == len(words):
        guess = "trace"
    print("Guess " + guess)
    input_guess(guess)
    print()
    print()
    time.sleep(2)
    entry = retrieve_output(round)
    firstletter = entry[0]
    secondletter = entry[1]
    thirdletter = entry[2]
    fourthletter = entry[3]
    fifthletter = entry[4]

    if firstletter == "g": 
        a = 0
        while a < len(narrowed):   
            if narrowed[a][0] != guess[0]:
                narrowed.pop(a)
            else:
                a += 1
    elif firstletter == "y":
        a = 0
        while a < len(narrowed):
            if guess[0] not in narrowed[a] or narrowed[a][0] == guess[0]:
                narrowed.pop(a)
            else:
                a += 1
    else:
        a = 0
        while a < len(narrowed):
            if guess[0] in narrowed[a]:
                narrowed.pop(a)
            else:
                a += 1

    if secondletter == "g": 
        b = 0
        while b < len(narrowed):   
            if narrowed[b][1] != guess[1]:
                narrowed.pop(b)
            else:
                b += 1
    elif secondletter == "y":
        b = 0
        while b < len(narrowed):
            if guess[1] not in narrowed[b] or narrowed[b][1] == guess[1]:
                narrowed.pop(b)
            else:
                b += 1
    else:
        b = 0
        while b < len(narrowed):
            if guess[1] in narrowed[b]:
                narrowed.pop(b)
            else:
                b += 1
    if thirdletter == "g": 
        c = 0
        while c < len(narrowed):   
            if narrowed[c][2] != guess[2]:
                narrowed.pop(c)
            else:
                c += 1
    elif thirdletter == "y":
        c = 0
        while c < len(narrowed):
            if guess[2] not in narrowed[c] or narrowed[c][2] == guess[2]:
                narrowed.pop(c)
            else:
                c += 1
    else:
        c = 0
        while c < len(narrowed):
            if guess[2] in narrowed[c]:
                narrowed.pop(c)
            else:
                c += 1
    if fourthletter == "g": 
        d = 0
        while d < len(narrowed):   
            if narrowed[d][3] != guess[3]:
                narrowed.pop(d)
            else:
                d += 1
    elif fourthletter == "y":
        d = 0
        while d < len(narrowed):
            if guess[3] not in narrowed[d] or narrowed[d][3] == guess[3]:
                narrowed.pop(d)
            else:
                d += 1
    else:
        d = 0
        while d < len(narrowed):
            if guess[3] in narrowed[d]:
                narrowed.pop(d)
            else:
                d += 1
    if fifthletter == "g": 
        e = 0
        while e < len(narrowed):   
            if narrowed[e][4] != guess[4]:
                narrowed.pop(e)
            else:
                e += 1
    elif fifthletter == "y":
        e = 0
        while e < len(narrowed):
            if guess[4] not in narrowed[e] or narrowed[e][4] == guess[4]:
                narrowed.pop(e)
            else:
                e += 1
    else:
        e = 0
        while e < len(narrowed):
            if guess[4] in narrowed[e]:
                narrowed.pop(e)
            else:
                e += 1
    print()
    print()

    

    if len(narrowed) <= 10:
        print("Possible Words")
        print("________________________")
        for word in narrowed:
            print(word)
    print()
    print()
    if len(narrowed) >= 1:
        round += 1
        auto(narrowed, round)
def simulate():
    arr = []
    playnum = 5000
    sum = 0
    highestround = 0
    worstword = ""
    print()
    print()
    loading = []
    increments = int(playnum / 10)
    for i in range(0,playnum,increments):
        loading.append(i + increments)
    

    for i in range(playnum):
        gotto = simplay()
        arr.append(gotto)
        if gotto > highestround:
            highestround = gotto
            worstword = chosenWord
        sum += gotto
        if i in loading:
            print("🟩", end = "", flush=True)
    print("🟩")
    print()
    print()
    
    average = sum / playnum 
    print("The average winning round in " + str(playnum) + " games is " + str(average))
    print("The highest number of guesses taken was " + str(highestround) +" on the word " + worstword)
    print(frequency(arr, highestround))
    
    a = numpy.array(arr)
    plt.hist(a, bins = [0,1,2,3,4,5,6,7,8,9,10,11,12])
    plt.title("Distribution of Highest Round Reached")
    plt.show()
    
def frequency(arr, highestround):
    fTable = []
    for i in range(1,highestround + 1):
        count = 0
        for num in arr:
            if num == i:
                count += 1
        fTable.append(count)
    return fTable
    

    
        
    
if __name__ == "__main__":
    main()
