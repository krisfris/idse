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


@cli.command()
@click.pass_context
@click.option('--data', default='')
@click.option('--sep', default=',')
def color(ctx, data, sep):
    d = QColor(*[int(x) for x in data.split(sep)]) if data else QColor()
    r = QColorDialog.getColor(d, None, 'Select Color', QColorDialog.ShowAlphaChannel)
    if r.isValid():
        click.echo(','.join(str(x) for x in r.getRgb()))


@cli.command()
@click.pass_context
@click.option('--data', default='')
@click.option('--sep', default=',')
@click.option('--pos', default=None)
@click.option('--pos-sep', default=',')
def context(ctx, data, sep, pos, pos_sep):
    menu = QMenu(None)
    actions = [menu.addAction(x) for x in data.split(sep)]
    pos = QCursor.pos() if pos is None else QPoint(*[int(x) for x in pos.split(pos_sep)])
    r = menu.exec_(pos)
    if r:
        click.echo(r.text())
