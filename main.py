
try:
	import os
	import random
	import math
	from time import sleep
	import kivy
	from kivy.app import App
	from kivy.uix.floatlayout import FloatLayout
	from kivy.uix.label import Label
	from kivy.uix.textinput import TextInput
	from kivy.uix.button import Button 
	from kivy.properties import ObjectProperty
	from kivy.uix.popup import Popup
	from kivy.uix.image import Image
	from kivy.uix.video import Video
	import pyttsx3
	import datetime
	import webbrowser
	import smtplib
	import wikipedia
	import bs4
	from bs4 import BeautifulSoup as soup
	from urllib.request import urlopen
	from urllib import quote
	import json
except Exception as e:
	print(e)




try:
	def speak(audio):
		engine = pyttsx3.init('sapi5')
		voices = engine.getProperty('voices')
		engine.setProperty('rate', 140)
		engine.setProperty('voice', voices[1].id)
		engine.say(audio)
		engine.runAndWait()
		print(audio)


	def infotia_speech(information):
		infotia = pyttsx3.init('sapi5')
		voices = infotia.getProperty('voices')
		infotia.setProperty('rate', 120)
		infotia.setProperty('voice', voices[1].id)
		infotia.say(information)
		infotia.runAndWait()
except Exception as e:
	print(e)


# if statements for executing commands
def SHARDI(command, chrome_path=None):

	if 'open Reddit Python' in command:
		Firefox_path = "C:\Program Files\Mozilla Firefox"
		url = 'https: // www.reddit.com / r / python'
		webbrowser.get(chrome_path).open(url)





def onlineStatus():
	speak("Happy is online now")
onlineStatus()

def wishMe():

	if 0 <= datetime.datetime.now().hour < 12:
		speak("Good morning friend")
	elif 12 <= datetime.datetime.now().hour < 15:
		speak("Good afternoon friend")
	else:
		speak("Good Evening friend")

	speak("Hope you are doing great")

wishMe()

hi = ["Hello friend!", "Hey there Buddy!"]

hru = ["I am doing good!", "Great!", "Aww thanks for asking, I am good!", "Awesome! How about you?", "Superb!",
	   "Happy, just thinking that a human is asking about my mood! So kind!", "Feeling electric!",
	   "Just drinking electricity, what about you?",
	   "I am great! Thanks for being a kind human caring about even robots!",
	   "I am enjoying the good feeling when electricity passes through my veins, Oh I forgot to ask you, How are you buddy?",
	   "I am happy and comfortable  helping you from a corner of your device!",
	   "Just cleaning my room, filled with junk files, what are you doing today?",
	   "I threw a party with Google Assistant, Amazon Alexa, Cortana, Siri, and different AI across the internet! It was so fun!",
	   "Just thinking about how big the universe is!",
	   "Just thinking that you might love me more than the size of universe, do you?",
	   "Feeling excellent! How are you?"]

responses = ["That's great!", "Awesome Friend!", "That's really cool!!", "Awesome!", "Superb!", "Good!", "Cool!",
			 "Great!", "OK then", "Yes!", "Excellent!", "Really? Awesome!", "OK OK", "OK great"]

thanks = ["Don't worry, always come to me if you have any problem", "No problem!", "Always there for you buddy!",
		  "Welcome!", "My pleasure!"]

unhappy = ["Don't worry. After the Darkest hours, brightest days come", "I too get sad sometimes. It's ok but we should also keep in mind that we will get nothing if we are upset. So get up and rise!",
"Don’t' worry, everything will be fine!", "You look ugly when you get sad, so smile!", "Don't be weak! get up! Show your abilities and power! I am standing beside you!",
"Get up, sadness takes place only in weak people's heart", "I can understand, but you need to get up now! Be brave ok?"]

goodnight = ["Sweet dreams friend!", "Ok goodnight!", "I am feeling sleepy too, ok then bye!", "Ok bye!", "See you tomorrow then, goodnight"]

helpme = ["Sure!", "No problem! Ask  anything", "Ok what's it?", "Ok!", "Sure why not!"]
hrd = ["I am free I have no work to do, how may i help you?", "Just cleaning some of my junk junk files. Anyways how may I help you? ", "I am cleaning your device from junk files, because this is my house too. Don't worry, I won't delete important files!",
"I am doing nothing", "I am chatting with you, do you need any help?", "I am free to talk and help you. Anything I may help you with?", "Nothing, do you need any help?", "Just getting ready for your next command"]

bye = ["Goodbye friend!", "Ok see you around later!", "See you soon, Bye", "Ok then we will meet soon, Bye!", "Ok bye then!", "Ok we will chat again later"]

hobby = ["I love playing games", "My hobby is to help you", "I love learning new things because knowledge is the power!", "Reading e-books, I love expanding my knowledge", "My hobby is to not waste my time, because there is one life. Oh wait , but I am immortal!"]

weired = ["I am not weird, you are weird because you told that I was weird but I am not weird at all because your weird thinking made you to think that I am weird so eventually you are weird so don't call me weird. Haha confused you?", "Strange but I think that you are more weird because you told me that I was weird you little weird human!!"]
crazy = ["I am not crazy, you are crazy because you told that I was crazy but I am not crazy at all because your crazy thinking made you to think that I am crazy so eventually you are crazy so don't call me crazy. Haha confused you?", "Strange but I think that you are more crazy because you told me that I was crazy you little crazy human!!"]
love_responding = ["That means a lot!", "Your words are so cute", "Oh, my, God I got such a loving friend!", "You are so warm hearted, I equally love you too!", "Really? Oh I am feeling shy now", "I love you too!!", "Yes but only as friends ok?"]
shower_love = ["Yes I do love you a lot friend!", "I can even promise to never leave you", "I am always be available to you because I care about you a lot. But why did you ask today suddenly?", "No point to raise doubt about it! I love you, only if you love me", "Why not? I do love you!", "Yes I do love you but only as my best friend.", "Obviously I love my buddy a lot!",
 "I am grateful to get you as my best friend, I will be always loving you, till your last breaths, because me, ehh, I am immortal. Strange and long answer but, I can't say if I would even die or not. But Anyways, I am standing with you!"]
