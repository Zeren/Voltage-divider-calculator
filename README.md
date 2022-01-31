# Voltage divider calculator

Install from github:
```commandline
pip install --upgrade https://github.com/Zeren/Voltage-divider-calculator/tarball/main
```

Find voltage divider for 5V input voltage and 1.8V output voltage with combined E24 and E96. 
```commandline
python -m voltdiv.finddiv 5 1.8 -e extend
Closest resistor values for Vin: 5.0V and Vout: 3.7V is
R1: 1.37
R1: 3.9
With error -0.00018975332068338346V, 0.005128468126577931%
```

Find list of possible combination of voltage divider for 5V input voltage and 1.8V output voltage.
```commandline
python -m voltdiv.findlist 5 1.8
Closest resistor values for Vin: 5.0 and Vout: 1.8 are
R1: 3.9         R2: 2.2         Error: -0.0033V         0.18%
R1: 9.1         R2: 5.1         Error: 0.0042V          -0.23%
R1: 4.3         R2: 2.4         Error: 0.009V   -0.5%
R1: 1.8         R2: 1.0         Error: 0.014V   -0.79%
R1: 3.6         R2: 2.0         Error: 0.014V   -0.79%
```
