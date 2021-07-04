# YoloDataToShanghaiTech
Convert data from the yolov5 (ultralytics, bounding boxes) dataset format to shanghai tech (density map). The idea is the match the formatting so it can be fed to networks that expect the shanghai data.

# Installing
Requirements are pretty minimal. 

`cd ~/git/YoloDataToShanghaiTech` (or wherever this repo is cloned to)
`python3 -m venv ./venv`
`source venv/bin/activate`
`pip3 install requirements.txt`

# Running the conversion script


# Checking the data
Use the `plotData.py` script to check your annotations. To run this on the shanghai data, copy all the IMG_n.jpg files you want to check, along with their GT_IMG_n.mat files directly into the `dataToPlot` directory (no folders below this). Any annotations found in that folder will be plotted to their matching image and saved to `dataPlotted`. The annotations must start with `GT_` and end in .mat with the exact same matlab struct format as the shanghai ones (it's complicated). Takes no args, but settings are at the top of the script.

`python3 plotData.py`
