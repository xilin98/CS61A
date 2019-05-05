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
		>>> queen.place
		False
