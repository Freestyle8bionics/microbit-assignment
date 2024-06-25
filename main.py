huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_FACE_RECOGNITION)

def on_forever():
    huskylens.request()
    serial.write_value("box", huskylens.readBox_ss(1, Content3.ID))
basic.forever(on_forever)
