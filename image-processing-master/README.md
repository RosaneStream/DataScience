# image_processing

## Description. 
The package image_processing is used to:
	Processing
		- Histogram matching 
		- Structural similarity
		- Resize image
	Utils
		- Read image
		- Save image
		- Plot image
		- Plot result
		- Plot histogram

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install image_processing


```bash
pip install image_processing
```
## Steps

Update requirements.txt
Update setup.py
Update README.md
Update io.py
Update plot.py
Update combination.py
Update transformation.py

Execute upgrade commands
python -m pip install --upgrade pip
python -m pip install --user twine
python -m pip install --user setuptools

Execute distribuition command
python setup.py sdist bdist_wheel

Public package in Pypi test
python -m twine upload --repository-url 
https://test.pypi.org/legacy/ dist/*

Install package in Pypi test
pip install –-index-url https://test.pypi.org/simple/ 
image-processing

Public package in Pypi
python -m twine upload --repository-url 
https://upload.pypi.org/legacy/ dist/*

Install package in Pypi
python -m pip install package_name

## Author
Rosane Ribeiro

## License
[MIT](https://choosealicense.com/licenses/mit/)