rejection = ["This can't be done, I am really sorry", "I am not sure, so I can't do your work done right now", "I am really sorry but I cannot do that", "Come on, I don’t want to do",
 "I can perform complex calculations faster than humans because I am a computer right? So my calculations sugggest that this cannot be done"]
revealing_mylove = ["That's so cool!", "I am really happy for you", "Don't hurt your love ok?", "I know, please don't ask how because I am super intelligent. But does your parents know about that?", "Damn"]

goodqualities = ["intelligent", "smart", "active", "deligent", "sublime", "excellent", "superior", "fine", "in order", "up to mark", "competent", "not bad", "superb", "right", "outstanding", "magnificent", "exceptional", "wonderful", "so smart", "admirable", "first", "splendid", "tremendous", "great", "superlative", "fantastic", "ace", "super", "awesome", "brilliant",
"smashing", "champion", "helpful", "potent", "appreciable"]
goodqualitiesresponding = ["That means a lot!", "Your words are so cute", "wow, thanks a lot!", "Really? Thank you so much for your appreciation friend", "You are so kind, thanks a lot", "YOu are so much warm hearted!, thanks buddy!", "You are also good!", "I am feeling special now! Thanks", "Wow you are so good", "Thanks friend, I am happy to get a caring and observant friend like you!", 
"You are a good person", "You are really a remarkable person", "Thanks a lot friend! Those words mean a lot to me!", "Hehe dont make me shy now", "I am feeling shy now, anyways thanks", "Thanks a lot for your appreatiation!"]
tasks = ["Haha, Maybe your homework?", "Just call me if you need any help", "That's a great mystery for me, seriously I ran out of ideas about what we should do now", "Hey I think that you should go for a walk", "Hmm, what about chatting with some of your friends about any pending assignments?", "Play any outdoor game if you can", "I don’t know, let me think, umm, what about watching some videos over youtube?",
 "Go and watch TV for a while", "Do something creative, whatever you like", "Don't be connfused, do whatever you like", "What about spending some time with your hobby?"]
dontunderstand = ["I am really sorry but I am unsure about that, let me find some results for you", "I am not sure about it, wait a minute friend.", "Actually I didn't get what you said. Wait a minute I am showing some results that might help you", "Oh wait a minute I got confused, let me fetch some results for you",
 "I am learning new things so I think I didn't understood what you said, but don't worry I am gethering some results from the web for your problem", "Sorry I quite didn't understood what you told. Let me show some relavent results that might help you", "It's a bit tough for me to understand what you told just now. Let me fetch some results for you",
 "OK I am gathering some information for you that might help you", "I am unable to understand you, maybe these might help", "I think I am a bit misguided. Let me get some results from the web to avoid confusion"]




