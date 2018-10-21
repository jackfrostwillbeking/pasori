import nfc
from binascii import hexlify


def on_connect(tag):
    idm, pmm = tag.polling(system_code=0xfe00)
    tag.idm, tag.pmm, tag.sys = idm, pmm, 0xfe00

    sc = nfc.tag.tt3.ServiceCode(93, 0x0b)  # 174B
    bc = nfc.tag.tt3.BlockCode(1, service=0)
    data = tag.read_without_encryption([sc], [bc])
    print 'str:', data
    print 'hex:', hexlify(data)


def main():
    with nfc.ContactlessFrontend('usb') as clf:
        clf.connect(rdwr={'on-connect': on_connect})


if __name__ == '__main__':
    main()
