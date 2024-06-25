huskylens.initI2c()
huskylens.initMode(protocolAlgorithm.ALGORITHM_FACE_RECOGNITION)
basic.forever(function on_forever() {
    huskylens.request()
    serial.writeValue("box", huskylens.readBox_ss(1, Content3.ID))
})
