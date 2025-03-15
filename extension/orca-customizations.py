import logging
import sys
from enum import Enum 
import os
import threading

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG) 
file_handler = logging.FileHandler("/tmp/orca-controller.log")
formatter = logging.Formatter("%(levelname)s - %(message)s - %(asctime)s") 
file_handler.setFormatter(formatter)
LOGGER.addHandler(file_handler)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
LOGGER.addHandler(console_handler)

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

REQUEST_PIPE = "/tmp/orca_controller_request.pipe"
RESPONSE_PIPE = "/tmp/orca_controller_response.pipe"


class OrcaControllerServer:
    def __init__(self, request_pipe=REQUEST_PIPE, response_pipe=RESPONSE_PIPE):
        self.request_pipe = request_pipe
        self.response_pipe = response_pipe
        self._ensure_pipes_exist()
        self.running = True

    def _ensure_pipes_exist(self):
        """Ensure named pipes exist before starting the server."""
        for pipe in [self.request_pipe, self.response_pipe]:
            try:
                os.mkfifo(pipe)
            except FileExistsError:
                pass  # Pipe already exists; that is ok

    def handle_request(self, request):
        """Process the request and return an appropriate response."""
        match request:
            case CommandSchema.HEALTH_CHECK.value:
                return "200, ok"
            case _:
                return f"404, error undefined request '{request}'"

    def serve_forever(self):
        """Continuously read from the request pipe and write to the response pipe."""
        logging.debug(f"Server started using named pipes: {self.request_pipe}, {self.response_pipe}")
        while self.running:
            with open(self.request_pipe, "r") as request_pipe:
                request = request_pipe.readline().strip()
                if not request:
                    continue  # Ignore empty requests
                
                response = self.handle_request(request)

                with open(self.response_pipe, "w") as response_pipe:
                    response_pipe.write(response + "\n")

    def run_in_background_thread(self):
        """Run the server in a background thread."""
        self.server_thread = threading.Thread(target=self.serve_forever, daemon=True)
        self.server_thread.start()

    def stop(self):
        """Stop the server gracefully."""
        self.running = False

try: 
    import orca.speech
    orca.speech.init()
    orca.speech.speak("Orca controller server started successfully", interrupt=True)
    LOGGER.info("Orca controller server started successfully")
except Exception as e:
    print(e)
    LOGGER.fatal(f"Failed to import Orca dependencies for controller server {e}")

try:
    server = OrcaControllerServer()
    server.serve_forever()
except Exception as e:
    LOGGER.fatal(f"Failed to start Orca controller server: {e}")