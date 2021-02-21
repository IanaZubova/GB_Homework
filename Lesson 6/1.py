import time


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        c = 0
        while c < 3:
            print(f'{TrafficLight.__color[c]}')
            if c == 0:
                time.sleep(7)
            elif c == 1:
                time.sleep(2)
            else:
                time.sleep(3)

            c += 1


t = TrafficLight()
t.running()