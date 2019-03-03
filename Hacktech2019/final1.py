def hacktech(frame):
	#!/usr/bin/env python
	# coding: utf-8

	# In[1]:


	import os
	import matplotlib.pyplot as plt
	from scipy.io import wavfile
	from gtts import gTTS 
	import os 
	from pygame import mixer
	from pygame import sndarray
	import soundfile as sd


	# In[2]:


	import subprocess
	import cv2
	import numpy as np
	import time
	from skimage.transform import rescale, resize, downscale_local_mean

	im = frame;

	def rgb2gray(rgb):
	    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
	print(im.shape)
	img = rgb2gray(im);
	print(img.shape)
	img = rescale(img, 300 / min(img.shape[0],img.shape[1]), anti_aliasing=False)

	print(img.shape)

	#print(image_rescaled.shape)
	cv2.imwrite("Img.jpg", img);
	p = subprocess.Popen('pwd',shell=True)
	p = subprocess.Popen('cd darknet;pwd',shell=True);
	p = subprocess.Popen('ls /home/charan/Downloads/hacktech/Hacktech2019/darknet/cfg/yolov2-tiny.cfg',shell=True);
	p = subprocess.Popen('ls /home/charan/Downloads/hacktech/Hacktech2019/darknet/yolov2-tiny.weights',shell=True);
	p = subprocess.Popen('ls /home/charan/Downloads/hacktech/Hacktech2019/Img.jpg',shell=True);
	p = subprocess.Popen('cd /home/charan/Downloads/hacktech/Hacktech2019/darknet/; /home/charan/Downloads/hacktech/Hacktech2019/darknet/darknet detect /home/charan/Downloads/hacktech/Hacktech2019/darknet/cfg/yolov2-tiny.cfg /home/charan/Downloads/hacktech/Hacktech2019/darknet/yolov2-tiny.weights /home/charan/Downloads/hacktech/Hacktech2019/Img.jpg > /home/charan/Downloads/hacktech/Hacktech2019/darknet/1.txt;', stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)

	#subprocess.run(["cd /home/charan/darknet; ./darknet detect cfg/yolov2-tiny.cfg ~/Downloads/yolov2-tiny.weights data/dog.jpg >~/1.txt"])


	# In[3]:


	time.sleep(3)
	file = open("/home/charan/Downloads/hacktech/Hacktech2019/darknet/1.txt","r");
	s=file.readline()
	obj,left,top,right,bottom = [],[],[],[],[]
	percentMatch = []
	for line in file: 
	    obj.append((line.split(' '))[0].replace(':',''))
	    percentMatch.append(int(line.split(' ')[1].replace('%','')))
	    s=file.readline();
	    a,b,c,d = s.split(',');
	    left.append(int(a));
	    top.append(int(b));
	    right.append(int(c));
	    bottom.append(int(d));
	    print(s)
	print(obj,percentMatch,left,top,right,bottom)    
	    


	# In[4]:


	sample = 1000
	def funcToCreateVoice(pixelValue,vPos, slope, c):    
	    Fs = 2000
	    #print(pixelValue)
	    f = slope*(vPos+1)+c
	    x = np.arange(sample)
	    y = pixelValue*np.sin(2 * np.pi * f * x / Fs)
	    return y;


	# In[5]:



	def quantize(im):
		
	    for i in range(im.shape[0]):
		
	        for j in range(im.shape[1]):
	            if(im[i,j]<65):
	                im[i,j]=64;
	            elif(im[i,j]<128 and im[i,j]>65):
	                im[i,j]=127;
	            elif(im[i,j]<192 and im[i,j]>128):
	                im[i,j]=191;
	            elif(im[i,j]<256 and im[i,j]>192):
	                im[i,j]=255;
	    plt.figure(),plt.imshow(im,'gray');
	    return im;


	# In[6]:


	# crop the first object::
	from scipy.io import wavfile
	import wavio
	language = 'en'
	mixer.init();
	mixer.music.set_volume(0.85)
	megaResult = []
	for i in range(len(obj)):
	    if(percentMatch[i]<11):
	        continue;
	    print(left[i],right[i],top[i],bottom[i])
	    subImg =(img[top[i]:bottom[i],left[i]:right[i]]);   
	    subImg = quantize(subImg)
	    print(subImg.shape)
	    #print(subImg)
	    # form a slope equation
	    slope = -(22000-200)/subImg.shape[0];
	    # c=y-slope*vPos
	    c = (22000-slope)*1;
	    result = []
	    pixelSum = np.zeros((len(obj),im.shape[1]))
	    
	    for y in range(subImg.shape[1]):
	        out = np.zeros(sample);
	        for x in range(subImg.shape[0]):                
	            out += funcToCreateVoice(subImg[x,y],x, slope,c);            
	            pixelSum[i][x] += subImg[x,y];        
	        result.append(out/subImg.shape[0]);                
	        pixelSum[i][y] /= subImg.shape[0]   
	    #wavfile.write('/home/charan/'+obj[i]+'.wav',44100,((np.array(result)).flatten()))
	    out = ((np.array(result)).flatten())    
	    #print(type(out),out.dtype)
	    #out = out.astype(np.int16)
	    #print(type(out),out.dtype)
	    #wavfile.write('/home/charan/'+obj[i]+'.wav',44100,out)
	    #print(out)
	    #plt.plot(out)
	    sd.write('./'+obj[i]+'.wav',out,44100,'PCM_16')
	    #wavio.write('/home/charan/'+obj[i]+'.wav', out , rate=44100)
	    
	    #cv2.imwrite("/home/charan/darknet/data/"+obj[i]+"1.jpg", subImg);
	    #print("1")
	    myobj = gTTS(text=obj[i], lang=language, slow=False) 
	    #print("2")
	    myobj.save("welcome.mp3")  
	    #print("3")
	    time.sleep(1)
	    mixer.music.load("welcome.mp3");    
	    mixer.music.play()
	    #print("4")    
	    time.sleep(1)    
	    mixer.music.load('./'+obj[i]+'.wav');    
	    #print("playing")
	    mixer.music.play()
	    #print("done")
	    #print("5")
	    time.sleep(1)
	    megaResult.append(result);


	# In[7]:





	# In[8]:


	from gtts import gTTS 
	import os 
	language = 'en'
	myobj = gTTS(text='Scene', lang=language, slow=False) 

	myobj.save("welcome.mp3")  
	mixer.init();
	mixer.music.load("welcome.mp3");
	mixer.music.set_volume(0.85)
	mixer.music.play()


	# In[9]:


	import requests
	import cv2
	import io
	import matplotlib.pyplot as plt


	# In[10]:


	def tag_image(image):
	    r = requests.post(
		"https://api.deepai.org/api/places",
		files={
		    'image': open(image, 'rb'),
		},
		headers={'api-key': '87d1c49a-11d5-4977-bbb7-735f5c0405f6'}
	    )
	    return r.json()


	# In[11]:


	retDict = tag_image('Img.jpg')['output'];
	print(retDict)
	tags = []
	for val in retDict.values():
	    for item in val:
	        if item['confidence']>0.10:
	            if item['name'] is not None:
	                tags.append(item['name'])                    
	if(len(tags)==0):
	    tags.append(retDict['places'][0]['name'])
	print(tags)


	# In[12]:


	import freesound

	client = freesound.FreesoundClient()
	client.set_token("jBsEpHySUKYAuHIexcBd5UrrvYfNG5lBkA4wIBVV","token")
	for val in tags:
	    results = client.text_search(query=val, fields="id,name,previews")
	print(results)
	i=0
	listSoundNames = []
	for sound in results:
	    i=i+1
	    if i<2:                
	        sound.retrieve_preview("./",sound.name.replace('.','_').replace(' ','_')+'.mp3')
	    listSoundNames.append('./'+sound.name.replace('.','_').replace(' ','_')+'.mp3')
	    print(sound.name)
	print(listSoundNames)
	if(len(listSoundNames)==0):
	    myobj = gTTS(text="Not Scenic", lang=language, slow=False) 
	    myobj.save("welcome.mp3")  
	    mixer.init();
	    mixer.music.load("welcome.mp3");
	    mixer.music.play()	
	    return;
	# In[13]:





	# In[15]:


	import scipy
	import time
	from pygame import mixer
	from gtts import gTTS 
	import os 
	language = 'en'
	myobj = gTTS(text=tags[0], lang=language, slow=False) 

	myobj.save("welcome.mp3")  
	mixer.init();
	mixer.music.load("welcome.mp3");
	mixer.music.play()
	mixer.init();
	mixer.music.load(listSoundNames[0]);
	mixer.music.play()
	time.sleep(10)
	mixer.music.stop()


	# In[ ]:





	# In[ ]:





	# In[ ]:





	# In[ ]:





	# In[ ]:





	# In[ ]:




