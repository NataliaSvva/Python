from time import sleep
class TrafficLight:
    __color=("Красный", "Желтый", "Зеленый")
    def running(self):
        i = 0
        while i < 3:
                print(f"Светофор горит {TrafficLight.__color[i]}")
                if i == 0:
                    sleep(7)
                if i == 1:
                    sleep(2)
                if i == 2:
                    sleep(10)
                i += 1
TrafficLight = TrafficLight()
TrafficLight.running()