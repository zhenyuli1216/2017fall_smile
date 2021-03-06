import glob #look for file
from shutil import copyfile # copy file from one to another one
from shutil import move


emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"] 
participants = glob.glob("./source_emotion/*") 
for x in participants: #x source_emotion/S005
	part = x[-4:] 
	for sessions in glob.glob("%s/*" %x): #sessions source_emotion/S005/001
		for files in glob.glob("%s/*" %sessions): #source_emotion/S005/001/....txt
			current_session = files[17:-30] #S005/001
			file = open(files,'r')			
			emotion = int(float(file.readline()))
			pictures = glob.glob("./source_images/%s/*" %(current_session))
			if not pictures:
				continue
			pictures.sort()
					
			neutral_face = pictures[0]
			emotional_face = pictures[-1]
		
			copyfile(neutral_face, "./sorted_set/neutral/%s"%(part))
			copyfile(emotional_face, "./sorted_set/%s/%s"%(emotions[emotion], part))
