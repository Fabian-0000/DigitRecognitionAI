# DigitRecognitionAI

## Dependencies
To install the required packages, run ```pip install -r requirements.txt```. It includes Pillow, matplotlib, numpy and tensorflow. Newer versions than listed in the file may work, but there is no guarantee.  
The project was tested with Python 3.10.7, though every newer version supporting all the libraries should work. 

## Run the Application
Simply run ```main.py``` with a supported version of Python.

## Structure
### File Structure:
- ```train/``` contains all the training data in its subdirectories ```train/0/```, ```train/1/```, ..., aswell as ```train.py```, which trains the AI and creates the file

- ```main.py``` and ```ai.py``` are the main code files used by the project

- ```digit_model.keras``` contains the AI model

### Code Structure:
The ```main.py``` contains a GUI class, which calls the AI in ```ai.py```. ```train.py``` is ran seperatly to pregenerate the AI model.

#
<br>

![Funny Gif](https://media1.tenor.com/m/S2wo3JKirgAAAAAd/know-what-else-is-massive-massive.gif)
![Funny Gif](https://media.tenor.com/A-ozELwp694AAAAM/thumbs-thumbs-up-kid.gif)
![Funny Gif](https://media1.tenor.com/m/WSnMZt-dXKUAAAAd/programming-programando.gif)