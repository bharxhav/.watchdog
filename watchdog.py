"""
This is the last time I'll ever write a docstring, thanks to watchdog!
"""

import typer
from git import Repo

app = typer.Typer()


@app.command()
def initiate(path: str = "."):
    """
    Initialize watchdog in the given repository path.
    """
    typer.echo(f"Initiating watchdog in {path}")


@app.command()
def status(path: str = "."):
    """
    Minimal Git Status.
    """
    repo = Repo(path)
    if repo.is_dirty():
        typer.echo("There are uncommitted changes.")
    else:
        typer.echo("Repository is clean.")


if __name__ == "__main__":
    app()
