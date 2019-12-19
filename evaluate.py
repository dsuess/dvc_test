import click
import json

@click.command()
@click.argument('ckpt-path', type=click.Path(dir_okay=False, exists=True), required=True)
@click.argument('eval-path', type=click.Path(dir_okay=False, writable=True), required=True)
def main(ckpt_path, eval_path):
    with open(ckpt_path) as buf:
        pred = buf.read()

    if pred == 'class_b':
        accuracy = 1
    else:
        accuracy = 0

    with open(eval_path, 'w') as buf:
        json.dump({'accuracy': accuracy}, buf)


if __name__ == "__main__":
    main()