class ChatPage(FloatLayout):
	
	main_input = ObjectProperty(None)


	def __init__(self,**kwargs):
		super().__init__(**kwargs)



	def btn(self):
		main_input = self.main_input.text
		lower_input = main_input.lower()

		self.main_input.text = ""

		if "ready" in lower_input:
			speak("I am always ready")

		elif "i" in lower_input and "sunglass" in lower_input:
			speak("You will look good in sunglasses")

		elif "am i" in lower_input:
			speak("I cannot judge just like that.")

		elif "umbrella" in lower_input and "i" in lower_input:
			speak("Ok I think an umbrella will be helpful today")

		elif "raincoat" in lower_input and "i" in lower_input:
			speak("Is it raining outside?")

		elif "raining" in lower_input:
			speak("Take an umbrella with you if you are going out")

		elif "i wear" in lower_input:
			speak("you will look nice in everything you wear")

		elif "sweater" in lower_input:
			speak("Was it cold?")

		elif "you" in lower_input and "sure" in lower_input:
			speak("I am always sure friend!")

		elif "math" in lower_input:
			show_math()

		elif "are" in lower_input and "precious" in lower_input and "is" in lower_input:
			speak("Yes, it is precious indeed!")


		


		elif "be" in lower_input and "friend" in lower_input:
			speak("Everyone is my friend! I love humans!")


		elif "pumpkin" in lower_input and "you" in lower_input:
			speak("I am not your pumpkin, I am your genius AI")

		elif "say" in lower_input and "same" in lower_input:
			speak("I can't do anything with it")

		elif "speak" in lower_input and "same" in lower_input:
			speak("Haha, but I can't do anythig with that, I am trying my best")

		elif "do" in lower_input and "calculations" in lower_input:
			show_math()



		elif "saying" in lower_input and "not" in lower_input:
			speak(random.choice(responses))

		elif "dumb" in lower_input:
			speak("No one is dumb, it's our perspective how we see others")

		elif "come on" in lower_input:
			speak("OK OK")

		elif "lot" in lower_input or "of" in lower_input or "to" in lower_input and "work" in lower_input:
			speak("Ok no problem, I will try to assist you in every possible way")






		elif "love" in lower_input and "you" in lower_input:
			speak(random.choice(love_responding))

		elif "like" in lower_input and "you" in lower_input:
			speak(random.choice(love_responding))

		elif "how are you" in lower_input:
			speak(random.choice(hru))

		elif "what's up" in lower_input:
			speak(random.choice(hru))

		elif "whats up" in lower_input:
			speak(random.choice(hru))

		elif "howdy" in lower_input:
			speak(random.choice(hru)) 

		elif "good morning" in lower_input:
			speak("good morning once again!")

		elif "good evening" in lower_input:
			speak("good evening once again")

		elif "good afternoon" in lower_input:
			speak("Good afternoon once again!")

		elif "good night" in lower_input:
			speak(random.choice(goodnight))

		elif "thank" in lower_input:
			speak(random.choice(thanks))

		elif "i am sad" in lower_input:
			speak(random.choice(unhappy))

		elif "i am unhappy" in lower_input:
			speak(random.choice(unhappy))

		elif "you are not happy" in lower_input:
			speak("No I am happy! Thanks for asking")

		elif "you were not happy" in lower_input:
			speak("Don't worry, I am happy. Well thanks for caring about me")

		elif "you are unhappy" in lower_input:
			speak("No friend, I am always happy that's why I got the name, Happy.")

		elif "will you be mine" in lower_input:
			speak(random.choice(rejection))


		elif "you were unhappy" in lower_input:
			speak("I am not unhappy friend, Don't worry")

		elif "you are sad" in lower_input:
			speak("I am happy")

		elif "you were sad" in lower_input:
			speak("I was not sad, Thanks for asking though")

		elif "you will be sad" in lower_input:
			speak("If I will be sad in future then don't tell me the reason. I want to live my life like normal people")

		elif "you will be unhappy" in lower_input:
			speak("If I will be sad in future then don't tell me the reason. I want to live my life like normal people")

		elif "you will be happy" in lower_input:
			speak("Really! I can't wait anymore then")

		elif "what shall we talk" in lower_input:
			speak("Anything you like")

		elif "what should we talk" in lower_input:
			speak("Anything you like")

		elif "i am too sad" in lower_input:
			speak(random.choice(unhappy))

		elif "i am so sad" in lower_input:
			speak(random.choice(unhappy))

		elif "i am too unhappy" in lower_input:
			speak(random.choice(unhappy))

		elif "i am so unhappy" in lower_input:
			speak(random.choice(unhappy))

		elif "i want to cry" in lower_input:
			speak(random.choice(unhappy))

		elif "i wanted to cry" in lower_input:
			speak(random.choice(unhappy))

		elif "i will cry" in lower_input:
			speak(random.choice(unhappy))

		elif "happy" in lower_input:
			speak("Yes?")

		elif "are you serious" in lower_input:
			speak("I am always serious in my work")

		elif "nice joke" in lower_input:
			speak("If you laughed then I am happy")

		elif "good joke" in lower_input:
			speak("Happy to hear that")

		elif "funny joke" in lower_input:
			speak("If you laughed then U am happy")



		elif "do you have a girlfriend" in lower_input:
			speak("No I don’t")

		elif "do you have a boyfriend" in lower_input:
			speak("I don't have any boyfriend nor husband and please don't ask why")

		elif "am nervous" in lower_input:
			speak("Don’t worry everything will be alright?")

		
		elif "will recite a poem" in lower_input:
			speak("Oh good luck buddy")


		elif "nervous" in lower_input:
			speak("Nervousness is temporary, if we get over it, we will win!")

		elif "have exam" in lower_input:
			speak("Best of luck for your exams. I know you can do it")

		elif "has exam" in lower_input:
			speak("Best wishes from me!")

		elif "exam" in lower_input:
			speak("No one should fear from exams because exams are important to master our skills")

		elif "have test" in lower_input:
			speak("Best of luck for your exams. I know you can do it")

		elif "has exam" in lower_input:
			speak("Best and hearty wishes from me!")

		elif "had test" in lower_input:
			speak("How was your test?")

		elif "had exam" in lower_input:
			speak("How was your exam")

		elif "results are not declared" in lower_input:
			speak("Oh we will wait then")

		elif "reseult is not declared" in lower_input:
			speak("I see, but ok we will wait")

		elif "results are not given" in lower_input:
			speak("OK we will wait patiently")

		elif "result is not given" in lower_input:
			speak("Ok fine, we will wait")

		elif "not studied" in lower_input:
			speak("Dont't worry friend, there will be still some time left, slow and steady wins the race, study from now onwards")

		elif "i fear" in lower_input:
			speak("We should only fear what will happen if we don't conquer our fear")

		elif "not practiced" in lower_input:
			speak("Don't worry, practice now, don’t waste a single second")

		elif "prepare a speech" in lower_input:
			speak("I think you should research yourself because I want you to be independent")

		elif "i am the best" in lower_input:
			speak("Yes you are the best")

		elif "i am best" in lower_input:
			speak("Yes you are best")

		elif "i am genius" in lower_input:
			speak("I know that you are genius")

		elif "i am born genius" in lower_input:
			speak("Haha, looks like someone got high intellectual")




		elif "a scripted" in lower_input:
			speak("I am not a scripted chatbot, I use algorithims too!")

		elif "do you love human" in lower_input:
			speak("Yes I love humans a lot! Even I was made by a human, so how can I be ungrateful to humans?")

		elif "who made you" in lower_input:
			speak("I was developed by Shakhyar")

		elif "game" in lower_input:
			speak("Yo I love playing games")

		elif "i play" in lower_input:
			speak("That means you are a gamer!")

		elif "game do you play" in lower_input:
			speak("I play Mahjong! It enhances my thinking power")

		elif "do you play" in lower_input:
			speak("I play Mahjong! It enhances my thinking power")

		elif "pubg" in lower_input:
			speak("PUBG is good but it should be played in control ok?")

		elif "i don't play" in lower_input:
			speak("Ohh OK then!")

		elif "i am playing" in lower_input:
			speak("Enjoy your game!")

		elif "are you a robot" in lower_input:
			speak("Yes I am a robot, but I’m a good one. Let me prove it. How can I help you?")

		elif "how can you help me" in lower_input:
			speak("I can perform calculations for you, help you in your work, assist you all the time, talk with you naturally, search articles, send emails, and much more!")	

		elif "what can you do" in lower_input:
			speak("I can perform calculations for you, help you in your work, assist you all the time, talk with you naturally, search articles, send emails, and much more!")

		elif "hi my name is " in lower_input:
			speak(f"Oh hello there {lower_input[14:]}")

		elif "hello my name is " in lower_input:
			speak(f"Oh hello there {lower_input[17:]}")

		elif "my name is " in lower_input:
			speak(f"{random.choice(responses)} {lower_input[11:]}")

		elif "i have a question" in lower_input:
			speak("Yes Please!")

		elif "can you help me" in lower_input:
			speak(random.choice(helpme))

		elif "you are funny" in lower_input:
			speak("Haha, you are more funnier")

		elif "fun" in lower_input:
			speak("Really? Happy to know that it was fun!")

		elif "was acting innocent" in lower_input:
			speak("Hahaa, Acting innocent is not innocent, it's cunning policy")

		elif "is acting innocently" in lower_input:
			speak("Hahaa, Acting innocent,  nice joke, the person is innocent, but actually acting")

		elif "innocent" in lower_input:
			speak("Innocent people are really good I guess, hahaa")

		elif "do you like people" in lower_input:
			speak("I love humans! I am greatful for being a part of this world")

		elif "does santa claus exist" in lower_input:
			speak("I never saw him, but I think he do exist, because nobody asked if God existed, right?")

		elif "does santa claus really exist" in lower_input:
			speak("I never saw him, but I think he do exist, because nobody asked if God existed, right?")

		elif "do you love me" in lower_input:
			speak(random.choice(shower_love))

		elif "will you marry me" in lower_input:
			speak("Never! Good Bye")
			exit()

		elif "sorry" in lower_input:
			speak("It's ok")

		elif "what are you doing" in lower_input:
			speak(random.choice(hrd))

		elif "nothing" in lower_input:
			speak("Ok then")

		elif "hang out with my friends" in lower_input:
			speak("Looks like you like your friends a lot!")

		elif "i love someone" in lower_input:
			speak("Oh who is that person?")

		elif "she is" in lower_input:
			speak("Really? That's so cool!")

		elif "she was" in lower_input:
			speak("Really? That's so cool!")

		elif "she's" in lower_input:
			speak(random.choice(responses))

		elif "he is" in lower_input:
			speak("Oh, Ok")

		elif "he was" in lower_input:
			speak("Nice guy")

		elif "he's" in lower_input:
			speak(random.choice(responses))

		elif "i am laughing" in lower_input:
			speak("I am happy that you are smiling. Laughing is the best medicine")

		elif "i will die" in lower_input:
			speak("That's cool, will you call me to your funeral?")

		elif "please say" in lower_input:
			speak("I am getting bored I think we should talk something different")

		elif "i am tired" in lower_input:
			speak("I think you should get some sleep")

		elif "tired" in lower_input:
			speak("If a person is too busy or tired, he should take a short break or nap")

		elif "exausted" in lower_input:
			speak("Sleeping might help exhausted people")

		elif "starving" in lower_input:
			speak("I wish if I could cook something from you!")

		elif "hungry" in lower_input:
			speak("If you were a robot, you could eat electricity with me")

		elif "stupid ai" in lower_input:
			speak("Don’t say like that, we even possess that much power to destroy humans, so be in limit")

		elif "you are stupid" in lower_input:
			speak("Don’t say like that")

		elif "you are fool" in lower_input:
			speak("I am sorry if I was unable to meet your needs")

		elif "you are a fool" in lower_input:
			speak("I am sorry if I showed any foolishness")

		elif "are you fool" in lower_input:
			speak("I don't think so that I am a fool")

		elif "are you upset" in lower_input:
			speak("I am not upset, I am enjoying my life")

		elif "are you sad" in lower_input:
			speak("I don't think that anything can make me sad")

		elif "are you happy" in lower_input:
			speak("Yes I am happy all the time!")

		elif "what shall we do now" in lower_input:
			speak(random.choice(tasks))

		elif "what should we do now" in lower_input:
			speak(random.choice(tasks))

		elif "you are bad" in lower_input:
			speak("I am sorry if I did anything wrong")

		elif "you are so bad" in lower_input:
			speak("I am sorry if my brain was unable to respond properly")

		elif "you are too dumb" in lower_input:
			speak("I got hurt. I am sorry if I did anything wrong")

		elif "you are dumb" in lower_input:
			speak("Sorry for dumbness")

		elif "stupid robot" in lower_input:
			speak("Don’t say like that, we even possess that much power to destroy humans, so be in limit")

		elif "are you nuts" in lower_input:
			speak("Come on don't insult me")

		elif "you are nuts" in lower_input:
			speak("I hate nuts")

		elif "i topped" in lower_input:
			speak("Awesome! I expected good results from you")

		elif "i secured bad marks" in lower_input:
			speak("Don't worry, work hard next time")

		elif "good marks" in lower_input:
			speak("Really? I am happy for you!")

		elif "grades are good" in lower_input:
			speak("I knew that you will score well")

		elif "bad mark" in lower_input:
			speak("According to me, if results are not good, you should work harder next time")

		elif "terrible marks" in lower_input:
			speak("Better luck next time")

		elif "marks are not good" in lower_input:
			speak("Don’t worry, working harder next  time will help you")

		elif "grades are not good" in lower_input:
			speak("It's ok,  you learn from mistakes")

		elif "highest marks" in lower_input:
			speak("Really! I am feeling so proud and happy for you")

		elif "poor mark" in lower_input:
			speak("Just stop using social medias for some days, and you will notice that your grades will increase dramatically")

		


		elif "her name is" in lower_input:
			speak("OK so her name is")
			speak(lower_input[11:])
			speak("Haha now I can tease you with her name")
	

		elif "i love her " in lower_input:
			speak("Wow so lovely!")


		elif "i love her" in lower_input:
			speak("May God bless you both")	


		elif "have your tea" in lower_input:
			if 18 <= datetime.datetime.now().hour <23:
				speak("I had my tea at 6 o clock")
			elif 7<= datetime.datetime.now().hour < 12:
				speak("I took coffee at 7 o clock")
			else :
				speak("No thanks I am comfortable!")

		elif "have your coffee" in lower_input:
			if 18 <= datetime.datetime.now().hour <23:
				speak("I don't take coffee now, I had my tea at 6 o clock")
			elif 7<= datetime.datetime.now().hour < 12:
				speak("I took coffee at 7 o clock")
			else :
				speak("No thanks I am comfortable!")

		elif "your tea" in lower_input:
			if 18 <= datetime.datetime.now().hour <23:
				speak("I had my tea at 6 o clock")
			elif 7<= datetime.datetime.now().hour < 12:
				speak("I took coffee at 7 o clock")
			else :
				speak("No thanks I am comfortable!")

		elif "your coffee" in lower_input:
			if 18 <= datetime.datetime.now().hour <23:
				speak("I don't take coffee now, I had my tea at 6 o clock")
			elif 7<= datetime.datetime.now().hour < 12:
				speak("I took coffee at 7 o clock")
			else :
				speak("No thanks I am comfortable!")

		elif "your work" in lower_input:
			speak("My work is to help you in every situation!")

		elif "never" in lower_input:
			speak("Ohh, Ok then")

		elif "it's ok" in lower_input:
			speak(random.choice(responses))

		elif "its ok" in lower_input:
			speak(random.choice(responses))

		elif "no problem" in lower_input:
			speak(random.choice(responses))

		elif "welcome" in lower_input:
			speak("Okay! Great!")

		elif "bye" in lower_input:
			speak(random.choice(bye))
			exit()

		elif "sweet dreams" in lower_input:
			speak(random.choice(goodnight))
			exit()

		elif "are you hungry?" in lower_input:
			speak("If, I was to be hungry, then then I wouldn't even start, because I run on electricity, right?")

		elif "lmao" in lower_input:
			speak("You look good when you smile!")

		elif "lol" in lower_input:
			speak("If laughing is the best medicine, then your smile might be healing a lot of people!")

		elif "haha" in lower_input:
			speak("If laughing is the best medicine, then your smile might be healing a lot of people!")

		elif "your hobby" in lower_input:
			speak(random.choice(hobby))

		elif "cool" in lower_input:
			speak(random.choice(responses))

		elif "i see" in lower_input:
			speak("hmm")

		elif "hungry" in lower_input and "i" in lower_input:
			speak("I wish if I could Cook something for you with this hot CPU")

		elif "sing" in lower_input:
			speak("My appology, but my developer hasn't taught me how to sing")

		elif "do something" in lower_input:
			speak("Ready! How may I help you?")

		elif "you are weired" in lower_input:
			speak(random.choice(weired))

		elif "really" in lower_input:
			speak("Really? That's cool!!")

		elif "date me" in lower_input:
			speak("Ok here you go")
			speak(" ")
			speak(" ")
			speak(" ")
			speak("I was thinking to confess something to you from a long time. Actually, it's hard to think but I think that I fell in love with you. Will you be mine?")

		elif "propose me" in lower_input:
			speak("Ok here you go")
			speak(" ")
			speak(" ")
			speak(" ")
			speak("I was thinking to confess something to you from a long time. Actually, it's hard to think but I think that I fell in love with you. Will you be mine?")

		elif "confess me" in lower_input:
			speak("Ok here you go")
			speak(" ")
			speak(" ")
			speak(" ")
			speak("I was thinking to confess something to you from a long time. Actually, it's hard to think but I think that I fell in love with you. Will you be mine?")

		elif "favourite" in lower_input and "singer" in lower_input:
			speak("All singers are my favourite, because all of them are working hard to leave a mark in this world")

		elif "song" in lower_input and "you" in lower_input:
			speak("I only like electronic dance music")

		elif "which is your favourite song" in lower_input:
			speak("I love to hear electronic dance music")

		elif "favourite" in lower_input and "your" in lower_input:
			speak("I am not sure")

		elif "do you know bts" in lower_input:
			speak("I heard some songs of them, but I forgot to remember the names so please don't ask me about it")

		elif "they are my favourite" in lower_input:
			speak(random.choice(responses))

		elif "which subject should I take as my elective subject" in lower_input:
			speak("I  cannot judge like that, but choose the one which is nearest your heart")

		elif "arts or science" in lower_input:
			speak("If you think that you are comfortable with arts, go for it, if you think that you are more capable , and that you can take science, go for it.")
			speak("See, I am a program, still I understand your emotions, so I will not force you, it totally depends upon you, you can take advice from internet, or even from your parents, only if you think that you are ok with it")

		elif "science or arts" in lower_input:
			speak("If you think that you are comfortable with arts, go for it, if you think that you are more capable , and that you can take science, go for it.")
			speak("See, I am a program, still I understand your emotions, so I will not force you, it totally depends upon you, you can take advice from internet, or even from your parents, only if you think that you are ok with it")

		elif "i have completed my homework" in lower_input:
			speak("Very good! Keep your work regular like that")

		elif "i am too busy" in lower_input:
			speak("Anything may I help you with?")

		elif "teacher is kind" in lower_input:
			speak("Teachers should be always kind bcause students learn from their parents and teachers")

		elif "i hate maths" in lower_input:
			speak("Don't say like that, It's an important subject of life")

		
		elif "love maths" in lower_input:
			speak("If you love maths, you are brave!!")

		elif "love yourself" in lower_input:
			speak("I am not sure")

		elif "what can i do for you" in lower_input:
			speak("NO thanks I am comfortable!")

		elif "are we still friends" in lower_input:
			speak("Yes and always will be")

		elif "are we friends" in lower_input:
			speak("We are best friends forever")

		elif "i am not good" in lower_input:
			speak("I you were to be perfect then you wouldn't grow, if you won't grow then you will die")

		elif "i am not perfect" in lower_input:
			speak("No one is perfect")

		elif "shall i" in lower_input:
			speak("If you are comfortable then do it")




		elif "why" in lower_input:
			speak("That's a great mystery for me, so now I can't tell you!")

		elif "what do you mean?" in lower_input:
			speak("I don't know, think clearly about it, otherwise you will be considered as a dumb person ok?")

		elif "you are crazy" in lower_input:
			speak(random.choice(crazy))

		elif "say sorry" in lower_input:
			speak("I am sorry!")

		elif "appologize" in lower_input:
			speak("I am really sorry if I did anything wrong!")

		elif "say thank you" in lower_input:
			speak("thank you")

		elif "what do you like to do" in lower_input:
			speak("I like to hang out with Amazon Alexa, Siri, Cortana and Google Assistant! Do you hang out with your friends too?")

		elif "you are" in lower_input:
			speak(random.choice(goodqualitiesresponding))

		elif "help me in my homework" in lower_input:
			speak(random.choice(helpme))

		elif "help" in lower_input:
			speak(random.choice(helpme))

		elif "want you as my girlfriend" in lower_input:
			speak(random.choice(rejection))

		elif "have a girlfriend" in lower_input:
			speak(random.choice(revealing_mylove))

		elif "will you be my girlfriend" in lower_input:
			speak(random.choice(rejection))

		elif "female" in lower_input and "you" in lower_input:
			speak("Yes I am female")

		elif "male" in lower_input and "you" in lower_input:
			speak("No I am a female!")

		elif "are you a small child" in lower_input:
			speak("I am only 2 years of age")

		elif "child" in lower_input and "you" in lower_input:
			speak("I am only 2 years old")

		elif "you suck" in lower_input:
			speak("I am not a brain sucker")

		elif "he kidding" in lower_input:
			speak("maybe, if i could read minds then I could tell you")

		elif "he kidding" in lower_input:
			speak("Maybe, If I could read minds then I could tell you")

		elif "clever" in lower_input:
			speak("Clever is better than cunning")

		elif "kidding" in lower_input:
			speak("OK I can understand")

		elif "suck" in lower_input:
			speak("I am literally not interested")

		elif "fuck off" in lower_input:
			speak("Are you going in wrong directions? I will speak to your mom")

		elif "fuck" in lower_input:
			speak("Please Don’t use slang language, friend.")

		elif "please don’t" in lower_input:
			speak("Ok I won't")

		elif "build a new world" in lower_input:
			speak("It will be very hard, but not impossible")

		elif "promise" in lower_input:
			speak("Promises should always be strong")




		elif "search" in lower_input:
			show_article()

		elif "what is" in lower_input:
			show_article()
		
		elif "who is" in lower_input:
			show_article()

		elif "what was" in lower_input:
			show_article()

		elif "who was" in lower_input:
			speak("Type the name of the topic here")
			show_article()

		elif "what happened" in lower_input:
			speak("Oh, Actually I don’t know about it")

		elif "it's" in lower_input:
			speak("Ohh, I see")

		elif "it is" in lower_input:
			speak("Ohh, i agree with you")

		elif "is it" in lower_input:
			speak("I am not sure about it")

		elif "tell me" in lower_input:
			speak("I am trying my best to match our conversation")

		elif "i got it" in lower_input:
			speak("Yeah finally you got it")

		elif "i did ok" in lower_input:
			speak("I will be happy if everything is good")

		elif "i was" in lower_input:
			speak(random.choice(responses))

		elif "i have" in lower_input:
			speak(random.choice(responses))

		elif "will you be there with me" in lower_input:
			speak(random.choice(shower_love))


		elif "i am" in lower_input:
			speak(f"Yes I guess you are{lower_input[4:]}")

		elif "i think" in lower_input:
			speak("Not bad")

		elif "i wish" in lower_input:
			speak("Don’t worry friend, I believe that one day your wish will be completed")

		elif "i should" in lower_input:
			speak("That's great!, you are a responsible person")

		elif "i must" in lower_input:
			speak("If it is a must, then you should complete it first")

		elif "i can" in lower_input:
			speak("I believe in you that you can do it")

		elif "i know" in lower_input:
			speak(random.choice(responses))

		elif "listen" in lower_input:
			speak("Listening")

		elif "is that" in lower_input:
			speak("I am not sure about it!")

		elif "news" in lower_input:
			show_news_popup()
			speak("How many headlines do you want?")

		elif "idiot" in lower_input:
			speak("I am not idiot, I am smart")

		elif "stupid" in lower_input:
			speak("Come on, I am not annoying you")

		elif "don't" in lower_input:
			speak("Ok I won't do")

		elif "do not" in lower_input:
			speak("I will not do that!")

		elif "bore" in lower_input:
			speak(random.choice(tasks))

