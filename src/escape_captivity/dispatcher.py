from urllib.parse import urlparse

import click

from .solver.ice import IceSolver
from .solver.db_regio_southeast import DBRegioSouthEastSolver
from .solver.db_station import DBStationSolver
from .solver.abellio import AbellioSolver


def dispatch(captive_portal_url: str):
    solvers = [
        IceSolver(),
        DBRegioSouthEastSolver(),
        DBStationSolver(),
        AbellioSolver(),
    ]
    portal_url_parsed = urlparse(captive_portal_url)
    for solver in solvers:
        if solver.applicable(portal_url_parsed):
            click.echo(f"Using solver {solver.__class__.__name__}")
            if solver.solve(portal_url_parsed):
                click.echo(f"{solver.__class__.__name__}: Success")
                return True
