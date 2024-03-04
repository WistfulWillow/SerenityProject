define y = Character("[povname]")
define r = Character("Ria Takashi")
define a = Character ("Amiaryllis")

transform jumper:
 ease .1 yoffset 24
 ease .08 yoffset -24
 ease .05 yoffset 8
 ease .02 yoffset -8
 ease .01 yoffset 4
 ease .01 yoffset -4
 ease .01 yoffset 0

transform sadbounce:
 ease .5 yoffset 8
 ease .3 yoffset 0
 
transform slideleft: 
 ease 1 xoffset -500
 
transform darken:
 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
 linear 0.5 matrixcolor TintMatrix("#4e4e4e") * SaturationMatrix(1.0)
transform lighten:
 linear 0.5 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

label start:
 scene canal
 play music "audio/Canal.wav" fadein 1.0
 "???" "Hey! Wake up!"
 "I slowly open my eyes."
 "You" "Ugh..."
 show ria raised_frown with dissolve:
  zoom 0.5
  xpos 500
  ypos 60
 "As everything comes into focus, I realize there is a girl standing above me. What...?"
 "???" "Hey! Can you hear me?"
 "You" "U-Uh-"
 "???" "Oh, so you can."
 "???" "Good. I really thought you were dead, the way you were lying here."
 "You" "Huh? Why?"
 show ria furrowed_frown:
  zoom 0.5
  xpos 500
  ypos 60
 "???" "Oh, come on! Of course I thought you were dead. You were on the sidewalk unconscious!"
 "You" "Huh..."
 "As you repeat yourself, the girl sighs with annoyance. A moment of silence passes between the two of you."
 "As you stare, the girl stares back."
 "???" "Why the hell are you looking at me like that?!"
 "You" "A-Ah, sorry-"
 "I carefully stand up, taking in my surroundings better. And one thing stands out most of all."
 "This girl...is so small!"
 show ria frown:
  zoom 0.5
  xpos 500
  ypos 60
 "???" "Well, if you’re fine, I’ll be on my way."
 menu:
  "Wait!":
   "You" "Wait!"
   "Before she turns to leave, the girl gives you a scowl."
   show ria furrowed_frown:
    zoom 0.5
    xpos 500
    ypos 60
   "???" "What?"
   "You" "Who- Who are you?"
  "Oh. Okay.":
   "You" "Oh. Okay."
   "Before she turns to leave, the girl gives you a scowl."
   show ria furrowed_frown:
    zoom 0.5
    xpos 500
    ypos 60
   "???" "Won't you even ask who I am?"
   "You" "Sorry..."
   "You" "Who are you?"
"She sighs."
"???" "My name is Ria Takashi. And who are you?"
python:
      povname = renpy.input("What is your name?", length=32)
      povname = povname.strip()
      if not povname:
         povname = "Alex"
y "My name is [povname]."
r "Huh. Well, nice to meet you, [povname]."
r "But if you'll excuse me, I need to go."
y "Why?"
"I ask on impulse. She averts her gaze."
show ria averted_frown:
    zoom 0.5
    xpos 500
    ypos 60
r "..."
r "It's none of your business. Goodbye."
hide ria averted_frown
with moveoutleft
"She walks away with a confident stride, clearly going to somewhere specific. That interaction was...strange."
"I look around with a sigh. So I really passed out here again, huh?"
"Guess it's time to go home."

scene train morning with fade
play music "audio/lofi.mp3" fadein 0.5
"I stepped onto the train, my daily commute beginning. The train was rather full, and internally I sighed in relief that I managed to get a seat."

"My usual routine played out: scrolling through social media, listening to music, taking a 5 minute nap... My destination was the terminus, which was quite far."
"I couldn’t complain, really; I could have some wind-down time before work, which did wonders for my mental health."

"By the second-to-last stop, the majority of the crowd had dispersed. Only me and three others remained. I knew my stop was coming soon, so I began to pack my things."
show transition with hpunch
play music "audio/Evans.mp3" fadein 1.0
"...A sudden jolt, and the train slowed to a halt."

"Huh? What was going on? I was so confused."
"I waited for an announcement of some sort, but a few minutes went by with nothing. The power was still on, but there was no reaction at all from the train crew. Come to think of it, I hadn’t seen them for a while..."
show int sad with dissolve:
 zoom 0.8
 xpos 500
 ypos -50
"???" "Oh no, oh no, oh no..."
"I heard panicked muttering coming from the seat across from me."

"I looked across to see a girl rocking back and forth in her seat, an extremely troubled look on her face."

y "Are you alright?"

show int sad at jumper
"She jumped at hearing my voice."

y "Ah- Sorry, I didn’t mean to scare you."
"???" "N-No... It’s fine..."
"She stood up, beginning to pace around."
show int sad_talk:
 zoom 0.8
 xpos 500
 ypos -50
"???" "Am I okay...? Am I..."

"I sighed."

y "Can we try to stay calm please? I’m sure we’ll get some sort of announcement soon."

show int eyeclose_smile_talk:
 zoom 0.8
 xpos 500
 ypos -50
"To my surprise, she started giggling."

"???" "Are you stupid? It’s been almost 15 minutes!"

hide int eyeclose_smile_talk with dissolve
"Well, it didn’t seem like I’d get anywhere trying to talk to her for now."

"I turned to the other side, where two more girls were sat. The first one seemed oddly familiar."

