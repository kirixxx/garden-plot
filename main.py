import os
import pickle
import click
from click_shell import shell
from restore.restore_service import RestoreService
from world.gamemap import World

@click.option(
    '--use-save',
    default=False,
    help="Set this parameter as 'True' to upload previous session, otherwise 'False'."
)
@shell(prompt='> ', intro='Launching cli application...')
def main(use_save):
    '''Model of a garden plot'''
    global garden
    garden = None
    
    restore_service = RestoreService()

    if use_save:
        garden = restore_service.restore_garden()

    if garden is None:
        garden = World()

@main.command(help='Create garden plot.', name='start-garden')
def start_garden():
    garden.start_garden()

@main.command(help='One day passes.', name='next-day')
def next_day():
    garden.commands("next_day")

@main.command(help='Adds a plant to the plot.', name='add-plant')
def add_plant():
    garden.commands("add_plant")

@main.command(help='Adds a tree to the plot.', name='add-tree')
def add_tree():
    garden.commands("add_tree")
    
@main.command(help='Adds a pest to the plot.', name='add-pests')
def add_pests():
    garden.commands("add_pests")
    
@main.command(help='Adds a pest to the plot.', name='weeding')
def add_pests():
    garden.commands("weeding")
    
@main.command(help='Watering plants.', name='water-plants')
def water_plants():
    garden.commands("water_plants")
    
@main.command(help='Save in file.', name='save-garden')
def save_garden():
    garden.commands("save")
    
@main.command(help='Inforamtion about any object.', name='info')
def save_garden():
    garden.commands("info")

if __name__ == '__main__':
    main()