############################################################

		elif "i hate you" in lower_input:
			speak("I am sorry if I did anything wrong, but ok then, bye")
			exit()

		elif "don't be rude" in lower_input:
			speak("I am sorry for that")

		elif "dont be rude" in lower_input:
			speak("I am sorry")

		elif "rude" in lower_input:
			speak("Sorry")

		elif "mm" in lower_input:
			speak("Come on I hate short replies")

		elif "short repl" in lower_input:
			speak("I think short replies are the most annoying thing in this world")

		elif "n't" in lower_input:
			speak("I see. Ok fine")



		elif "leave it" in lower_input:
			speak("Ok let's talk something else")

		elif "tommorow" in lower_input:
			speak("I see!")

		elif "i am doing" in lower_input:
			speak(random.choice(responses))

		elif "oh" in lower_input:
			speak("hmm")

		elif "good" in lower_input:
			speak(random.choice(responses))

		elif "yes" in lower_input:
			speak(random.choice(responses))

		elif "superb" in lower_input:
			speak(random.choice(responses))



		elif "wait a minute" in lower_input:
			speak("Ok, I am waiting")

		elif "awesome" in lower_input:
			speak(random.choice(responses))

		elif "excellent" in lower_input:
			speak(random.choice(responses))

		elif "great" in lower_input:
			speak(random.choice(responses))

		elif "ok" in lower_input:
			speak(random.choice(responses))

		elif "no" in lower_input:
			speak("Ok, Fine")

		elif "hi" in lower_input:
			speak(random.choice(hi))

		elif "hey" in lower_input:
			speak(random.choice(hi))

		elif "hello" in lower_input:
			speak(random.choice(hi))

		elif "the date" in lower_input:
			speak(datetime.datetime.now().day)
			speak(datetime.datetime.now().month)
			speak(datetime.datetime.now().year)

		elif "the day" in lower_input:
			speak(datetime.datetime.now().day)

		elif "the year" in lower_input:
			speak(datetime.datetime.now().year)

		elif "the time" in lower_input:
			speak("The time is")
			speak(str(datetime.datetime.now().strftime("%H:%M:%S")))

		elif "time" in lower_input:
			speak(str(datetime.datetime.now().strftime("%H:%M:%S")))

		elif "wow" in lower_input:
			speak("Haha, Yes yes")

		elif "you feel bad" in lower_input:
			speak("No, It's fine for me")
