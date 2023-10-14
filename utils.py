from random import uniform
from datetime import datetime
from time import sleep


def get_random_wait_time(fromm:float, to:float) -> float:
    random_wait_time = uniform(fromm, to)
    return random_wait_time

def wait_random_time(fromm:float, to:float) -> None:
    random_wait_time = get_random_wait_time(fromm=fromm, to=to)
    sleep(random_wait_time)


def main():
    print(datetime.now().time())
    wait_random_time(fromm=0.99, to=5.25)
    print(datetime.now().time())

if __name__ == "__main__":
    main()