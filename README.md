# Hyperspectral-Image-Classification-System

This repository is a system based on Pytorch, sklearn and PyQt5 

My code for deep learning algorithms references the projects:
[DBDA]（https://github.com/lironui/Double-Branch-Dual-Attention-Mechanism-Network#network）  

On the main interface, compare the results images and GT(Ground Truth) images


## Requirements:
* `numpy >= 1.16.5`
- `torch >= 1.2.0`
* `sklearn >= 0.19.2` 
- `pyqt >= 5.9.2` 


## Usage:
1. You need to download the hyperspectral datasets in mat format at: http://www.ehu.eus/ccwintco/index.php?title=Hyperspectral_Remote_Sensing_Scenes, and move the files to `../datasets` folder.  
2. Taking DBMA framework as an example, you need to run `../界面/gui_main.py`, then you can choose the hyperspectral datasets, the algorithms and the storage path of classification result image in the main interface.  
3. You can click the button named `网络参数设置` in the main interface, and click the button named `开始` to run the system.   

(Remark: This system has many flaws. Currently, in order to save system running time, I saved the trained network and the system would load the trained network if users clicked the button named `开始`. Therefore, this system only can load the trained networks and these networks were saved in the `../界面` flder. If you want to use this system and set new network parameters, you could delete the trained network and call algorithms directly.)

## Results:
### Main interface
![image](https://github.com/hubowen7/hyperspectral-image-classification-system/blob/master/main_interface.png)

### Sub interface
![image](https://github.com/hubowen7/hyperspectral-image-classification-system/blob/master/interface_1.png)
![image](https://github.com/hubowen7/hyperspectral-image-classification-system/blob/master/interface_2.png)





