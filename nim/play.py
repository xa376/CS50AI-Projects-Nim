from nim import train, play
import time
t0 = time.time()
ai = train(10000)
t1 = time.time()
print(t1 - t0)
play(ai)
