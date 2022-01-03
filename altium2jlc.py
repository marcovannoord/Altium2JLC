# img_viewer.py

import PySimpleGUI as sg
import os.path
import csv
from itertools import islice
# First the window layout in 2 columns

file_example_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FILE-"),
        sg.FileBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-EXAMPLE_LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_example_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Altium 2 JLCPCB Pick&Place converter", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # file name was filled in
    if event == "-FILE-":
        file = values["-FILE-"]
        example_list = []
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
                for row in csvreader:
                    print(row['Designator'], row['Layer'])
                    example_list.append(row['Designator'])
        except Exception as e:
            example_list = []
            print(e)

        window["-EXAMPLE_LIST-"].update(example_list)
    elif event == "-EXAMPLE_LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-EXAMPLE_LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)

        except:
            pass

window.close()