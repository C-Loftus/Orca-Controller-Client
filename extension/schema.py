from enum import Enum 

class CommandSchema(Enum):
    """
    Enum representing the commands that can be sent to the server using named pipes.
    """
    # Make sure the server is running
    HEALTH_CHECK = "health_check"
    # Increase the volume of the default voice in orca
    VOLUME_UP = "volume_up"
    # Decrease the volume of the default voice in orca
    VOLUME_DOWN = "volume_down"
    # Speak arbitrary text
    SPEAK = "speak"