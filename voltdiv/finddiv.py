import numpy as np
import argparse
import voltdiv.common as comm


def find_closet(vin: float, vout: float, e_value: np.ndarray = comm.E24) -> tuple[float, float]:
    closest_r1 = None
    closest_r2 = None
    closest_vout = 0
    for r1 in e_value:
        for r2 in e_value:
            if np.abs(comm.divider(r1, r2, vin) - vout) < np.abs(closest_vout - vout):
                closest_vout = comm.divider(r1, r2, vin)
                closest_r1 = r1
                closest_r2 = r2
    return closest_r1, closest_r2


def divider(vin: float, vout: float, e_value: str) -> None:
    try:
        e = comm.Edict[e_value.upper()]
    except KeyError:
        print('{} is not in E values list'.format(e_value))
        return
    r1, r2 = find_closet(vin, vout, e_value=e)
    print('Closest resistor values for Vin: {}V and Vout: {}V is'.format(vin, vout))
    print('R1: {}'.format(r1))
    print('R1: {}'.format(r2))
    print(
        'With error {:4.2}V, {:4.2}%'.format(vout - comm.divider(r1, r2, vin),
                                             (comm.divider(r1, r2, vin) - vout) / vout * 100))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('vin', type=float, help="Input voltage")
    parser.add_argument('vout', type=float, help="Output voltage")
    parser.add_argument('-e', '--e', type=str, default='E24', help='Either E3, E6, E12, E24, E48, R96 `extend`')
    parser.parse_args()
    args = parser.parse_args()
    divider(args.vin, args.vout, args.e)


if __name__ == '__main__':
    main()
