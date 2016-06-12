#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import RPIO
import time

from tasten import tasten

BLA = 17
BLUB = 23

def setmeup():
        for i in [2,3,4,17,27,22,23,24,25,8]:
                RPIO.setup(i, RPIO.OUT, pull_up_down=RPIO.PUD_DOWN)
                RPIO.output(i, False)

def pushkey(keyname):
        eine, andere = tasten[keyname.lower()]
        drueckerle(eine, andere)

def drueckerle(eine, andere):
        print("drücke {} und {}".format(eine, andere))
        RPIO.output(andere, True)
        #time.sleep(0.2)
        RPIO.output(eine, True)

        time.sleep(0.4)

        RPIO.output(eine, False)
        #time.sleep(0.2)
        RPIO.output(andere, False)
        time.sleep(1.7)

def muh():
        RPIO.setup(BLA, RPIO.OUT)
        RPIO.setup(BLUB, RPIO.OUT)

        RPIO.output(BLA, True)
        time.sleep(1.25)
        RPIO.output(BLUB, True)

        time.sleep(1.25)

        RPIO.output(BLA, False)
        time.sleep(1.25)
        RPIO.output(BLUB, False)


def meh():
        for i in [2,3,4,17,27,22,23,24,25,8]:
                RPIO.setup(i, RPIO.OUT)

        for BLA in [2,3,4,17,27,22,]:
                for BLUB in [23,24,25,8]:
                        print("{} -> {}".format(BLA, BLUB))
                        RPIO.output(BLA, True)
                        RPIO.output(BLUB, True)
#
                        time.sleep(0.2)
#
                        RPIO.output(BLA, False)
                        RPIO.output(BLUB, False)
                        time.sleep(0.5)


if __name__ == '__main__':
        setmeup()
        # drueckerle(17, 23)
        pushkey('cm')
        pushkey('laser')
        pushkey('2')
        pushkey('go')
