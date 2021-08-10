"""
    CLI for interacting with and uploading blankly models.
    Copyright (C) 2021  Emerson Dove

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import argparse

parser = argparse.ArgumentParser(description='Blankly CLI & deployment tool.')
parser.add_argument('--deploy',
                    metavar='deploy',
                    type=str,
                    help='Main deploy command for the module. Input a path to a deployment formatted bot folder.')


def main():
    args = parser.parse_args()
    print(vars(args))
    if args.deploy:
        print(args)

        print("blankly deployment is coming soon!")


main()
