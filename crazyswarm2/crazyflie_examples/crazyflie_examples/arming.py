#!/usr/bin/env python

from crazyflie_py import Crazyswarm

def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    for cf in allcfs.crazyflies:
        cf.arm(True)
        timeHelper.sleep(10.0)


if __name__ == '__main__':
    main()
