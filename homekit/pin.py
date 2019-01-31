import argparse
import sys
from homekit.controller import Controller


def setup_args_parser():
    parser = argparse.ArgumentParser(description='HomeKit pairing app')
    parser.add_argument('-d', action='store', required=True, dest='device',
                        help='HomeKit Device ID (use discover to get it)')
    # parser.add_argument('-p', action='store', required=False, dest='pin', help='HomeKit configuration code')
    parser.add_argument('-f', action='store', required=False, dest='file', help='HomeKit pairing data file')
    parser.add_argument('-a', action='store', required=False, dest='alias', help='alias for the pairing')
    return parser.parse_args()


if __name__ == '__main__':
    args = setup_args_parser()

    controller = Controller()
    
    try:
        controller.request_pin(args.alias, args.device)
        # pairing = controller.get_pairings()[args.alias]
        # pairing.list_accessories_and_characteristics()
        # controller.save_data(args.file)
        print('Pin request started check device'.format(a=args.alias))
    except Exception as e:
        print(e)
        sys.exit(-1)
