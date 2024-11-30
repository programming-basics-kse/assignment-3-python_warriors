import argparse
import sys
import total
import interactive
import medals
import overall
import additianal_task as at


parser = argparse.ArgumentParser("Information from user about olympic data")
parser.add_argument("address_file", type=str, help="File with data")
parser.add_argument("command", choices=["medals", "total", "overall", "interactive", "top"], help="optional")
parser.add_argument("arg", nargs="*", help="")
parser.add_argument("-output", type=str, help="Output file", default=None)

args = parser.parse_args()
file_address = args.address_file
if file_address != "OlympicAthletes-athlete_events.tsv":
    sys.exit("Not a valid file")
command = args.command
args_for_function = args.arg
output_file = args.output


if command == "medals":
    country = args_for_function[0]
    year_of_olympics = args_for_function[1]
    medals.output_into_scr(file_address, country, year_of_olympics, output_file)
elif command == "total":
    year_of_olympics = args_for_function[0]
    total.total_medals(file_address, year_of_olympics, output_file)
elif command == "overall":
    overall.overall(file_address, " ".join(args_for_function), output_file)
elif command == "interactive":
    country = input("Please enter a country: ")
    interactive.interactive(file_address, country, output_file)
elif command == "top":
    list_of_data = args_for_function.split(" ")
    at.additional_task(file_address, list_of_data, output_file)