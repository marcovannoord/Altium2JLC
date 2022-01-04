# Altium Pick and Place file to JLCPCB converter tool
<img width="498" alt="image" src="https://user-images.githubusercontent.com/90630/148036893-3ff3a9f1-e89e-4745-989b-4981c5f5d714.png">

When ordering files at JLCPCB, i usually use an `outjob` in Altium to create all files: Gerber, BOM and Pick&Place.  

However, Altium does not allow us setting the output format for the pick&place csv-file. 
This tool helps by converting to a format that JLCPCB can open. 


## How to use
- Export Pick&Place files from Altium. See below image for the correct output settings
- Open the altium2jlc.exe file.
- Select the .csv file that Altium generated in the first step.
- A new file `pos_jlcpcb.csv` will be generated in the same folder as the original file.

![image](https://user-images.githubusercontent.com/90630/148036842-f918e2a0-b490-400d-a820-dbe7b94059af.png)


# Running from source
- Make sure you have python 3.8+ and pySimpleGui installed by running `pip install pysimplegui`

# Building executable
Run `pip install pysimplegui-exemaker` to install the GUI-maker and use `python -m pysimplegui-exemaker.pysimplegui-exemaker` to create the executable 
