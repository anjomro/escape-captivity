# SPDX-FileCopyrightText: 2023-present anjomro <py@anjomro.de>
#
# SPDX-License-Identifier: EUPL-1.2
import click

from escape_captivity.__about__ import __version__
from escape_captivity.detect_captive_portal import get_captive_portal_address, check_internet_connection
from escape_captivity.dispatcher import dispatch


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="escape-captivity")
def escape_captivity():
    """Escape Captivity is a tool to automatically solve captive portals"""
    if check_internet_connection():
        click.echo("Internet connection available, no captive portal detected")
    else:
        click.echo("Captive portal detected, trying to solve")
        # Get captive portal address
        captive_portal_address = get_captive_portal_address()
        if captive_portal_address is not None:
            click.echo(f"Captive portal address: {captive_portal_address}")
            # Dispatch captive portal address
            dispatch(captive_portal_address)
            # Check if internet connection is available
            if check_internet_connection():
                click.echo("Captive portal solved, you are free now")
            else:
                click.echo("Captive portal could not be solved. Sorry.")
        else:
            click.echo("Captive portal address could not be determined. Sorry.")


@click.group(invoke_without_command=True)
def dev():
    """Subcommand for development tools"""
    click.echo(f"Captive Portal: {get_captive_portal_address()}")


escape_captivity.add_command(dev)