"I stood up, deciding to approach."
y "Uh, excuse me?"
show am nervous with dissolve:
 zoom 0.5
 xpos 1200
 ypos 60
show ria frown with dissolve:
 zoom 0.5
 xpos 500
 ypos 60
"They both looked up at me. A glint of recognition appeared in the first girl’s eyes."

y "Ria?"
show ria raised_frown:
 zoom 0.5
 xpos 500
 ypos 60
show am angry_talk:
 zoom 0.5
 xpos 1200
 ypos 60
"???" "Hey! Don’t address her by first name, you stranger!"
r "Calm, Ami. I know her."
show am sad_talk:
 zoom 0.5
 xpos 1200
 ypos 60
"Ami?" "Oh. Apologies, ma’am."
y "I really didn’t think I’d see you again..."
r "Neither did I. You’re the weirdo who fell asleep by the canal, right?"
y "...Yeah."
"How rude... although she wasn’t exactly wrong..."

y "W-well-"

"I wasn’t sure what to say now I’d struck conversation."

y "Uh, the train seems to have broken."
show ria furrowed_frown:
 zoom 0.5
 xpos 500
 ypos 60
r "I’m well aware."
y "Y-Yeah..."

"I internally groaned. Why did I have to be so damn awkward?!"

y "So, uh, who’s the girl next to you?"
r "Well-"

show am angry_talk at jumper:
 zoom 0.5
 xpos 1200
 ypos 60
"Before she could finish, the girl in question stood up quickly, standing in between us."

a "My name is Amiaryllis. I am Major Takashi’s personal bodyguard!"
y "Wait, what?"

"I glanced between them for a moment."

"The clothes, the posture, the attitude-it all made sense now."

y "You work in the Government?"

a "We both work in the Military."
y "W-Woah..."

"I was really meeting with real soldiers... But more to the point, Ria looked no older than 13!"

"I decided not to say anything, for fear of sparking a disagreement."
show ria furrowed_frown at slideleft:
 zoom 0.5
 xpos 500
 ypos 60
hide am angry_talk
show int averted_talk with moveinright:
 zoom 0.8
 xpos 500
 ypos -50
"???" "You work in the Military?!"

"The strange girl from before approached us."
show int sad at jumper:
 zoom 0.8
 xpos 500
 ypos -50
a "Stay back!"

"She shuffled to the side so she was in the way of both of us."
hide int sad with dissolve
show am angry_talk:
 zoom 0.5
 xpos 1200
 ypos 60
a "Stop asking Major Takashi so many questions or there’ll be trouble! She does not wish to be bothered at this time!"
show ria averted_frown
"Ria sighed, looking out of the window."

y "Alright, alright!"
hide am angry_talk with dissolve
hide ria averted_frown with dissolve
"I stepped back, returning to my seat."

"This situation was so strange. Imagining being stuck in this train with this crew made me more nervous than the initial train breaking..."
scene train afternoon with dissolve

"It had been an hour, and we hadn’t heard any updates. The anxious girl had passed out, Ria was trying to pry open the doors and windows, and Amaryllis was standing beside her, giving me death glares whenever I so much as looked at her precious Ria."
"There was nothing I could do but sit idly, waiting. My phone didn’t even have any signal here."
show am nervous at darken:
 zoom 0.5
 xpos 1200
 ypos 60
show ria eyeclose_furrowed_frown:
 zoom 0.5
 xpos 500
 ypos 60
r "Ugh! I give up!"

show am nervous at jumper:
 zoom 0.5
 xpos 1200
 ypos 60
"Ria threw her wrench to the ground in frustration. Amiaryllis immediately scrambled to pick it up."
show ria furrowed_frown:
 zoom 0.5
 xpos 500
 ypos 60
r "I give up. There's no way out of this place."
y "Yeah. Seems so..."

"A long moment of silence filled the train."

y "I guess we have no choice but to keep waiting."

"Ria nodded."
show am nervous at lighten:
 zoom 0.5
 xpos 1200
 ypos 60

a "There must be something we can do! What about the meeting!?"

"Ria takes out her phone from her bag and begins fiddling with it."

y "I wouldn’t bother, I couldn’t get any signal."
r "Well, you don’t work for the Government, do you?"
"She replied sassily. I sighed, letting her find out the hard way."
show ria eyeclose_furrowed_frown with fade:
 zoom 0.5
 xpos 500
 ypos 60
r "Damn it!"
y "Told you so."
r "Shut up!"

"Amiaryllis gave me another hard glare. I sighed for what felt like the thousandth time."

"Finally, the other girl began to wake up."

"???" "Wh...Where am I.."
y "Still on the train..."
"???" "Really?"

show ria furrowed_frown:
 zoom 0.5
 xpos 500
 ypos 60
"We all nodded."

"???" "Damn it."

"She sighed, standing up."

"???" "There’s really been no updates at all?"
y "Nope."
r "This is ridiculous."
a "Agreed!"
y "Well it’s not like complaining is gonna’ change anything."
r "True..."

"Just then, my stomach began to rumble."

y "Ugh..."

"???" "Are you hungry?"
y "Yeah. I skipped breakfast."
show am sad_talk
a "That’s really careless."
y "Well in my defense, I didn’t know we’d be stuck in the train for so long!"
"???" "Please, let’s not fight."
"Ria tutted."
show ria averted_frown
r "This whole situation is insane."
y "Agreed."
scene train evening with fade
"The mood had dropped significantly."

return