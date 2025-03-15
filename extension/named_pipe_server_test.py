import time
from extension.client import OrcaControllerClient
from extension.named_pipe_server import OrcaControllerServer
from extension.schema import CommandSchema


def test_health_check():
    """Test the /health endpoint using named pipes."""
    server = OrcaControllerServer()
    server.run_in_background_thread()
    # Ensure server has time to start
    time.sleep(0.5)
    OrcaControllerClient().send(CommandSchema.HEALTH_CHECK)
    response = OrcaControllerClient().receive()
    assert 'ok' in response
    server.stop()
