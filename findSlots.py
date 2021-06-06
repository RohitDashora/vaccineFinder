import argparse
import finderLogic

#adding argparse to go with command line argument, this will also generate helptext
ap= argparse.ArgumentParser()
ap.add_argument("pincode", help="Pincode of your location")
ap.add_argument("agelimit", help="Age limit, choose for 18 or 45", type=int, choices=[18,45])
#ap.add_argument("--date", help="Date when you are looking for vaccination [format dd-mm-yyyy] by default its today's date and onwards")
args = ap.parse_args()

#top level variables
ageLimit=args.agelimit
pincode=args.pincode

output=finderLogic.findslots(pincode=pincode, ageLimit=ageLimit)
print(*output, sep='\n')