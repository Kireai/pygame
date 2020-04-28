from typing import Optional, Union
from pygame.event import Event

def get_ticks() -> int: ...
def wait(milliseconds: int) -> int: ...
def delay(milliseconds: int) -> int: ...
def set_timer(eventid: Union[int, Event], milliseconds: int, once: Optional[bool]=False) -> None: ...
class Clock:
    def tick(self, framerate: Optional[int]=0) -> int: ...
    def tick_busy_loop(self, framerate: Optional[int]=0) -> int: ...
    def get_time(self) -> int: ...
    def get_rawtime(self) -> int: ...
    def get_fps(self) -> float: ...