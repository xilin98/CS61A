This file holds the tests that you create. Remember to import the python file(s)
you wish to test, along with any other modules you may need.
Run your tests with "python3 ok -t --suite SUITE_NAME --case CASE_NAME -v"
--------------------------------------------------------------------------------

Suite 1

	>>> from ants import *

	Case Example
		>>> x = 5
		>>> x
		5

  Case debug
	  >>> from ants import *
		>>> hive, layout = Hive(AssaultPlan()), dry_layout
		>>> dimensions = (1, 9)
		>>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
		>>> #
		>>> # Testing ShortThrower miss
		>>> ant = ShortThrower()
		>>> out_of_range = Bee(2)
		>>> colony.places["tunnel_0_0"].add_insect(ant)
		>>> colony.places["tunnel_0_4"].add_insect(out_of_range)
		>>> ant.action(colony)

	Case B
		>>> import ants, importlib
		>>> importlib.reload(ants)
		<module 'ants' from 'C:\\Users\\orange\\desktop\\cs61a\\cs61a\\projects\\ants\\ants.py'>
		>>> hive = ants.Hive(ants.AssaultPlan())
		>>> dimensions = (2, 9)
		>>> colony = ants.AntColony(None, hive, ants.ant_types(),
		...         ants.dry_layout, dimensions)
		>>> #
		>>> # Adding/Removing QueenAnt with Container
		>>> queen = ants.QueenAnt()
		>>> impostor = ants.QueenAnt()
		>>> container = ants.TankAnt()
		>>> colony.places['tunnel_0_3'].add_insect(container)
		>>> colony.places['tunnel_0_3'].add_insect(impostor)
		>>> impostor.action(colony)
		>>> colony.places['tunnel_0_3'].ant is container
		True
		>>> container.place is colony.places['tunnel_0_3']
		True
		>>> container.contained_ant is None
		True
		>>> impostor.place is None
		True
		>>> colony.places['tunnel_0_3'].add_insect(queen)
		>>> colony.places['tunnel_0_3'].remove_insect(queen)
		>>> container.contained_ant is queen
		True
  Case C
		>>> from ants import *
		>>> hive, layout = Hive(AssaultPlan()), dry_layout
		>>> dimensions = (1, 9)
		>>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
		>>> # Testing Scare
		>>> error_msg = "ScaryThrower doesn't scare for exactly two turns."
		>>> scary = ScaryThrower()
		>>> bee = Bee(3)
		>>> colony.places["tunnel_0_0"].add_insect(scary)
		>>> colony.places["tunnel_0_8"].add_insect(bee)
		>>> scary.action(colony)
		>>> bee.action(colony)
		>>> bee.place.name
		'tunnel_0_8'
		>>> colony.time=1
		>>> slow=SlowThrower()
		>>> colony.places["tunnel_0_2"].add_insect(slow)
		>>> slow.action(colony)
    >>> bee.action(colony)
		>>> bee.place.name
		'tunnel_0_8'i
		>>> for _ in range(2):
		...    bee.action(colony)
		>>> bee.place.name
		'tunnel_0_8'
  Case D
		>>> from ants import *
		>>> hive, layout = Hive(AssaultPlan()), dry_layout
		>>> dimensions = (1, 9)
		>>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
		>>> laser = LaserAnt()
		>>> ant = HarvesterAnt(2)
		>>> bee1 = Bee(2)
		>>> bee2 = Bee(2)
		>>> bee3 = Bee(2)
		>>> bee4 = Bee(2)
		>>> colony.places["tunnel_0_0"].add_insect(laser)
		>>> colony.places["tunnel_0_0"].add_insect(bee4)
		>>> colony.places["tunnel_0_3"].add_insect(bee1)
		>>> colony.places["tunnel_0_3"].add_insect(bee2)
		>>> colony.places["tunnel_0_4"].add_insect(ant)
		>>> colony.places["tunnel_0_8"].add_insect(bee3)
		>>> laser.action(colony)
		>>> round(bee4.armor,2)
		0.0
		>>> laser.action(colony)
		>>> round(bee3.armor,2)
		1.8
		>>> round(ant.armor,2)
		0.1
		# There is a bug if I test the '1.8' first
