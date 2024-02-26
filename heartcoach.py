import tkinter as tk
import customtkinter
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"







#import all external data of groups. // creates variable
doesSmoke = True
sexMF = int()

#want user to input their own data ie. weight, height, age, do they smoke? etc
sex = str(input("What is your sex? "))
age = int(input("What is your age? "))
height = int(input("What is your height? "))
weight = int(input("What is your weight? "))
inputtedValue = int(input("Do you smoke? Input 1 for true or 0 for false: "))

if inputtedValue == 1:
    doesSmoke = True # changes boolean based on value

else :
    doesSmoke = False

#we choose which groups of info we want
#separate into smaller groups

if sex == "male" or sex == "Male":
    #arrayAge = averageHeartRate, averageHeartRhythm, averageHeartStrength
    sexMF = 1
    m18To25 = 63.5
    m26To35 = 63.5
    m36To45 = 64.5
    m46To55 = 65.5
    m56To65 = 64.5
    m65Above = 63.5
    

elif sex == "female" or sex == "Female":
    sexMF = 0
    f18To25 = 67.5
    f26To35 = 66.5
    f36To45 = 67.0
    f46To55 = 67.5
    f56To65 = 67.5
    f65Above = 66.5

#men
    #average heartrate
    #average rhythm
    #average strength(amplitude)

#woman
    #average heartrate
    #average rhythm
    #average strength(amplitude)


#what we want to do with the patient ECG data SOMEHOW IMPORT FROM GOOGLE SHEETS?
#put in 2d array
patientECGSecond =  [0,
10,
20,
30,
40,
50,
60,
70,
80,
90,
100,
110,
120,
130,
140,
150,
160,
170,
180,
190,
200,
210,
220,
230,
240,
250,
260,
270,
280,
290,
300,
310,
320,
330,
340,
350,
360,
370,
380,
390,
400,
410,
420,
430,
440,
450,
460,
470,
480,
490,
500,
510,
520,
530,
540,
550,
560,
570,
580,
590,
600,
610,
620,
630,
640,
650,
660,
670,
680,
690,
700,
710,
720,
730,
740,
750,
760,
770,
780,
790,
800,
810,
820,
830,
840,
850,
860,
870,
880,
890,
900,
910,
920,
930,
940,
950,
960,
970,
980,
990
]

patientECGVoltage = [0.2,
0.8,
1.2,
1.5,
1.4,
0.8,
0.2,
-0.4,
-0.8,
-1.2,
-1,
-0.5,
0,
0.5,
1,
1.3,
1.4,
1.2,
0.8,
0.2,
-0.4,
-0.8,
-1,
-0.8,
-0.4,
0,
0.5,
1,
1.2,
1.4,
1.3,
1,
0.5,
0,
-0.4,
-0.8,
-1,
-0.8,
-0.4,
0,
0.5,
1,
1.2,
1.4,
1.3,
1,
0.5,
0,
-0.4,
-0.8,
-1,
-0.8,
-0.4,
0,
0.5,
1,
1.2,
1.4,
1.3,
1,
0.5,
0,
-0.4,
-0.8,
-1,
-0.8,
-0.4,
0,
0.5,
1,
1.2,
1.4,
1.3,
1,
0.5,
0,
-0.4,
-0.8,
-1,
-0.8,
-0.4,
0,
0.5,
1,
1.2,
1.4,
1.3,
1,
0.5,
0,
-0.4,
-0.8,
-1,
-0.8,
-0.4,
0,
0.5,
1,
1.2,
1.4,
]

#peaks = np.argsort(patientECGVoltage)[-4:][::-1]

#print("Indexes of the top 4 maximum values:", )

def findPeaksVoltage(patientECGVoltage):
    peaks = []
    for i in range(1, len(patientECGVoltage) - 1):
        if patientECGVoltage[i] > patientECGVoltage[i - 1] and patientECGVoltage[i] > patientECGVoltage[i + 1]:
            peaks.append(i)
    return peaks

