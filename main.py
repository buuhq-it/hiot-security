
import multiprocessing
from devices import watch, camera, elder_tracker, smart_home

if __name__ == "__main__":
    jobs = [
        multiprocessing.Process(target=watch.run),
        multiprocessing.Process(target=camera.run),
        multiprocessing.Process(target=elder_tracker.run),
        multiprocessing.Process(target=smart_home.run)
    ]
    for job in jobs:
        job.start()
