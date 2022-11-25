# focusED-Glasses
kerasmodel2.h5 contains the actual model
  It can be replaced with any teachable machine keras model, just make sure it has the same name
  Currently the model is trained on a kaggle database of images of cell phones to determine what a phone looks like
tmmodel.py (teachable machine model) contains the python code for the model
  more info is written in comments within the code
lablels.txt contains the labels for the two classes inside kerasmodel.h5
  This isn't really being used in the code right now, but the labels are being stored in it, so if you need them they're there
