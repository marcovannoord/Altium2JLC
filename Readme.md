# Altium Pick and Place file to JLCPCB converter tool
When ordering files at JLCPCB, i usually use an `outjob` in Altium to create all files: Gerber, BOM and Pick&Place.  

However, Altium does not allow us setting the output format for the pick&place csv-file. 
This tool helps by converting to a format that JLCPCB can open. 

## How to use
- Export Pick&Place files from Altium. See below image for the correct output settings
- Open the altium2jlc.exe file.
- Select the .csv file that Altium generated in the first step.
- A new file `pos_jlcpcb.csv` will be generated in the same folder as the original file.