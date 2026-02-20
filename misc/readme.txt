The notebooks use the following python3 libraries
- numpy
- sympy
- matplotlib

### Homemade Python Skript um Website zu erzeugen
The generateHTML.py skript uses
- bs4
- jupyter_contrib_nbextensions
- "notebook < 7" (if the wrong version of notebook is installed, you get weird missing module alerts)
all can be installed via "pip install ..."

### Schönere Variante mit JupyterBook

- pip install jupyter-book
- pip install ghp-import


Migration von altem JupyterBook mit
jupyter book

Im Ordner EPROG_2025:
- Die HTML Seite erzeugen mit
jupyter-book build --html

- Auf Github publizieren mit 
ghp-import -n -p -f _build/html


### Presentation in der Vorlesung
For presenting the notebooks as slides, install "pip install rise"
- Slides must be specified in the notebooks (ctrl+shift+p -> "switch slide type" in VSCode)
- To allow scrolling and writing on the slides, add
"rise": {
   "enable_chalkboard": true,
   "scroll": true
  }
  to each notebooks metadata
