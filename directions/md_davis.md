# HOW to use md-davis

MD-Davis is a tool to calculate electrostatics and other properties of proteins. It is a python based tool and can be used in linux and windows.<br>
It's made by Dj-maity, who helped us for this project!
<br>Check out: https://md-davis.readthedocs.io/en/latest/install.html

## Configurations for smooth running

Download the below essentials-

- libboost-dev
- build-essentials
  You can do this by

```bash
sudo apt install libboost-dev build-essentials
```

## Software Configurations

# FOR DELPHI(check the manual from official webiste)

```bash
cd src/interface environment.h
// remove from Parallel_omp
make all.   # this is to do in Release_omp
```

> > delhphicpp_omp_release is made in release_omp

## Conda setup

Before this, you musy have conda downloaded.

```bash
conda activate md-davis
git clone https://github.com/djmaity/md-davis.git
pip install ./
python setup.py install
```

## MSMS

For msms

1. download msms
2. put it in your directory
3. extract
4. (just info) important file is msms.x86_64Linux2.2.6.1, which will be used

## FOR calculation of values.

You have to be inside the file which contains the pdb files, which may or may not be morphs.<br>
Inside the folder with ONLY morph files use this-

```bash
md-davis electrostatics --surface --center -m /home/djmaity/programs/msms/msms.x86_64Linux2.2.6.1 -d /home/djmaity/programs/delphicpp_omp_release -g 251 -o ./ *.pdb
```

OR (for you in linux machine)

```bash
md-davis electrostatics --surface --center -m /home/admin/AnirudhGupta/iGEM/msms/msms.x86_64Linux2.2.6.1 -d /home/admin/AnirudhGupta/iGEM/Delphicpp_v8.5.0_Linux/Release_omp/delphicpp_omp_release -g 251 -o ./ *.pdb
```

### Note:

- -m is the path to msms
- -d is the path to delphicpp
- -g is the grid size (251 felt ok of 7y6i)
- -o is the output directory
- \*.pdb is the pdb files in the directory

To get non surface values, remove --surface. But you may not get all the files as you obtain with surface. So make sure what you are doing is fine.

## CONDITIONS FOR MORPHS

when creating morphs, we should have center and orgin aligned morphs. save morphs with 0(some option)
Also, Make sure the text files of morphs has Hydrogen atoms, for that you need Chimera(pymol does it badly).

## GUI EXECTUTION

```bash
md-davis-gui.exe
# or
md-davis-gui
```

## TO GET FIELD LINES MOVING AS MORPH

```bash
md-davis electrodynamics --ss_color --surface --name Human_NCC directory_path # directory path should contain the cube files mainly
```

## For running ANALYSIS.ipynb

```bash
conda install jupyterlab
jupyter notebook
conda install plotly pandas
pip install biopandas
```

(check the kernel of your notebook)
