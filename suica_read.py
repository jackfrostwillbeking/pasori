#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import os
import sys
import pygame.mixer
import time
import io

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/nfcpy')
dir=os.path.dirname(os.path.abspath(__file__))
import nfc

idlist = dir+'/id.txt'
muon_sound = dir+'/muon_01sec.wav'
fail_sound = dir+'/nc43688.wav'
#coin_sound = dir+'nc23750.wav'
coin_sound = dir+'/nc106374.wav'
#coin_sound = dir+'coin05.mp3'
pygame.mixer.init()
coin=pygame.mixer.Sound(coin_sound)
muon=pygame.mixer.Sound(muon_sound)
fail=pygame.mixer.Sound(fail_sound)
id=''
flag=False

def connected(tag):
  idm=str(tag.idm).encode("hex")
  pmm=str(tag.pmm).encode("hex")
  print str(tag.idm).encode("hex")
  print str(tag.pmm).encode("hex")
  global id
  id=idm+pmm

if __name__ == "__main__":
  clf = nfc.ContactlessFrontend('usb')
  if clf.connect(rdwr={'on-connect': connected}):
    with open(idlist) as f:
      lines = f.readlines()
      for I in lines:
        ll = I.strip()
        print(type(ll))
        print(ll)
        if ll == id:
          flag=True
          break
  pygame.mixer.Sound.play(muon)
  time.sleep(2)
  if flag:
    pygame.mixer.Sound.play(coin)
    time.sleep(3)
  else:
    pygame.mixer.Sound.play(fail)
    time.sleep(3)
