from bitstring import BitArray, BitStream

TRANS_TIME=500 #transition time in ms

song2mood=dict()
mood2color=dict()
color2hsb=dict()

def grace_to_hsb(text):
	return color_to_hsb(mood_to_color(grace_to_mood(text)))

def grace_to_mood(text):
	if text not in song2mood:
		print "Not found: " + text
		return "calm"
	return song2mood[text]

def mood_to_color(text):
	if text not in mood2color:
		print "Big Error!!!", text, len(text)
	return mood2color[text]

def color_to_hsb(text):
	if text not in color2hsb:
		print "Bigger Error!!!", text
	return color2hsb[text]


song2mood["Arousing / Energizing Groove"]="exciting"
song2mood["Arrogant / Attitude / Defiant"]="defiant"
song2mood["Bittersweet Pop"]="melancholy"
song2mood["Blue / Depressed / Lonely"]="melancholy"
song2mood["Casual Jaunty / Funky Groove"]="cheerful"
song2mood["Chaos / Pain"]="distressed"
song2mood["Cheerful / Carefree Pop"]="cheerful"
song2mood["Cheerful / Playful / Lighthearted"]="cheerful"
song2mood["Confident / Tough Party"]="powerful"
song2mood["Cool Beats & Loops"]="exciting"
song2mood["Creepy / Eerie / Ominous"]="melancholy"
song2mood["Dark / Cool / Melancholy"]="melancholy"
song2mood["Dark / Dreamy / Brooding"]="calm"
song2mood["Dark Alienated / Brooding"]="distressed"
song2mood["Dark Dramatic / Emotional / Thrilling"]="exciting"
song2mood["Dark Grim Caution / Suspicion"]="protective"
song2mood["Dark Groovy / Savvy"]="powerful"
song2mood["Dark Hard Beat"]="powerful"
song2mood["Dark Intense Pop Determination"]="powerful"
song2mood["Dark Pop"]="exciting"
song2mood["Dark Romantic Lively Rhythm"]="exciting"
song2mood["Dark Sprightly / Playful"]="cheerful"
song2mood["Dark Twangy / Strumming"]="exciting"
song2mood["Deep Dreamy Relaxing Beat"]="calm"
song2mood["Determined / Bitter / Serious / Jaded"]="defiant"
song2mood["Driving Dark Groove"]="powerful"
song2mood["Edgy / Sexy"]="exciting"
song2mood["Enchanted / Mysterious / Dreamy"]="calm"
song2mood["Energetic / Invigorating / Joyous"]="exciting"
song2mood["Energetic Abstract Groove"]="exciting"
song2mood["Energetic Anxious / Hurt / Frustrated"]="distressed"
song2mood["Energetic Hypnotic Rhythm & Vocal"]="calm"
song2mood["Energetic Melancholy"]="melancholy"
song2mood["Enigmatic / Brooding / Mysterious"]="calm"
song2mood["Euphoric Energy & Power"]="exciting"
song2mood["Evocative & Intriguing"]="exciting"
song2mood["Exuberant / Festive"]="cheerful"
song2mood["Fiery Passionate Rhythm"]="exciting"
song2mood["Gentle Bittersweet"]="calm"
song2mood["Gritty / Earthy / Soulful"]="dignified"
song2mood["Happy Energetic Excitement"]="exciting"
song2mood["Heavy Body Beat"]="powerful"
song2mood["Heavy Loud Emo-Brooding"]="melancholy"
song2mood["Intimate Nostalgic Bittersweet"]="melancholy"
song2mood["Light / Delicate / Gentle / Tranquil"]="secure"
song2mood["Light Soft Soulful"]="calm"
song2mood["Lite Glossy Sensual Groove"]="tender"
song2mood["Lite Groovy / Dreamy / Precious"]="protective"
song2mood["Lite Melancholy"]="melancholy"
song2mood["Loud Celebratory"]="exciting"
song2mood["Other"]=""
song2mood["Peaceful / Healing / Reverent"]="protective"
song2mood["Positive Energetic Abstract Beat"]="exciting"
song2mood["Positive Loud Strength & Glory"]="powerful"
song2mood["Quiet / Introspective"]="calm"
song2mood["Sensitive Meandering / Exploring"]="calm"
song2mood["Sentimental"]="secure"
song2mood["Serious/ Cerebral / Questioning"]="dignified"
song2mood["Showy / Dramatic / Rousing / Lively"]="exciting"
song2mood["Smokey Romantic "]="tender"
song2mood["Soft Sensual / Intimate"]="tender"
song2mood["Somber / Solem / Spiritual"]="melancholy"
song2mood["Sophisticated / Lush / Romantic"]="dignified"
song2mood["Soulful Easy Beat"]="secure"
song2mood["Soulful Jubilant / Joyous Strength"]="powerful"
song2mood["Sultry / Swank"]="tender"
song2mood["Tender Sad / Soulful"]="melancholy"
song2mood["Triumphant / Rousing"]="powerful"
song2mood["Upbeat Pop Groove"]="exciting"
song2mood["Wistful / Melancholy / Forlorn"]="melancholy"

mood2color["calm"]="green"
mood2color["cheerful"]="yellow"
mood2color["defiant"]="redorange"
mood2color["dignified"]="purple"
mood2color["distressed"]="orange"
mood2color["exciting"]="red"
mood2color["melancholy"]="purpleblue"
mood2color["powerful"]="crimson"
mood2color["protective"]="coral"
mood2color["secure"]="blue"
mood2color["tender"]="cyan"
mood2color[""]="white"

# from random import random
# def rando():
# 	return ( int(random() * 65535) , int(random() * 65535) , int(random() * 65535), int(random() * 6500 + 2500) )

color2hsb["green"]=23189,65535,35031,9000
color2hsb["yellow"]=10758,65535,32276,3310
color2hsb["orange"]=6550,65535,40796,2500
color2hsb["redorange"]=5251,64552,40796,2500
color2hsb["crimson"]=65535,65535,65535,3500
color2hsb["red"]=63356,62322,55766,2500
color2hsb["coral"]=65535,24430,35361,3500
color2hsb["purple"]=53494,65535,35361,3500
color2hsb["purpleblue"]=49781,65535,35361,3500
color2hsb["blue"]=43589,65535,44482,9000
color2hsb["cyan"]=32241,65535,33738,3500
color2hsb["white"]=0,0,20000,4723


if __name__ == "__main__":
	# print constructBody((0,65535,52428), TRANS_TIME)
	pass