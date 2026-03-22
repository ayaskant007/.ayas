# .ayas Image Studio

.ayas Image Studio is a custom desktop application built in Python that introduces a brand new, proprietary image file format: **`.ayas`**. 

This app acts as both a **Converter** and a **Viewer**. It takes standard images (JPG, PNG), applies an automated, high-quality comic-book stylization, and encodes them into the exclusive `.ayas` binary format. It also features a built-in viewer to render `.ayas` files back to the screen.

## Features

* **Custom File Extension (.ayas):** Uses a unique binary magic header (`AYAS_FORMAT_2026`) to ensure file authenticity. Standard image viewers cannot read these files.
* **Comic Stylization Engine:** Leverages OpenCV's bilateral filtering and adaptive thresholding to smooth colors and preserve high-contrast ink lines, giving photos a hand-drawn comic look.
* **Modern GUI:** Built with `Tkinter`, featuring a sleek dark-mode sidebar navigation system and stacked page frames.
* **Standalone Viewer:** Includes an integrated canvas viewer that decodes the custom binary stream and renders the `.ayas` file using Pillow.

## Tech Stack

* **Python 3.x**
* **OpenCV (`cv2`)**: For advanced image processing and comic stylization.
* **NumPy**: For fast matrix/array operations on image data.
* **Pillow (`PIL`)**: To bridge the gap between OpenCV image matrices and the Tkinter UI.
* **Tkinter**: For the graphical user interface.

## Installation & Setup

1. **Clone or Download the Repository**
2. **Install the Required Libraries:**
   Open your terminal or command prompt and run:
   ```bash
   pip install opencv-python numpy Pillow