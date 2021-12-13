# Edible-Mushroom-Classification

![](https://img.shields.io/badge/license-MIT-green)
![](https://img.shields.io/github/repo-size/sowmi06/Edible-Mushroom-Classification)
![](https://img.shields.io/github/issues/sowmi06/Edible-Mushroom-Classification)

<!-- ![](https://miro.medium.com/max/1400/0*BAFtzQvvUQpnzBwy.gif) -->

## Table of contents

1.  [Project Description](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/README.md#project-description)
1.  [Configuration Instructions](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/README.md#configuration-instructions)
    1.  [System Requirements](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/README.md#system-requirements)
    1.  [Tools and Library Requirements](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/README.md#tools-and-library-requirements)
1.  [Installation Instructions](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/README.md#installation-instructions)
1.  [Operating Instructions](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/README.md#operating-instructions)
1.  [Manifesting Directory structure](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/README.md#manifesting-directory-structure)
1.  [Copyrights](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/README.md#copyrights)
1.  [Contact](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/README.md#contact)
1.  [Bugs](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/README.md#bugs)
1.  [Acknowledgement](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/README.md#acknowledgement)
1.  [References](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/README.md#references)





## Project Description
Mushroom is fleshy and edible fruit bodies of several species of fungi members of Basidiomycetes grown in ground surface or substrate of other plants such as straw and wood some of which are edible, but a minority of them are toxic. Every year, a large number of people die from eating poisonous mushrooms. It is useful to identify whether a mushroom is poisonous according to the appearance features of the mushroom. The automatic recognition of mushroom toxicity has important social and application value in effectively preventing food poisoning. An automatic identification can break through the limitation to determine whether it is toxic. 

These mushroom toxicity recognition methods have some limitations, such as low accuracy, unqualified detection of unknown toxins, strict requirements for the experimental environments, sufficient professional knowledge, and complex experimental cycles. To solve these problems, we propose an automatic toxicity identification method based on visual features. Firstly, data is inspected for unbalanced set, followed by preprocessing the dataset by data wrangling(Encoding categorical features, Standardizing the features, Encoding the target variable) to convert the categorical data into numerical data Finally, various classifiers like Logistic Regression, Naive Bayes and Random Forest classifier are applied to check for the accuracies of each classifier and propose the best suitable classifier to recognize the toxicity of mushrooms, even that of some unknown species—according to their appearance features and important social and application value. The implementation result indicates that the Random Forest classifier outperforms.




## Configuration Instructions
The [Project](https://github.com/sowmi06/Edible-Mushroom-Classification.git) requires the following tools and libraries to run the [source code](https://github.com/sowmi06/Driver_Drowsiness_Detection/blob/main/Source_Code/Edible-Mushroom-Classification.py).
### System Requirements 
- [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/install/)
    - Python version 3.6.0 – 3.9.0
    - pip 19.0 or later 
    - Ubuntu 16.04 or later (64-bit)
    - macOS 10.12.6 (Sierra) or later (64-bit)
    - Windows 7 or later (64-bit) 
 
- Python IDE (to run ".py" file)
    - [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows), [Spyder](https://www.psych.mcgill.ca/labs/mogillab/anaconda2/lib/python2.7/site-packages/spyder/doc/installation.html) or [VS code](https://code.visualstudio.com/download)

### Tools and Library Requirements 
    
- [Numpy](https://numpy.org/install/)

  Numpy releases are available as wheel packages for macOS, Windows and Linux on [PyPI](https://pypi.org/project/numpy/). 
  
  Install numpy using pip:
        
        pip install numpy
                
  Install numpy using Conda packages:

        conda install numpy
  
  To check your numpy installation:
   
        python -m pip show numpy # to see which version and where numpy is installed

   

- [Scikit-learn](https://scikit-learn.org/stable/install.html) 
  
  Install scikit-learn using pip:
        
        pip install -U scikit-learn
                
  To check your scikit-learn installation:

        python -m pip show scikit-learn  # to see which version and where scikit-learn is installed
     


- [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)

The easiest way to install pandas is to install it as part of the Anaconda distribution, a cross platform distribution for data analysis and scientific computing.
          
  Install it using Conda packages:

       conda install pandas
  
  Installing from [PyPI](https://pypi.org/project/pandas/) :
      
        pip install pandas
   

## Installation Instructions
To work with the project code
- Clone the [Edible-Mushroom-Classification](https://github.com/sowmi06/Edible-Mushroom-Classification.git) repository into your local machine from this link : https://github.com/sowmi06/Edible-Mushroom-Classification.git

- Follow the same directory structure from the cloned repository. 


## Operating Instructions

The following are the steps to replicate the exact results acquired from the project:

- Satisify all the system and the tool, libraries requirements.
- Clone the [Edible-Mushroom-Classification](https://github.com/sowmi06/Edible-Mushroom-Classification.git) repository into your local machine. 
- Run the [LR_NB.py](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/LR_NB.py) for the Logestic Regression and Naive Bayes results and [Random_Forest.py](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/Random_Forest.py) for the Random forest result.
- Follow the same directory structure from the cloned repository.


## Manifesting Directory structure

The following directory structure is required to replicate exact results acquired from the project:

### Directory layout to repicate results

    .
    ├── .gitignore               
    ├── LICENSE                
    ├── LR_NB.py  
    ├── Preprocessing.py
    ├── README.md
    └── Random_Forest.py




### Directories and Files

[LR_NB.py](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/LR_NB.py) - A ".py" file containing the proposed model implementation of the mushroom classification using Naive Bayes and Logestic Regression Classifier.

[Random_Forest.py](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/Random_Forest.py) - A ".py" file containing the proposed model implementation of the mushroom classification using Random Forest Classifier.

[Preprocessing.py](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/Preprocessing.py) -  A ".py" file containing the preprocessing steps.

[Readme.md](https://github.com/sowmi06/Edible-Mushroom-Classification/blob/main/README.md) - Readme file to execute the project. 



## Copyrights
The project is under the [MIT](LICENSE). Refer [LICENSE](LICENSE) file for more information.

## Contact  
Feel free to drop an [email](mailto:sowmidevaraj06@gmail.com) for any help. 

## Bugs
The code is a finalized and free from bugs.

## Acknowledgement
I would like to thank Dr. Thiago E. A. de Oliveira for guiding throughout research paper. 

## References 
- Anaconda Navigator : https://docs.anaconda.com/anaconda/navigator/install/
- PyCharm IDE Installation : https://www.jetbrains.com/pycharm/download/#section=windows
- Spyder IDE Installation : https://www.psych.mcgill.ca/labs/mogillab/anaconda2/lib/python2.7/site-packages/spyder/doc/installation.html
- VS code IDE Installation: https://code.visualstudio.com/download
- Numpy Installation : https://numpy.org/install/
- Scikit learn Installation : https://scikit-learn.org/stable/install.html
- Pandas Installation: https://pandas.pydata.org/docs/getting_started/install.html
