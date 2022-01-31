import numpy as np
from typing import List, Tuple, Any
import argparse

E3 = np.array([1.0, 2.2, 4.7])

E6 = np.array([1.0, 1.5, 2.2, 3.3, 4.7, 6.8])

E12 = np.array([1.0, 1.2, 1.5, 1.8, 2.2, 2.7,
                3.3, 3.9, 4.7, 5.6, 6.8, 8.2])

E24 = np.array([1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0,
                3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1])

E48 = np.array([1.00, 1.05, 1.10, 1.15, 1.21, 1.27, 1.33, 1.40, 1.47, 1.54, 1.62, 1.69,
                1.78, 1.87, 1.96, 2.05, 2.15, 2.26, 2.37, 2.49, 2.61, 2.74, 2.87, 3.01,
                3.16, 3.32, 3.48, 3.65, 3.83, 4.02, 4.22, 4.42, 4.64, 4.87, 5.11, 5.36,
                5.62, 5.90, 6.19, 6.49, 6.81, 7.15, 7.50, 7.87, 8.25, 8.66, 9.09, 9.53])

E96 = np.array([1.00, 1.02, 1.05, 1.07, 1.10, 1.13, 1.15, 1.18, 1.21, 1.24, 1.27, 1.30,
                1.33, 1.37, 1.40, 1.43, 1.47, 1.50, 1.54, 1.58, 1.62, 1.65, 1.69, 1.74,
                1.78, 1.82, 1.87, 1.91, 1.96, 2.00, 2.05, 2.10, 2.16, 2.21, 2.26, 2.32,
                2.37, 2.43, 2.49, 2.55, 2.61, 2.67, 2.74, 2.80, 2.87, 2.94, 3.01, 3.09,
                3.16, 3.24, 3.32, 3.40, 3.48, 3.57, 3.65, 3.74, 3.83, 3.92, 4.02, 4.12,
                4.22, 4.32, 4.42, 4.53, 4.64, 4.75, 4.87, 4.99, 5.11, 5.23, 5.36, 5.49,
                5.62, 5.76, 5.90, 6.04, 6.19, 6.34, 6.49, 6.65, 6.81, 6.98, 7.15, 7.32,
                7.50, 7.68, 7.87, 8.06, 8.25, 8.45, 8.66, 8.87, 9.09, 9.31, 9.53, 9.76])

Edict = {'E3': E3,
         'E6': E6,
         'E12': E12,
         'E24': E24,
         'E48': E48,
         'E96': E96,
         'extend': np.append(E24, E96)}


def divider(r1: float, r2: float, vin: float) -> float:
    return vin * r2 / (r1 + r2)


def find_closet(vin: float, vout: float, e_value: np.ndarray = E24) -> Tuple:
    closest_r1 = None
    closest_r2 = None
    closest_vout = 0
    for r1 in e_value:
        for r2 in e_value:
            if np.abs(divider(r1, r2, vin) - vout) < np.abs(closest_vout - vout):
                closest_vout = divider(r1, r2, vin)
                closest_r1 = r1
                closest_r2 = r2
    return closest_r1, closest_r2


def main(vin: float, vout: float, e_value: str) -> None:
    try:
        e = Edict[e_value]
    except KeyError:
        print('{} is not in E values list'.format(e_value))
        return
    r1, r2 = find_closet(vin, vout, e)
    print('Closest resistor values for Vin: {} and Vout: {} is'.format(vin, vout))
    print('R1: {}'.format(r1))
    print('R1: {}'.format(r2))
    print('With error {}V, {}%'.format(vout - divider(r1, r2, vin), (divider(r1, r2, vin) - vout) / vout * 100))


if __name__ == '__main__':
    # print(find_closet(5, 3.3, e_value=np.append(E24, E96)))
    parser = argparse.ArgumentParser()
    parser.add_argument('vin', type=float, help="Input voltage")
    parser.add_argument('vout', type=float, help="Output voltage")
    parser.add_argument('--set', type=str, default='E24', help='Either `E12` or `E24`, `extend`')
    parser.parse_args()
    args = parser.parse_args()
    main(args.vin, args.vout, args.set)