def findPeaksSeconds(patientECGSecond, peaks):
    peaksSeconds = []
    for peak in peaks:
        peaksSeconds.append(patientECGSecond[peak])
    return peaksSeconds

def differences(peaksSeconds):
    diffSeconds = []
    for i in range(1, len(peaksSeconds) - 1):
        diffSeconds.append(peaksSeconds[i] - peaksSeconds[i - 1]) 
    return diffSeconds

def averageDifferences(diffSeconds):
    sum = 0.0
    count = 0.0
    average = 0.0
    for i in range(0, len(diffSeconds) - 1):
        count = count + 1
        sum = sum + diffSeconds[i]
    average = sum / count
    return average

def patientHeartRate(average):
    average = 60000.0/average
    return average

peaks = findPeaksVoltage(patientECGVoltage)
#print(peaks)
peaksSeconds = findPeaksSeconds(patientECGSecond, peaks)
#print(peaksSeconds)
diffSeconds = differences(peaksSeconds)
#print(diffSeconds)
average = averageDifferences(diffSeconds)
#print(average)
heartRate = patientHeartRate(average)
#print("heartrate is", round(heartRate, 2), "bpm")

#Your target heart rate is 50 to 85 percent of your maximum heart rate. It is the level at which your heart is beating with moderate to high intensity. To determine your maximum heart rate, take 220 and subtract your age.

#check each element in 2d array. 
#compare elements in 2d array with standard #compare inputted value with average of data set
    #average heartrate
    #average rhythm
    #average strength(amplitude)

differenceLevel = 0.0
heartRateStatus = str()

if sexMF == 1:
    if age >= 18 and age <= 25:
        differenceLevel = abs(heartRate - m18To25)
        if differenceLevel >= 82 and differenceLevel <= 100:
            heartRateStatus = "Slightly Above Average"
        elif differenceLevel >= 101 and differenceLevel<= 150: 
            heartRateStatus = "High"
        elif differenceLevel >= 151:
            heartRateStatus = "Extremely High"
        elif differenceLevel <= 81:
            heartRateStatus = "Below Average"
    elif age >= 26 and age <= 35:
        differenceLevel = abs(heartRate - m26To35)
        if differenceLevel >= 82 and differenceLevel <= 100:
            heartRateStatus = "Slightly Above Average"
        elif differenceLevel >= 101 and differenceLevel<= 150: 
            heartRateStatus = "High"
        elif differenceLevel >= 151:
            heartRateStatus = "Extremely High"
        elif differenceLevel <= 81:
            heartRateStatus = "Below Average"
    elif age >= 36 and age <= 45:
        differenceLevel = abs(heartRate - m36To45)
        if differenceLevel >= 83 and differenceLevel <= 100:
            heartRateStatus = "Slightly Above Average"
        elif differenceLevel >= 101 and differenceLevel<= 150: 
            heartRateStatus = "High"
        elif differenceLevel >= 151:
            heartRateStatus = "Extremely High"
        elif differenceLevel <= 82:
            heartRateStatus = "Below Average"
    elif age >= 46 and age <= 55:
        differenceLevel = abs(heartRate - m46To55)
        if differenceLevel >= 84 and differenceLevel <= 100:
            heartRateStatus = "Slightly Above Average"
        elif differenceLevel >= 101 and differenceLevel<= 150: 
            heartRateStatus = "High"
        elif differenceLevel >= 151:
            heartRateStatus = "Extremely High"
        elif differenceLevel <= 83:
            heartRateStatus = "Below Average"
    elif age >= 56 and age <= 65:
        differenceLevel = abs(heartRate - m56To65)
        if differenceLevel >= 82 and differenceLevel <= 100:
            heartRateStatus = "Slightly Above Average"
        elif differenceLevel >= 101 and differenceLevel<= 150: 
            heartRateStatus = "High"
        elif differenceLevel >= 151:
            heartRateStatus = "Extremely High"
        elif differenceLevel <= 81:
            heartRateStatus = "Below Average"
    elif age >= 65:
        differenceLevel = abs(heartRate - m65Above)
        if differenceLevel >= 80 and differenceLevel <= 100:
            heartRateStatus = "Slightly Above Average"
        elif differenceLevel >= 101 and differenceLevel<= 150: 
            heartRateStatus = "High"
        elif differenceLevel >= 151:
            heartRateStatus = "Extremely High"
        elif differenceLevel <= 79:
            heartRateStatus = "Below Average"

