# USRC's Drone Racing Competition Simulator

Welcome to USRC's DRC simulator! Here, you can:
- Practice your Python coding skills
- Learn Computer Vision
- Create a self-driving car.

If you're a developer looking to improve this repository, please look at `developers.md` in this same directory.

## Getting started
To get started with the simulator, you need to do some things:
1. Have `python` (python 3, to be precise) installed. For installation instructions, go to [Python's download site](https://www.python.org/downloads/).
2. Install all the dependencies below:
```
pip3 install opencv-python
pip3 install websockets
````
3. Copy our repository to a safe place, using `git clone https://github.com/usydroboticsclub/DRCSimulator.git`.
4. That's it! You're ready to go.
## Running the simulator
1. Open a terminal at the directory and type in `python3 simulatorServer.py`.
2. In a web browser, go to `http://localhost:8000`. You should see a car floating in mid air. (That's normal. Cars do this all the time.)
3. In a separate terminal, run `python3 sampleCar.py`. You should see the following things happen:
    - The car in your browser window starts moving in a circle.
    - A window pops up, showing the car's point of view.
4. Of the two windows in the browser, you can click and drag the top one to change your view into a birds-eye view.

## Coding your own car
1. Copy `sampleCar.py` into a safe place.
2. Open `sampleCar (copy).py` in ~~Visual Studio Code~~ your preferred IDE / text editor.
3. Read, edit, run when ready. And show us what you can do! Send videos, emails and code to [usydroboticsclub@gmail.com](mailto:usydroboticsclub@gmail.com). 

### A few more pointers
- You can find USYD's successful 2019 entry here: https://github.com/clucini/SelfZoomingCar. It's not particularly well documented, but there may be some lessons to be learnt in terms of modular architecture. (May.)

### Some caveats
This simulator is not designed to be competition-grade. You can mess around with the parameters a lot; you can make the car very very fast or make it fly by editing the source code as you want. So, um, enjoy? Just don't push it to prod.

Have fun!