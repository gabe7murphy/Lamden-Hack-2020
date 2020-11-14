#need something on the websit that displays the time before each round and that
#countdowns til no more bets and round starts. and need something to displays
#the crash value as it increases but that doesnt seem hard to code.


import time
import matplotlib.pyplot as plt
%matplotlib notebook
plt.rcParams['animation.html'] = 'jshtml'
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

time = 0
crash_number = #how to go from zero to the crash number instead of jumping to
               #that specific number when it goes through the time
               
x, y = [],[]
while True:
    x.append(time)
    y.append(#crash number)

    ax.plot(x,y,color='b')

    fig.canvas.draw()

    ax.set_xlim(left = max(0, time-5), right = time+5)

    time.sleep(0.1)
    time += 1


#WHAT THIS IS BELOW IS THE CODE TO FIND THE NUMBER THAT THE GRAPH WILL CRASH AT
#SOME HOW WE ALSO NEED TO FIND A WAY TO KEEP GETTING HASHES TO DECODE IF THEY
#WANT TO KEEP PLAYING

    #https://github.com/MindingTheData/Crash-Analysis/blob/master/Crash.ipynb
    #https://www.youtube.com/watch?v=F1HA7e3acSI&t=178s

##import matplotlib.pyplot as plt
##import numpy as np
##import hashlib
##import random
##import string
##import hmac
##
##e = 2**52
##salt = "0000000000000000000fa3b65e43e4240d71762a5bf397d5304b2596d116859c"
##
##
##
##game_hash = '100af1b49f5e9f87efc81f838bf9b1f5e38293e5b4cf6d0b366c004e0a8d9987'
##
##def get_result(game_hash):
##    hm = hmac.new(str.encode(game_hash), b'', hashlib.sha256)
##    hm.update(salt.encode("utf-8"))
##    h = hm.hexdigest()
##    if (int(h, 16) % 33 == 0):
##        return 1
##    h = int(h[:13], 16)
##    e = 2**52
##    return (((100 * e - h) / (e-h)) // 1) / 100.0
##


    
