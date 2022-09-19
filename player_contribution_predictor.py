#!/usr/bin/env python

import click
from dblib.predict_impact import predict_impact

# build a click group
@click.group()
def cli():
    """A simple CLI check if a given player will have a significant contribiution in a season"""


# build a click command
@cli.command()
@click.option(
    "--player",
    default="Che Adams",
    help="player to use for prediction",
)
def cli_predict(player):
    """Execute prediction"""
    prediction = predict_impact(player)
    print(prediction)


# run the CLI
if __name__ == "__main__":
    cli()