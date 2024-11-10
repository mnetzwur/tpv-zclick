# tpv-zclick
Use TP Virtual/IndieVelo with Zwift Click on macOS

The purpose of this script is to use the QZ App on MacOS to intercept zwift click events and then send keypresses to IndieVelo/TrainingPeaks Virtual to change the virtual gear. The advantage over using the QZ App directly is that the shifting is implemented within TrainingPeaks Virtual and power will come directly from your trainer/powermeter rather than the QZ App, which should not violate the performance verification of IndieVelo races. 

I am not a software developer and the below is an ugly hack. It comes with zero warranty. USE AT YOUR OWN RISK.

## Installation
1. Install the QZ App from the macOS appstore.
2. Install the Trainingpeaks Virtual App from the TrainingPeaks Website[1]. 
3. Before you run this script, run the QZ app (qdomyoszwift) at least once and enable the Zwift Click/Zwift Play Driver. Click on the menu in the top left corner, then Accessories->Zwift Devices Options, then enable "Zwift Click" or "Zwift Play" as well as "Buttons Debouncing." **Note: touchpad scrolling doesn't work in this app on macos, you have to click and drag to scroll.**

<img width="513" alt="Screenshot 2024-11-10 at 3 19 34 PM" src="https://github.com/user-attachments/assets/7e004d74-f3a2-461c-ac12-8c4613b2ecd6">

3. Quit the app.
4. Now download the TPVirtual-Click.py from this repository and save it to your Downloads folder.
5. WAKE UP the Zwift Click BEFORE you run this script by pressing one of the buttons until the blue light blinks.
6. Open the Terminal and type "python TPVirtual-Click.py" and wait, the script should launch TP Virtual and the QZ App if everything works as expected. Once you ride in the app, pressing the click's up and down buttons should change the virtual gears on TP.

Notes: This assumes that you're not using the QZ app for anything else. This script deletes debug logs of the QZ app when it starts. When the script starts it attempts to find the directory in which QZ app stores it's logfiles. If that doesn't work, you may have to find that directory yourself. It's somewhere in ~/Library/Containers/. 

