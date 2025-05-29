#!/usr/bin/env python

from crazyflie_py import Crazyswarm
import numpy as np


def main():
    Z = 0.5  # 호버링 고도
    X_FORWARD = 1.0  # x방향 이동 거리
    MOVE_DURATION = 3.0  # x방향 이동 시간

    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    allcfs.arm(True)
    timeHelper.sleep(3.0)

    # 이륙
    allcfs.takeoff(targetHeight=Z, duration=Z + 1.0)
    timeHelper.sleep(Z + 1.5)

    # x 방향으로 이동
    for cf in allcfs.crazyflies:
        start = np.array(cf.initialPosition) + np.array([0, 0, Z])
        end = start + np.array([X_FORWARD, 0, 0])
        cf.goTo(end, 0, MOVE_DURATION)
    timeHelper.sleep(MOVE_DURATION + 0.5)

    # 착륙
    allcfs.land(targetHeight=0.02, duration=Z + 1.0)
    timeHelper.sleep(Z + 1.0)


if __name__ == '__main__':
    main()
