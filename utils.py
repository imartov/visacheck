from random import uniform, randint
from datetime import datetime
from time import sleep


def get_random_wait_time(fromm:float, to:float) -> float:
    random_wait_time = uniform(fromm, to)
    return random_wait_time

def wait_random_time(fromm:float, to:float) -> None:
    random_wait_time = get_random_wait_time(fromm=fromm, to=to)
    sleep(random_wait_time)

def get_random_int(fromm:int, to:int) -> int:
    random_int = randint(fromm, to)
    return random_int

def main():
    pass

if __name__ == "__main__":
    main()