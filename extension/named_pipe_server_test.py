import time
import importlib
orcaCustomizations = importlib.import_module("orca-customizations")

class OrcaControllerClient():
    """A simple client for connecting to the server using named pipes"""

    def __init__(self, request_pipe=orcaCustomizations.REQUEST_PIPE, response_pipe=orcaCustomizations.RESPONSE_PIPE):
        self.request_pipe = request_pipe
        self.response_pipe = response_pipe

    def send (self, command):
        with open(self.request_pipe, "w") as request_pipe:
            request_pipe.write(command.value)

    def receive (self):
        with open(self.response_pipe, "r") as response_pipe:
            return response_pipe.readline().strip()

def test_health_check():
    """Test the /health endpoint using named pipes."""
    server = orcaCustomizations.OrcaControllerServer()
    server.run_in_background_thread()
    # Ensure server has time to start
    time.sleep(0.5)
    OrcaControllerClient().send(orcaCustomizations.CommandSchema.HEALTH_CHECK)
    response = OrcaControllerClient().receive()
    assert 'ok' in response
    server.stop()
