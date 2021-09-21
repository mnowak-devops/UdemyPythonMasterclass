import sys
import os.path

# Checking the IP addres and file validation
def ip_file_valid():

    ip_file = input(r"\n% Enter Ip file path and name (e.g C:\Users\Documents\myfile.txt: ")

    #Checking if file exists
    if os.path.exists(ip_file) == True:
        print("\n* IP file is valid. \n")
    else:
        print("\n* IP File {} is not valid or do not exist. Please check amd try again. \n".format(ip_file))
        sys.exit()

    # Open file fore reading it
    selected_ip_file = open(ip_file, 'r')

    # Start frome beginning of file
    selected_ip_file.seek(0)

    #Reading file line by line
    lp_list = selected_ip_file.readlines()

    selected_ip_file.close()

    return lp_list

