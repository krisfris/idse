import sys
import json
import click

from idse.api import *


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj['app'] = QApplication(sys.argv)


class DataDictSerializer:
    def __init__(self, item_sep, key_value_sep):
        self.item_sep = item_sep
        self.key_value_sep = key_value_sep

    def dumps(self, data):
        return self.item_sep.join(self.key_value_sep.join((k, v)) for k, v in data.items())

    def loads(self, data):
        return dict(x.split(self.key_value_sep) for x in data.split(self.item_sep) if x)


@cli.command(name='dict')
@click.pass_context
@click.option('--data', default='')
@click.option('--json', 'json_', default=None)
@click.option('--item-sep', default=',')
@click.option('--key-value-sep', default='=')
def edit_dict(ctx, data, json_, item_sep, key_value_sep):
    if json_ is None:
        serializer = DataDictSerializer(item_sep, key_value_sep)
    else:
        serializer = json
        data = json_

    d = serializer.loads(data)
    r = prompt_dict(d)

    if r is not None:
        click.echo(serializer.dumps(r))
