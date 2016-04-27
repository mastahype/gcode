#!python 

def printInstructions():
	print("+------------------------------------------------------------------+")
	print("| GCode Repair Tool                                                |")
	print("+------------------------------------------------------------------+")
	print("| The purpose of this program is to resume a print that has        |")
	print("| previously died.                                                 |")
	print("|                                                                  |")
	print("| If you know the layer number where the print                     |")
	print("| died at, you resume printing at that layer.                      |")
	print("|                                                                  |")
	print("| If you don't have which layer the print stopped at you can take  |")
	print("| the total prited height of your object on the print bed (in mm)  |")
	print("| followed by the extrusion height of the print in milimeters.     |")
	print("+------------------------------------------------------------------+")
	print("|                                                                  |")
	print("| Syntax:                                                          |")
	print("|    gcode.py <arguments>                                          |")
	print("| Arguments:                                                       |")
	print("|     --dimensions, -d:                                            |")
	print("|          -d <total_height> <extrusion_height>                    |")
	print("|     --layer, -l:                                                 |")
	print("|          -l <layer_number>                                       |")
	print("|     --input, -i:                                                 |")
	print("|          -i <file_name>                                          |")
	print("|          If no file is specified, a default will be used         |")
	print("|     --output, -o:                                                |")
	print("|          -o <file_name>                                          |")
	print("|          If no file is specified a file named output.gcode will  |")
	print("|          be placed on the desktop                                |")
	print("+------------------------------------------------------------------+")