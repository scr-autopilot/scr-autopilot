# Setting up SCR-Autopilot step-by-step

1. Navigate to https://python.org/downloads and click `Download Python 3.9.6`
2. Open the downloaded file
3. Check `Add Python 3.9 to PATH`
4. Click `Install Now`
5. Navigate to https://github.com/scr-autopilot/scr-autopilot/releases
6. Scroll down a little bit
7. Under `Assets` click `Source code (zip)`
8. Unzip the file where you want (I will put it on the Desktop)
9. Open the unzipped folder
10. Create a new folder called **`Tesseract-OCR`** in there

![Screenshot](https://i.imgur.com/qzA20hg.png)

11. Navigate to https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.0-alpha.20201127.exe and open the downloaded file

12. Go through the installer as instructed, but change the `Destination Folder` to folder you created in step 10 (mine is `Desktop > scr-autopilot-0.4-beta > Tesseract-OCR`)

13. Navigate to https://autohotkey.com

14. Click `Download` and `Download Current Version`

15. Click `Express Installation` and `Exit`

16. Hit `Win + R`

17. Type `cmd` in there and hit OK

18. Paste this into the command prompt

    ```
    py -m pip install opencv_python requests PyDirectInput ahk Flask numpy pytesseract Pillow pywin32
    ```

    _The command installs required modules for SCR-Autopilot to work._

19. After the installing finishes, you may get a warning message, but you can safely ignore it.

20. Close the command prompt

21. And now to start SCR-Autopilot, go to the `scr-autopilot-0.4-beta` folder (mine is on the Desktop) and run the `main.py` file



##### If you have any problems with SCR-Autopilot feel free to ask on the [Discord server](https://discord.gg/jtQ2R8cxWq)