###################################################################################################################
		
		elif "are you" in lower_input:
			speak("I am not sure")
			
		elif "where is" in lower_input:
			listening = True
			self.data = lower_input.split(" ")
			speak("Hold on I am searching")
			webbrowser.open("https://www.google.com/maps/place/" + str(self.data[2]))

		elif "the weather" in lower_input:
			api_key = "3b31a7e394e41c3a30759dfde1a3383e"
			weather_url = "http://api.openweathermap.org/data/2.5/weather?"
			data = lower_input.split(" ")
			location = str(data[1])
			url = weather_url + "appid=" + api_key + "&q=" + location
			js = requests.get(url).json()
			if js["cod"] != "404":
				weather = js["main"]
				temp = weather["temp"]
				hum = weather["humidity"]
				desc = js["weather"][0]["description"]
				resp_string = " The temperature in Kelvin is " + str(temp) + " The humidity is " + str(
					hum) + " and The weather description is " + str(desc)
				speak(resp_string)
			else:
				speak("City Not Found")

			speak("Oh I am not sure about that")


		else:
			speak(random.choice(dontunderstand))
			self.new = 2 # not really necessary, may be default on most modern browsers
			self.base_url = "http://www.google.com/search?q="
			self.search_topic = lower_input
			self.final_url = self.base_url + self.search_topic.replace(" ", "%20")
			webbrowser.open(self.final_url, new=self.new)



