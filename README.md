# Voltage divider calculator

## Instalation

Install from GitHub:
```commandline
pip install --upgrade https://github.com/Zeren/Voltage-divider-calculator/tarball/main
```

Or installation with git clone:
```commandline
git clone https://github.com/Zeren/Voltage-divider-calculator
pip install .\Voltage-divider-calculator\
```

## Usage 

Find voltage divider for 5V input voltage and 1.8V output voltage with combined E24 and E96.
```powershell
divider.exe 5 1.8 -e extend
```
Output:
```text
Closest resistor values for Vin: 5.0V and Vout: 1.8V is
R1: 4.32
R1: 2.43
With error  0.0V,  0.0%
```
Find list of possible combination of voltage divider for 15V input voltage and 1.8V output voltage with combined E24 and E96. 
```powershell
divider_list.exe 15 1.8 -e extend
```
Output:
```text
Closest resistor values for Vin: 15.0V and Vout: 1.8V are
R1: 15.4        R2: 2.1         Error:  0.0V     0.0%
R1: 22.0        R2: 3.0         Error:  0.0V     0.0%
R1: 11.0        R2: 1.5         Error:  0.0V     0.0%
R1: 11.0        R2: 1.5         Error:  0.0V     0.0%
R1: 12.1        R2: 1.65        Error:  0.0V     0.0%
```

## E series options

```powershell
divider.exe -h
```
Output:
```text
usage: divider [-h] [-e E] vin vout

positional arguments:
  vin          Input voltage
  vout         Output voltage

options:
  -h, --help   show this help message and exit
  -e E, --e E  Either E3, E6, E12, E24, E48, R96 `extend`
 ```

Where extend is combination of E24 and E96.
