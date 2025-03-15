from extension.named_pipe_server import REQUEST_PIPE, RESPONSE_PIPE
from extension.schema import CommandSchema


class OrcaControllerClient():
    """A simple client for connecting to the server using named pipes"""

    def __init__(self, request_pipe=REQUEST_PIPE, response_pipe=RESPONSE_PIPE):
        self.request_pipe = request_pipe
        self.response_pipe = response_pipe

    def send (self, command: CommandSchema):
        with open(self.request_pipe, "w") as request_pipe:
            request_pipe.write(command.value)

    def receive (self):
        with open(self.response_pipe, "r") as response_pipe:
            return response_pipe.readline().strip()