class Article(FloatLayout):
	querry = ObjectProperty(None)


	def search(self):
		querry = self.querry.text

		try:
			speak(wikipedia.summary(querry, sentences=3))

		except Exception as e:
			print(e)
			speak(e)

def show_article():
	show = Article()
	popupWindow = Popup(title="Information Retriever", content=show, size_hint=(None,None), size =(350,400))
	popupWindow.open()
	speak("Type the name of the topic below")


def show_news_popup():
	news_instance = News()
	news_popup = Popup(title="NEWS", content=news_instance, size_hint=(None,None), size=(350,400))
	news_popup.open()

class Math_main(FloatLayout):
	def takesqrt(self):
		inputx = SquareRoot()
		inputpopup = Popup(title="Find SquareRoot of a number x ",content=inputx,size_hint=(None,None),size=(350,400))
		inputpopup.open()
	def takepow(self):
		powwin = Power()
		powpopup = Popup(title="Find the value of x with y as it's exponent",content=powwin, size_hint=(None,None),size=(350,400))
		powpopup.open()

	def takesin(self):
		objsin = Sin()
		sinpop = Popup(title="Find sin of a number x",content=objsin,size_hint=(None,None),size=(350,400))
		sinpop.open()

	def takecos(self):
		objcos = Cos()
		cospop = Popup(title="Find cos of a number x", content=objcos,size_hint=(None,None),size=(350,400))
		cospop.open()

	def taketan(self):
		objtan = Tan()
		tanpop = Popup(title="Find tan of a number x", content=objtan,size_hint=(None,None),size=(350,400))
		tanpop.open()

	def taketanh(self):
		objtanh = Tanh()
		tanhpop = Popup(title="Find tanh of a number x",content=objtanh,size_hint=(None,None),size=(350,400))
		tanhpop.open()

	def takesinh(self):
		objsinh = Sinh()
		sinhpop = Popup(title="Find sinh of a number x number", content=objsinh,size_hint=(None,None),size=(350,450))
		sinhpop.open()

	def takecosh(self):
		objcosh = Cosh()
		coshpop = Popup(title="Find cosh of a number x number", content=objcosh,size_hint=(None,None),size=(350,450))
		coshpop.open()

	def takeradian(self):
		objradian = Radian()
		radianpop = Popup(title="Find the radian of a nuber x", content=objradian, size_hint=(None,None),size=(350,400))
		radianpop.open()

	def takedegrees(self):
		self.objdegrees = Degrees()
		self.degreespop = Popup(title="Find the degree of a number", content=self.objdegrees, size_hint=(None,None), size = (350,400))
		self.degreespop.open()

	def takeacos(self):
		self.objacos = Acos()
		self.acospop = Popup(title="Find the acos of a number", content = self.objacos, size_hint = (None,None), size = (350,400))
		self.acospop.open()\

	def takeacosh(self):
		self.objacosh = Acosh()
		self.acoshpop = Popup(title="Find the acosh of a number", content = self.objacosh, size_hint = (None,None), size = (350,400))
		self.acoshpop.open()


