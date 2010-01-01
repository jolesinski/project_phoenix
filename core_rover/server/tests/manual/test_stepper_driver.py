from subsystems.drivers import StepperMotor

if __name__ == '__main__':
    motor = StepperMotor(16)
    print motor.stop()
