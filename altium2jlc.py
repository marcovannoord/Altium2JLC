# img_viewer.py

import PySimpleGUI as sg
import os.path
import csv
from itertools import islice
from collections import OrderedDict
# First the window layout in 2 columns

file_example_column = [
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-IMPORT-PREVIEW-"
        )
    ]
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-EXPORT_PREVIEW-"
        )]
]

# ----- Full layout -----
layout = [
    [sg.Text("Select an altium Pick&Place file. On the left you see the file, on the right you see the result, \nthat has been written to the same folder as 'pos_jlcpcb.csv")],
    [
        sg.Text("Altium pick and place file"),
        sg.In(size=(25, 1), enable_events=True, key="-FILE-"),
        sg.FileBrowse(file_types=(("CSV files", "*.csv"),)),
    ],
    [
        sg.Column(file_example_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Altium 2 JLCPCB Pick&Place converter", layout)

# desired output order
order = ['Designator', 'Center-X(mm)', 'Center-Y(mm)', 'Layer', 'Rotation']

# define renamed columns via dictionary
renamer = {'Center-Y(mm)': 'Mid Y', 'Center-X(mm)': 'Mid X'}
columns_renamed = [renamer.get(x, x) for x in order]

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # file name was filled in
    if event == "-FILE-":
        file = values["-FILE-"]
        example_list = []
        output_list = []
        try:
            # Try to find the header of the CSV file
            with open(file, 'r', newline='') as csvfile:
                while True:
                    pos = csvfile.tell()
                    line = csvfile.readline()
                    if line[0] == '"': # if the line starts with a "-character, we assume it is the header
                        csvfile.seek(pos) # go back one line
                        break
                # read the csv file
                csvreader = csv.DictReader(csvfile, delimiter=',' )
                example_list.append('"Designator","Layer","Center-X(mm)","Center-Y(mm)","Rotation"')
               
                outputfile = os.path.join(os.path.dirname(file),"pos_jlcpcb.csv")
                # Now start printing the example output
                with open(outputfile, 'w', newline='') as fout:
                    writer = csv.writer(fout, delimiter=',')
                    # write new header
                    writer.writerow(columns_renamed)
                    output_list.append('{},{},{},{},{}'.format(columns_renamed[0], columns_renamed[1], columns_renamed[2], columns_renamed[3], columns_renamed[4]))

                    # iterate reader and write row
                    for row in csvreader:
                        print(row['Designator'], row['Layer'])
                        example_list.append('{},{},{},{},{}'.format(row["Designator"],row["Layer"],row["Center-X(mm)"],row["Center-Y(mm)"],row["Rotation"]))
                        if row["Layer"] == 'TopLayer':
                            row["Layer"] = 'Top'
                        outrow = [row[k] for k in order]
                        output_list.append('{},{},{},{},{}'.format(outrow[0], outrow[1], outrow[2], outrow[3], outrow[4]))
                        writer.writerow(outrow)


        except Exception as e:
            example_list = []
            output_list = []
            print(e)
        window["-IMPORT-PREVIEW-"].update(example_list)
        window["-EXPORT_PREVIEW-"].update(output_list)
window.close()