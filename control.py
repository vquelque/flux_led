# coding=utf-8
"""
 # @ Author: Valentin Quelquejay-Leclère
 # @ Create Time: 2020-03-04 17:03:25
 # @ Modified by: Valentin Quelquejay-Leclère
 # @ Modified time: 2020-03-04 17:31:10
 # @ Description: Control MagicHome LED Strip and eventually DMX lights 
 """
# Will maybe use https://pypi.org/project/PyDMXControl/ to control DMX later


from flux_led import WifiLedBulb, BulbScanner


def main():

    # Find the bulb on the LAN
    scanner = BulbScanner()
    scanner.scan(timeout=4)

    # Specific ID/MAC of the bulb to set
    # First LED STRIP
    bulb_info = scanner.getBulbInfoByID("2CF432CE8B6A")

    if bulb_info:

        bulb = WifiLedBulb(bulb_info["ipaddr"])
        bulb.update_state()
        print(bulb)

    else:
        print("Can't find bulb")


if __name__ == "__main__":
    main()