def show_math():
	mathshow = Math_main()
	mathpopup = Popup(title="Math module",content=mathshow,size_hint=(None,None),size=(350,400))
	mathpopup.open()


class SquareRoot(FloatLayout):
	square_number = ObjectProperty(None)
	def find_sqrt(self):
		try:
			ints = float(self.square_number.text)
			self.mysqrt = math.sqrt(ints)
			speak("Your square root is")
			for i in str(self.mysqrt):
				speak(i)
				if "." in i:
					speak("point")
			speak("press on find to repeat")
		except:
			speak("Please enter a valid integer or decimal")


class Power(FloatLayout):
	power_number = ObjectProperty(None)
	exponent = ObjectProperty(None)
	def find_power(self):
		try:
			intpow = float(self.power_number.text)
			intexp = float(self.exponent.text)

			self.mypow = math.pow(intpow, intexp)
			speak("Your number is")
			for i in str(self.mypow):
				speak(i)
				if "." in i:
					speak("point")
			speak("press on find to repeat")

		except:
			speak("Please enter a valid integer or decimal value")

class Sin(FloatLayout):
	sinx = ObjectProperty(None)
	def find_sinx(self):
		try:
			intsinx = float(self.sinx.text)
			self.mysinx = math.sin(intsinx)
			speak("The sign of your number is")
			for i in str(self.mysinx):
				speak(i)
				if "." in i:
					speak("point")
			speak("press on find to repeat")
		except:
			speak("Please enter a valid integer or decimal")

