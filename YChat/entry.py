from .runable.gui_client import main as client_gui_main
from .runable.cli_start_server import main as server_cli_main


def run_client_gui():
	client_gui_main()

def run_server_cli():
	server_cli_main()