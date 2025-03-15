import extension.named_pipe_server as named_pipe_server
import logging

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.FileHandler("/tmp/orca-controller.log"))
LOGGER.info("Orca controller server started successfully")

# time.sleep(1000)

server = named_pipe_server.OrcaControllerServer()
# server.serve_forever()