# .ayas Image Studio

.ayas Image Studio is a custom desktop application built in Python using tkinter and ctkinter that introduces my very own image file format: **`.ayas`**. 

The app has a converter and a viewer, the converter converts a normal image file into a .ayas image file and the viewer can be used to view the file.

## Features

* **Custom File Extension (.ayas):** Uses a unique binary magic header (`AYAS_FORMAT_2026`) to ensure that it is a .ayas image file only and NOT a RANDOM AHH image file. Standard image viewers cannot read these files.
* **Comic Style filter:** Utilizes OpenCV's bilateral filtering and adaptive thresholding to give that "comic effect"
* **Modern GUI:** Built with `Tkinter and ctkinter`, featuring a sleek dark-mode sidebar navigation system and stacked page frames, i built using tkinter first but it looked like that i made the app for windows xp so yeah had to use ctkinter.
* **Standalone Viewer:** Includes an integrated canvas viewer that decodes the custom binary stream and renders the `.ayas` file using Pillow so that you can see your comic styled images!!!

## Installation & Setup

1. **Clone or Download the Repository**
2. **Install the Required Libraries:**
   Open your terminal or command prompt and run:
   ```bash
   pip install opencv-python numpy Pillow
