import click
import pandas as pd
from pathlib import Path


@click.command()
@click.argument('datadir', type=click.Path(file_okay=False, exists=True), required=True)
@click.argument('ckpt-path', type=click.Path(dir_okay=False, writable=True), required=True)
def main(datadir, ckpt_path):
    df = pd.read_csv(Path(datadir) / 'annotations.csv', header=None)
    prediction = df[1].mode()[0]
    with open(ckpt_path, 'w') as buf:
        buf.write(prediction)


if __name__ == "__main__":
    main()
