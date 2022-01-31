import numpy as np
from typing import Tuple
import argparse
import voltdiv.common as comm


def find_list(vin: float,
              vout: float,
              n_list: int = 5,
              e_value: np.ndarray = comm.E24) -> Tuple[np.ndarray, np.ndarray]:
    divider_matrix = np.array([[r2 / (r1 + r2) for r2 in e_value] for r1 in e_value])
    diff_matrix = np.abs(divider_matrix * vin - vout)
    index = np.argsort(diff_matrix.flatten())
    min_index_row, min_index_col = np.unravel_index(index, (e_value.size, e_value.size))
    r1 = e_value[min_index_row[0:n_list]]
    r2 = e_value[min_index_col[0:n_list]]
    return r1, r2


def main(vin: float, vout: float, e_value: str) -> None:
    try:
        e = comm.Edict[e_value.upper()]
    except KeyError:
        print('{} is not in E values list'.format(e_value))
        return
    r1, r2 = find_list(vin, vout, e_value=e)
    print('Closest resistor values for Vin: {}V and Vout: {}V are'.format(vin, vout))
    for R1, R2 in zip(r1, r2):
        print('R1: {} \tR2: {} \tError: {:4.2}V  \t{:4.2}%'.format(R1, R2, vout - comm.divider(R1, R2, vin),
                                                                   (comm.divider(R1, R2, vin) - vout) / vout * 100))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('vin', type=float, help="Input voltage")
    parser.add_argument('vout', type=float, help="Output voltage")
    parser.add_argument('-e', '--e', type=str, default='E24', help='Either E3, E6, E12, E24, E48, R96 `extend`')
    parser.parse_args()
    args = parser.parse_args()
    main(args.vin, args.vout, args.e)
