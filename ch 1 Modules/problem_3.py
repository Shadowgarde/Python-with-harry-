import pyttsx3
engine = pyttsx3.init()  #initial object creation hogya 

#ab me iska rate set karunga 
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
print(rate)


#ab me iski volume set karunga 
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume', 0.5)
print(volume)

engine.say("And mother what work do you have for me")
engine.runAndWait()
