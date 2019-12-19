import os
import click
import yaml

from pathlib import Path


@click.command()
@click.argument('cfg_file', type=click.Path(dir_okay=False, exists=True), required=True)
@click.argument('dst', type=click.Path(file_okay=False, writable=True), required=True)
def main(cfg_file, dst):
    with open(cfg_file) as buf:
        cfg = yaml.load(buf, Loader=yaml.FullLoader)

    print(cfg)
    dst = Path(dst)
    dst.mkdir(exist_ok=True)
    os.system(f'cp -r {cfg["location"]} {dst}')


if __name__ == "__main__":
    main()