if sexMF == 0:
    if age >= 18 and age <= 25:
        differenceLevel = abs(heartRate - f18To25)
        if differenceLevel >= 85 and differenceLevel <= 100:
            heartRateStatus = "Slightly Above Average"
        elif differenceLevel >= 101 and differenceLevel<= 150: 
            heartRateStatus = "High"
        elif differenceLevel >= 151:
            heartRateStatus = "Extremely High"
        elif differenceLevel <= 84:
            heartRateStatus = "Below Average"
    elif age >= 26 and age <= 35:
        differenceLevel = abs(heartRate - f26To35)
        if differenceLevel >= 82 and differenceLevel <= 100:
            heartRateStatus = "Slightly Above Average"
        elif differenceLevel >= 101 and differenceLevel<= 150: 
            heartRateStatus = "High"
        elif differenceLevel >= 151:
            heartRateStatus = "Extremely High"
        elif differenceLevel <= 81:
            heartRateStatus = "Below Average"
    elif age >= 36 and age <= 45:
        differenceLevel = abs(heartRate - f36To45)
        if differenceLevel >= 83 and differenceLevel <= 100:
            heartRateStatus = "Slightly Above Average"
        elif differenceLevel >= 101 and differenceLevel<= 150: 
            heartRateStatus = "High"
        elif differenceLevel >= 151:
            heartRateStatus = "Extremely High"
        elif differenceLevel <= 82:
            heartRateStatus = "Below Average"
    elif age >= 46 and age <= 55:
        differenceLevel = abs(heartRate - f46To55)
        if differenceLevel >= 84 and differenceLevel <= 100:
            heartRateStatus = "Slightly Above Average"
        elif differenceLevel >= 101 and differenceLevel<= 150: 
            heartRateStatus = "High"
        elif differenceLevel >= 151:
            heartRateStatus = "Extremely High"
        elif differenceLevel <= 83:
            heartRateStatus = "Below Average"
    elif age >= 56 and age <= 65:
        differenceLevel = abs(heartRate - f56To65)
        if differenceLevel >= 84 and differenceLevel <= 100:
            heartRateStatus = "Slightly Above Average"
        elif differenceLevel >= 101 and differenceLevel<= 150: 
            heartRateStatus = "High"
        elif differenceLevel >= 151:
            heartRateStatus = "Extremely High"
        elif differenceLevel <= 83:
            heartRateStatus = "Below Average"
    elif age >= 65:
        differenceLevel = abs(heartRate - f65Above)
        if differenceLevel >= 84 and differenceLevel <= 100:
            heartRateStatus = "Slightly Above Average"
        elif differenceLevel >= 101 and differenceLevel<= 150: 
            heartRateStatus = "High"
        elif differenceLevel >= 151:
            heartRateStatus = "Extremely High"
        elif differenceLevel <= 83:
            heartRateStatus = "Below Average"

#Boolean decleration for heart result
severe = False
moderate = False
low = False


if doesSmoke == True:
    if heartRateStatus == "Extremely High":
        print("Warning! Heart Attack Imminent!")
        severe = True
    if heartRateStatus == "High":
        print("Warning! High Risk of Heart Attack!")
        moderate = True
    if heartRateStatus == "Below Average":
        print("Low Risk, Below Average Heart Rate")
        low = True

