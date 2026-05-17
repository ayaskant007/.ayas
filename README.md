# .ayas Image Studio

.ayas Image Studio is a custom-made python desktop app (based on tkinter and ctkinter) which adds my own image file format **`.ayas`**. 

The app has a converter and a viewer, the converter converts a normal image file into a .ayas image file and the viewer can be used to view the file.

## Features

* Custom File Extension (.ayas): Contains a unique binary magic header (AYAS_FORMAT_2026) to make sure that it is a .ayas image file and NOT a RANDOM AHH image file. These files are not readable with standard image viewers.
* Comic Style filter: Applies OpenCV's bilateral filtering and adaptive thresholding for that "comic effect"
* Built using Tkinter and ctkinter, has a sleek dark-mode sidebar navigation system and stacked page frames.i built using tkinter first but it looked like i built the app for windows xp so yeah had to use ctkinter.
* Standalone Viewer: Contains an embedded canvas viewer which can decode the custom binary stream and draw the comic styled images on the canvas using Pillow to view your comic images!

## Installation & Setup

1. **Clone or Download the Repository**
2. **Install the Required Libraries:**
   Open your terminal or command prompt and run:
   ```bash
   pip install -r requirements.txt


## Run

1. Make sure you have the reqd. packages installed.
2. Run the application:

```bash
python writer.py
```

or go to releases and download the .exe file