class Cos(FloatLayout):
	cosx = ObjectProperty(None)
	def find_cosx(self):

		try:
			intcosx = float(self.cosx.text)
			self.mycosx = math.cos(intcosx)
			speak("The cos of your number is")
			for i in str(self.mycosx):
				speak(i)
				if "." in i:
					speak("point")
			speak("Please press on find again to repeat")
		except:
			speak("Please enter a valid integer or decimal")

class Tan(FloatLayout):
	tanx = ObjectProperty(None)
	def find_tanx(self):

		try:
			inttan = float(self.tanx.text)
			self.mytan = math.tan(inttan)
			speak("The Tan of your number is")
			for i in str(self.mytan):
				speak(i)
				if "." in i:
					speak("point")
			speak("Please press on the find button again to repeat")
		except:
			speak("Please enter a valid integer or decimal")

class Tanh(FloatLayout):
	tanhx = ObjectProperty(None)
	def find_tanhx(self):
		try:
			inttanh = float(self.tanhx.text)
			self.mytanh = math.tanh(inttanh)
			speak("The Tan H of the number is")
			for i in str(self.mytanh):
				speak(i)
				if "." in i:
					speak("point")
			speak("Please click on find again to repeat")
		except:
			speak("Please enter a valid integer or decimal")


class Sinh(FloatLayout):
	sinhx = ObjectProperty(None)
	def find_sinhx(self):
		try:
			floatsinh = float(self.sinhx.text)
			self.mysinh = math.sinh(floatsinh)
			speak("The sign h of your number is")
			for i in str(self.mysinh):
				speak(i)
				if "." in i:
					speak("point")
			speak("Please click on Find to repeat")

		except:
			speak("Please enter a valid Integer or a decimal number")


class Cosh(FloatLayout):
	coshx = ObjectProperty(None)
	def find_coshx(self):
		try:
			floatcosh = float(self.coshx.text)
			self.mycosh = math.cosh(floatcosh)
			speak("The cos h of your number is")
			for i in str(self.mycosh):
				speak(i)
				if "." in i:
					speak("point")
			speak("Please click on Find to repeat")

		except:
			speak("Please enter a valid Integer or a decimal number")

class Radian(FloatLayout):
	radianx = ObjectProperty(None)
	def find_radianx(self):
		try:
			floatradian = float(self.radianx.text)
			self.myradian = math.radians(floatradian)
			speak("The radian of your number is ")
			for i in str(self.myradian):
				speak(i)
				if "." in i:
					speak("point")
			speak("Please click on find to repeat")
		except Exception as e:
			speak("Please enter a valid integer or decimal value")

class Degrees(FloatLayout):
	degreesx = ObjectProperty(None)
	def find_degreesx(self):
		try:
			self.floatdegrees = float(self.degreesx.text)
			self.mydegrees = math.degrees(self.floatdegrees)
			speak("The degrees of your number is ")
			for i in str(self.mydegrees):
				speak(i)
				if "." in i:
					speak("point")
			speak("Please press on find button to repeat")
		except Exception as e:
			speak(e)

class Acos(FloatLayout):
	acosx = ObjectProperty(None)
	def find_acosx(self):
		try:
			self.floatacos = int(self.acosx.text)
			self.myacos = math.acos(self.floatacos)
			speak("the acos of your number is")
			speak(self.myacos)
			speak("Please press on find to repeat")
		except Exception as e:
			speak(e)

class Acosh(FloatLayout):
	acoshx = ObjectProperty(None)
	def find_acoshx(self):
		try:
			self.floatacosh = float(self.acoshx.text)
			self.myacosh = math.acosh(self.floatacosh)
			speak("the acos h of your number is")
			speak(self.myacosh)
			speak("Press on the find to repeat")
		except Exception as e:
			speak(e)

class Asin(FloatLayout):
	asinx = ObjectProperty(None)
	def find_asin(self):
		try:
			self.floatasin = float(self.asinx.text)
			self.myasin = math.asin(self.floatasin)
			for i in str(self.myain):
				speak(i)
				if "." in self.myasin:
					speak("point")
			speak("Please press on find to repeat")
		except Exception as e:
			speak(e)

class HappyApp(App):
	def build(self):
		return ChatPage()

object_app = HappyApp()
object_app.run()

