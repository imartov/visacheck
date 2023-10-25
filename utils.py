from random import uniform, randint
from datetime import datetime
from time import sleep


def wait_random_time(fromm:float, to:float) -> None:
    random_wait_time = uniform(fromm, to)
    sleep(random_wait_time)

def get_random_int(fromm:int, to:int, end=False, driver=False) -> int:
    to = int(driver.execute_script("return document.body.scrollHeight")) if end else to
    return randint(fromm, to)

def get_current_time() -> str:
    return datetime.now().strftime('%d.%m.%Y %H:%M:%S')

def main():
    pass

if __name__ == "__main__":
    main()