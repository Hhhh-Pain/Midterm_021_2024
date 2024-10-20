import matplotlib as plot
import wave as w
import random as rand

# Have the user select each wav file, open it, see an image of the entire audio length of the audio file and listen to said file.abs
# user can determine where is the low pass filter in (M)hz, and simulate that via code & tell user what cap & resistor to use when doing it irl

Redo = 0
wav_files = {}
waveform_hear_audio = 0
resistor = 0
capacitor = 0


def low_pass_filter(Hz, CRN, Value):
    # 2(3.1415926535) or 2*pi to the 10 digits is = 6.283185307

    # Formula is Hz(2pi)(Resistor)(Capacitor) = 1
    # Isolate either Capacitor or Resistor gets you 
    # 1/(Hz(2pi(Resistor or Capacitor))) = Capacitor or Resistor

    # Value is the value of the resistor of the cap or resistor, in farads or ohms
    denom = (Hz)*(6.283185307)*(Value)
    if denom == 0:
        print("Your Hz frequency or your value for your capacitor or resistor cannot be 0")
    if CRN == "C":
        resistor = 1/denom
        capacitor = Value
    elif CRN == 'R':
        capacitor = 1/denom
        resistor = Value
    elif CRN == 'N':
        Value = round(rand.uniform(0,1000))
        Value = Value*10
        capacitor = 1/denom
        resistor = Value
    return capacitor, resistor

def openfile(number):
    wav_files.update({f'{number}': f'w.open("wav/wav_{number}.wav", "rb")'})
    print(wav_files)

# CryoPods_Wav = w.open("wav/1_Cryo_Pods.wav","rb")
# DesertDevotional_Wav = w.open("wav/2_Desert_Devotional.wav","rb")
# ElvenProcession_Wav = w.open("wav/3_Elven_Procession.wav","rb")
# HiddenPassage_Wav = w.open("wav/4_Hidden_Passage.wav","rb")
# LairOfTheWyrm_Wav = w.open("wav/5_Lair_of_the_Wyrm.wav","rb")
# NautiloidEscape_Wav = w.open("wav/6_Nautiloid_Escape.wav","rb")
# RiseOfTheGolem_Wav = w.open("wav/7_Rise_of_the_Golem.wav","rb")
# StagecoachHeist_Wav = w.open("wav/8_Stagecoach_Heist.wav","rb")
# TombGuardians_Wav = w.open("wav/9_Tomb_Guardians.wav","rb")
# Trireme_Wav = w.open("wav/10_Trireme.wav","rb")




while True:
    Redo = int(input("do you want to pick a music to listen to? any integer is yes & 0 is no"))
    if Redo > 0:
        number = int(input("what file do you want to listen to? i only have numbers 0-9"))
        if number in range(9):
            openfile(number)
            # run the audio
        else:
            print("sorry, that isn't within 0-9. opinions denied.")
            wav_files.clear()
            exit()
    if Redo == 0:
        print("ok then, goodbye")
        wav_files.clear()
        break


print("welcome")
print("do you want to see or hear the files? type 1 for yes; 0 for no.")
if waveform_hear_audio > 0:
    #show audio while displaying audio
    print("play audio")


while True:
    audio_test = int(input("what audio do you want to hear? give a number from 0 to 9 to listen to that audio"))
    # play audio
    # show waveform if waveform > 0
    exit = input("are you done? type 'y' for yes, 'n' for no")
    if exit == "y":
        break
    if exit == "n":
        print(end='')
        
Hertz = int(input("what hz value do you want your low pass filter to be on?"))
while True:
    Cap_Res_None = input("do you have a capacitor or resistor that you have on hand to use for the circuit? type 'C' for Capacitor, 'R' for resistor, or 'N' for none.")
    
    if Cap_Res_None == 'C':
        Cap_Res_Value = float(input("What value is the capacitor? Please input the numerical value of your capacitor in Farads."))
        break
    elif Cap_Res_None == 'R':
        Cap_Res_Value = float(input("What value is the resistor? Please input the numerical value of your resistor in Ohms."))
        break
    elif Cap_Res_None == 'N':
        print("If you have none, I will pick a random resistor value from 1 to 10000 that are a multiple of 10 to determinne the best capacitor value needed for your determined hertz")
        Cap_Res_Value = 1
        break
    else:
        print("please type 'C', 'R', or 'N' to carry on.")    
        
capacitor, resistor = low_pass_filter(Hertz, Cap_Res_None, Cap_Res_Value)
print(f'Your low pass filter needs a {resistor} ohm resistor and a {capacitor} farad capacitor')

filter = input('Do you want to use the low pass filter and go through the provided audio files?')
if filter == 'y':
    # go through filter, output audio, show waveform if waveform > 0
    # have the same while loop as before, but have it change hz values again (or keep old) when going to next audio
    pass
if filter == 'n':
    exit()


# def load_wav_files():
#     wav_files = {} 
#     for i in range(10):
#         file_name = f'wav_{i}.wav'
#         wav_files[file_name] = f'w.open{file_name}, "rb")'
#     return wav_files


# load_wav_files()

    # with w.open("wav/1_Cryo_Pods.wav", 'rb') as wav_01: 
    #     print(wav_01)
        
    #     # params = wav_01.getparams() 
    #     # frames = wav_01.readframes(params.nframes)
        
    #     # print(len(frames))
