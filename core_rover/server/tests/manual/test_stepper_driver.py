from core_rover.server.subsystems.drivers import StepperMotor

if __name__ == '__main__':
    motor = StepperMotor(103)
    print motor.stop()