if doesSmoke == False:
    if heartRateStatus == "Extremely High":
        print("Warning! Heart Attack Imminent!")
        severe = True
    if heartRateStatus == "High":
        print("Warning! High Risk of Heart Attack!")
        moderate = True
    if heartRateStatus == "Below Average":
        print("Low Risk, Below Average Heart Rate")
        low = True

#define what range they lie in (extremely high, high, slightly above average, slightly below average, low, extremely low) using Z score from stats
    #average heartrate (GIVE SCORE)
    #average rhythm (GIVE SCORE)
    #average strength(amplitude) (GIVE SCORE)


#sum up score
#put score in range (no risk, high risk, extreme risk), also check if user has specific conditions ex. smoking, weight, etc said in beginning.
#(ex. if male, + 1. if smoking + 5)
#print something depending on each
























#1. find the outliers (amplitude wise) (compared to standard according their inputed weight, height, age, etc)
#2. identify irregular heartbeats (compared to the standard)
#3. find average rate (compare it to the standard)

#heartrate
#heartrhythm
#heartstrength

#for select heart issues:
#Heart Attack (identify, warn)
#Arrhythmias (identify, warn)
#Weak heartbeat (sign of other issues needing more examination to diagnose)
#Strong hearbeat (sign of other issues needing more examination to diagnose)
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        img1 = ImageTk.PhotoImage(Image.open("heartrate.png"))
        img2= ImageTk.PhotoImage(Image.open("heartrate.png"))

        # configure window
        self.title("HacktheHeart.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure((1), weight=1)
        self.grid_columnconfigure((2), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Heart Coach", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.user_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.user_1_event)
        self.user_1.grid(row=1, column=0, padx=20, pady=10)
        self.user_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.user_2_event)
        self.user_2.grid(row=2, column=0, padx=20, pady=10)
        self.user_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.user_3_event)
        self.user_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create heart entry and button frame (bottom frame)
        self.bottombar_frame = customtkinter.CTkFrame(self)
        self.bottombar_frame.grid(row=3,column=1, padx=(40,8), pady=(20,20), sticky="nsew")
        self.bottombar_frame.grid_columnconfigure(0, weight=1)
        #self.entry = customtkinter.CTkEntry(self.bottombar_frame, placeholder_text="Enter Score Here")

        ## create function which enters in user input when button is pressed
        #self.entry.grid(row=0, column=0, columnspan=1, padx=(50, 0), pady=(20, 20), sticky="nsew")
        self.score = customtkinter.CTkButton(master = self.bottombar_frame, fg_color="transparent", border_width=2, text= "Analyze", text_color=("gray10", "#DCE4EE"), command=self.analyze_event)
        self.score.grid(row=0, column=0, padx=(200, 200), pady=(20, 20), sticky="nsew")
        self.score.grid_columnconfigure(0, weight=0)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create infromation tab
        self.infromationtab = customtkinter.CTkTabview(self, width=250)
        self.infromationtab.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.infromationtab.add("Contact Page")
        self.infromationtab.add("Personal Info")
        self.infromationtab.tab("Contact Page").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.infromationtab.tab("Personal Info").grid_columnconfigure(0, weight=1)
        self.usertext = customtkinter.CTkTextbox(self.infromationtab.tab("Personal Info"), width=240, height= 150)
        self.usertext.insert("0.0", "User/Doctor Input Data Here\n\n")
        self.usertext.grid(row=0, column=1, padx=(20), pady=(20, 0), sticky="nsew")

        self.caller1 = customtkinter.CTkOptionMenu(self.infromationtab.tab("Contact Page"), dynamic_resizing=False,
                                                        values=["Dad", "Mom", "Grandpa Joe", "Doctor Sam"])
        self.caller1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.call = customtkinter.CTkButton(master = self.infromationtab.tab("Contact Page"), fg_color="transparent", border_width=2, text= "Call", text_color=("gray10", "#DCE4EE"), command=self.call_event)
        self.call.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.call_input_button = customtkinter.CTkButton(self.infromationtab.tab("Contact Page"), text="Open Emergency Dial",
                                                           command=self.open_input_dialog_event, state="disabled")
        self.call_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))

        # create frame for graphs
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)

        #create frame for conditions
        self.analysis_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.analysis_frame.grid(row=0, column=1, padx= (20,0), pady=(0, 0), sticky="nsew")
        self.analysis_frame.grid_columnconfigure(0, weight=1)
        self.analysis_frame.grid_rowconfigure(4, weight=1)

        #create the seperate frame inside for each individual condition
        self.heartcondition_frame = customtkinter.CTkScrollableFrame(self.analysis_frame, label_text="Heart Condition")
        self.heartcondition_frame.grid(row=1, column=0, rowspan = 1, padx=(20,0), pady=(20,0), sticky="nsew")
   

        self.analysis_frame.grid_columnconfigure(0, weight=1)
        self.heartcondition = customtkinter.CTkLabel(self.heartcondition_frame, text="Your heart condition analysis will show up here.", wraplength=260)
        self.heartcondition.grid(row = 0, column = 0, padx = (5,5), pady=(5,0))



        #self.analysis_frame.grid_rowconfigure(4, weight=1)
        self.pacecondition_frame = customtkinter.CTkScrollableFrame(self.analysis_frame, label_text="Pacemaker Condition")
        self.pacecondition_frame.grid(row=1, column=1, rowspan = 1, padx=(20,10),pady=(20,0), sticky="nsew")
        self.analysis_frame.grid_columnconfigure(1, weight=1)
        self.pacecondition = customtkinter.CTkLabel(self.pacecondition_frame, text="Your pacemaker condition analysis will show up here.", wraplength=260)
        self.pacecondition.grid(row = 0, column = 0, padx = (5,5), pady=(5,0))
        




        ##
        #self.progressbar_1 = customtkinter.CTkProgressBar(self.bottombar_frame)
        #self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        ##

        #self.progressbar_2 = customtkinter.CTkProgressBar(self.bottombar_frame)
        #self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        #self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        #self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        #self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        #self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        #self.progressbar_3 = customtkinter.CTkProgressBar(self.bottombar_frame, orientation="vertical")
        #self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Diet Check-List")
        self.scrollable_frame.grid(row=1, column=2, rowspan = 3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_checkbox = []
        for i in range(9):
            checkbox = customtkinter.CTkCheckBox(master=self.scrollable_frame, text=f"Yummy Food or Drink {i+1}")
            checkbox.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_checkbox.append(checkbox)

        # create checkbox and switch frame
        #self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        #self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        #self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        #self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        #self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        #self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        #self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        #self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

        #setting user/data inputs
        

        # set default values
        self.user_1.configure(text="User 1")
        self.user_2.configure(text="User 2")
        self.user_2.configure(state="disabled", fg_color="transparent")
        self.user_3.configure(text="User 3")
        self.user_3.configure(state="disabled", fg_color="transparent")
        #self.checkbox_3.configure(state="disabled") ###DISABLE STUFF HERE state="disabled"


        #self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        #self.slider_1.configure(command=self.progressbar_2.set)
        #self.slider_2.configure(command=self.progressbar_3.set)
        #self.progressbar_1.configure(mode="indeterminnate")
        #self.progressbar_1.start()
        self.textbox.insert("0.0", "Condition\n\n")
        
        #Heart Stats
        self.heartinfo = customtkinter.CTkTabview(self.slider_progressbar_frame, width=250, height = 150)
        self.heartinfo.grid(row=0, column=0, padx=(20, 10), pady=(0, 10), sticky="nsew")
        self.heartinfo.add("Heart Rate")
        self.heartinfo.add("ECG")
        self.heartinfo.tab("Heart Rate").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.heartinfo.tab("ECG").grid_columnconfigure(0, weight=1)
        
        self.heartGraph = tk.Label(self.heartinfo.tab("Heart Rate"), image = img1)
        self.heartGraph.grid(row=0, column=0, padx=(20,0), pady=(20,0))
        self.ecgGraph = tk.Label(self.heartinfo.tab("ECG"), image = img2)
        self.ecgGraph.grid(row=0, column=0, padx=(20,0), pady=(20,0))
        self.label_tab_2 = customtkinter.CTkLabel(self.heartinfo.tab("Heart Rate"), text="Heart Graph")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        self.label_tab_3 = customtkinter.CTkLabel(self.heartinfo.tab("ECG"), text="ECG Graph")
        self.label_tab_3.grid(row=0, column=0, padx=20, pady=20)
        
        #Heart Analysis
        #self.analysis = customtkinter.CTkTabview(self.analysis_frame, width=250)
        #self.analysis.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="nsew")
        #self.analysis.add("Heart Condition")
        #self.analysis.add("Pace Maker Condition")
        #self.analysis.tab("Heart Condition").grid_columnconfigure(0, weight=1)  
        #self.analysis.tab("Pace Maker Condition").grid_columnconfigure(0, weight=1)
        #self.label_tab_2 = customtkinter.CTkLabel(self.analysis.tab("Heart Condition"), text="Heart condition/status goes here")
        #self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        #self.label_tab_3 = customtkinter.CTkLabel(self.analysis.tab("Pace Maker Condition"), text="Pace Maker Batttery goes here")
        #self.label_tab_3.grid(row=0, column=0, padx=20, pady=20)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog( text="Call Emergency Number:", title="Emergency Dial")
        print("Calling", dialog.get_input())
        messagebox.showinfo("Dialing", "Emergency contact is being called. Stay Safe.")
    
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def user_1_event(self): ###THIS HERE SHOULD CHANGE THE User
        print("user1_button click")
    
    def user_2_event(self): ###THIS HERE SHOULD CHANGE THE
        print("user2_button click")

    def user_3_event(self): ###THIS HERE SHOULD CHANGE THE
        print("user3_button click")

    def call_event(self):
        selected_option = self.caller1.get()
        print("Calling", selected_option )

    
    def analyze_event(self):
        try:
            if severe == True:
                #print("The number is greater than 10.")
                self.call_input_button.configure(state="normal")
                self.heartcondition.configure(text="Your heart conditon risk is severe. \n\nContact your doctor immediately. Call emergency line immediately if symptom worsen!\n\nSymptoms to look out for: *personalized list*\n\nSuggested Supplements: *based on previous history* ")
                #CREATE WARNING WINDOW DIALOG
                messagebox.showinfo("WARNING", "Your heart condition risk is severe. Do NOT participate in excessive physical activity.")
                
            elif moderate == True:
                self.call_input_button.configure(state="normal")
                #print("The number is between 5 to 10.")
                self.heartcondition.configure(text="Your heart conditon risk is moderate.\n Consider seeing a doctor if conditions worsen.\n\nSymptoms to look out for: *personalized list*\n Suggested Supplements: *based on previous history* ")
                #CREATE WARNING WINDOW DIALOG
                messagebox.showinfo("WARNING", "Your heart condition risk is moderate. Be cautious in participating in physical activity.")
                

                
            elif low == True:
                #print("The number is less than 10.")
                self.call_input_button.configure(state="disabled")
                self.heartcondition.configure(text="Your heart conditon risk is low. \n\nSymptoms to look out for: *personalized list*\n\nSuggested Supplements: *based on previous history* ")
                #CREATE WARNING WINDOW DIALOG
                messagebox.showinfo("Your heart condition risk is low.Y You can participate in physical activity with concern.")
        except:
            print("yes")
    
    

if __name__ == "__main__":
    app = App()
    app.mainloop()