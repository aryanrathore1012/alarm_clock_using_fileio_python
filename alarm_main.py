########################################################### CREDITS ##############################################################################################

'''
                                                  WELCOME TO THE HOTEL_MANAGER

                    THIS PROGRAM IS AN ALARM THAT NOTIFIES THE USER THIS INCLUDES QUICK, DAILY, WEEKLY ALARMS

                                                    MADE BY : ARYAN RATHORE 
                                            COMPUTER SCIENCE ENGINEER AT VIT BHOPAL

                                                        CONTACT INFO
                                                       +91-9685071745
                                                aryanrathore13572002@gmail.com
                                               aryan.rathore2021@vitbhopal.ac.in

made from 2021-10-17 to 2021-10-24 
'''

####################################################### IMPORTS ###############################################################

import time
import datetime as dt
from playsound import playsound
from plyer import notification

####################################################### FUNCTIONS ###############################################################

'''                                                        IMPORTANT NOTE                                                              
                BEFORE YOU RUN THE PROGRAM MAKE SURE YOU READ AND FOLLOW THE LINES BELOW AND CHECK how_to_setup_alarm_log.txt 
                                                   OTHERWISE THE PROGRAM WONT RUN                                                      '''

# 2

'''   MAKE SURE YOU OPEN THE PROGRAM EVERYTIME YOU OPEN YOUR PC AND LET IT RUN IN THE BACKGROUND IT DOES NOT RUN IN BACKGROND BY DEFAULT  '''

# 3

'''   I HAVE TO SPECIFY A FILE PATH TO OPEN THE LOG (alarm_log.txt, alarm_rung.txt) FILES IF YOU ARE USING OR COPY PASTING MY CODE
    MAKE YOU CHANGE THE FILE PATHS LINES WHERE THE FILE PATH NEEDS TO BE SPECIFIED HAVE '# ---------------------' AT END  '''


#  THIS IS THE NOTIFY FUNCTION THAT SHOWS THE NOTIFICATION
def notify_user(alarm_hour, alarm_min, custom_message, custom_date, cuweek):

    # the current date time date and weekday that we will compare down below
    hours = dt.datetime.now().hour
    minutes = dt.datetime.now().minute
    cudate = dt.datetime.now().date()
    cuweek = dt.datetime.now().weekday()

    if str(hours) == alarm_hour and str(minutes) == alarm_min:

        # this code handles the daily reminders so there is no need for removal
        if custom_date == "None":

            for i in range(3):
                notification.notify(
                    title="|||DING DONG THE ALARM HAS RUNG|||",
                    message=custom_message,
                    app_icon="F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\pink.ico",
                    timeout=20)
                playsound('python_language/python_projects/alarm_clock/play.mp3')
                time.sleep(20)

            # after the alarm rings we update the alarm_rung.txt using thios code 
            with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_rung.txt", "r") as reading: # ---------------------
                content = reading.read()

            content = content + \
            f"The alarm ({uhour}:{uminute}|{umessage}|{udate}|{uweek}) has rung.\n"

            reading.close()

            with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_rung.txt", "w") as writing: # ---------------------
                writing.write(content)

            writing.close()

        # these alrams are temprory they just run once and then never again so we will remove them
        elif str(custom_date) == str(cudate):

            for i in range(3):
                notification.notify(
                    title="|||DING DONG THE ALARM HAS RUNG|||",
                    message=custom_message,
                    app_icon="F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\pink.ico",
                    timeout=20)
                playsound('python_language/python_projects/alarm_clock/play.mp3')
                time.sleep(20)

            with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_rung.txt", "r") as reading: # ---------------------
                content = reading.read()

            content = content + \
                f"The alarm ({uhour}:{uminute}|{umessage}|{udate}|{uweek}) has rung.\n"

            reading.close()

            with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_rung.txt", "w") as writing: # ---------------------
                writing.write(content)

            writing.close()

            # this code removes the unessecary alarms that have already rung once and will never ring again from the code.
            with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_log.txt", "r") as reading: # ---------------------
                content = reading.read()  # opening the file and readng it

                utime = f"{uhour}:{uminute}|{umessage}|{udate}|{uweek},"

                content = content.replace(utime, "")

                reading.close()

                # then we open the file and write the log
                with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_log.txt", "w") as writing: # ---------------------
                    writing.write(content)

                writing.close()

        elif str(custom_week) == str(cuweek):

            for i in range(3):
                notification.notify(
                    title="|||DING DONG THE ALARM HAS RUNG|||",
                    message=custom_message,
                    app_icon="F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\pink.ico",
                    timeout=20)
                playsound('python_language/python_projects/alarm_clock/play.mp3')
                time.sleep(20)

            # this code updates the alarm_rung.txt file after the alarm has rung
            with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_rung.txt", "r") as reading: # ---------------------
                content = reading.read()

            content = content + \
                f"The alarm ({uhour}:{uminute}|{umessage}|{udate}|{uweek}) has rung.\n"

            reading.close()

            with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_rung.txt", "w") as writing: # ---------------------
                writing.write(content)

            writing.close()

#######################################################################################################################################

print("\n---------------------------------------------------------------------------------------------------------\n")
print(" -------------------- welcome the python alram clock -------------------- ")
print("\n---------------------------------------------------------------------------------------------------------\n")

ui = input("\nEnter 1 if you wanna set a new alarm here\npress 2 to check all the active alarms\npress 3 to delete an active alarm\npress 4 to see all the alarm that have rung aka an alarm_rung log.\nor (press enter to let the alarm run in the background) : ")

if ui == "1":
    user_options = int(input('''\n\nEnter 1 one if you wanna add a quick reminder today
Enter 2 if you wanna add an alarm on a perticlar date and time
Enter 3 if you want the alarm to ring a specific time everyday aka a daily alarm
Enter 4 if you wanna add an alarm that rings every week on specific days and time for example (alarm rings on monday 13:00 every week) aka weekly alarm here : '''))

    # 1 and 2 have specific dates the alarm is supposed to ring only 1 time so i have to renmove the logs as the alarm rings
    if user_options == 1:

        # this part of the code takes the info from the user
        uhour = int(input("Enter the hour here(in 24 hour clock time): "))
        uminute = int(input("Enter the minute here: "))
        umessage = input("enter the message you want the alarm to show here: ")
        udate = dt.datetime.now().date()
        uweek = None

        # the stucture of the log is made
        utime = f"{uhour}:{uminute}|{umessage}|{udate}|{uweek},"

        # then we open the file and the log
        with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_log.txt", "r") as reading:  # ---------------------
            content = reading.read()  # opening the file and readng it

        content = content + utime

        reading.close()

        # then we open the file and write the log
        with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_log.txt", "w") as writing: # ---------------------
            writing.write(content)

        writing.close()

    # perticular date and time should be removed from log as soon as it rings
    elif user_options == 2:

        udate = input("Enter the date in this format (2022-04-23) here: ")
        umessage = input("enter the message you want the alarm to show here: ")
        uhour = int(input("Enter the hour here(in 24 hour clock time): "))
        uminute = int(input("Enter the minute here: "))
        uweek = None

        # the stucture of the log is made
        utime = f"{uhour}:{uminute}|{umessage}|{udate}|{uweek},"

        # then we open the file and the log
        with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_log.txt", "r") as reading: # ---------------------
            content = reading.read()  # opening the file and readng it

        content = content + utime

        reading.close()

        # then we open the file and write the log
        with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_log.txt", "w") as writing: # ---------------------
            writing.write(content)

        writing.close()

    # this is our daily reminder the alram should ring everyday hence there is no need to remove these from the alarm_log
    elif user_options == 3:

        umessage = input("enter the message you want the alarm to show here: ")
        uhour = int(input("Enter the hour here(in 24 hour clock time): "))
        uminute = int(input("Enter the minute here: "))
        udate = None
        uweek = None

        # the stucture of the log is made
        utime = f"{uhour}:{uminute}|{umessage}|{udate}|{uweek},"

        # then we open the file and the log
        with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_log.txt", "r") as reading: # ---------------------
            content = reading.read()  # opening the file and readng it

        content = content + utime

        reading.close()

        # then we open the file and write the log
        with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_log.txt", "w") as writing: # ---------------------
            writing.write(content)

        writing.close()

    elif user_options == 4:

        umessage = input("enter the message you want the alarm to show here: ")
        uhour = int(input("Enter the hour here(in 24 hour clock time): "))
        uminute = int(input("Enter the minute here: "))
        udate = None
        uweek = input("Enter the weekday on which you want the alarm to ring every week\nIMP ENTER 0 FOR MODAY\nIMP ENTER 1 FOR TUESDAY\nIMP ENTER 2 FOR WEDNUSDAY\nIMP ENTER 3 FOR THURSDAY\nIMP ENTER 4 FOR FRIDAY\nIMP ENTER 5 FOR SATURDAY\nIMP ENTER 6 FOR SUNDAY here: \n")

        # the stucture of the log is made
        utime = f"{uhour}:{uminute}|{umessage}|{udate}|{uweek},"

        # then we open the file and the log
        with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_log.txt", "r") as reading: # ---------------------
            content = reading.read()  # opening the file and readng it

        content = content + utime

        reading.close()

        # then we open the file and write the log
        with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_log.txt", "w") as writing: # ---------------------
            writing.write(content)

    else:
        print("Please enter a valid value 1, 2, 3, 4 and restart the program. ")
        quit()

elif ui == "2":

    print("\nThe active alarms at the moment are as follows: \n")

    with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_log.txt", "r") as reading: # ---------------------
        content = reading.read()  # opening the file and readng it
        alarm_list = content.split(",")

    for j in range(len(alarm_list)):
        print(f"{j+1}. {alarm_list[j]}")

    reading.close()

elif ui == "3":

    # opening the alarm_log and reading it
    print("\nhere is a list of the active alarms: \n")

    with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_log.txt", "r") as reading: # ---------------------
        content = reading.read()  # opening the file and readng it
        alarm_list = content.split(",")

    for j in range(len(alarm_list)):
        print(f"{j+1}. {alarm_list[j]}")

    # taking the log from the user
    ualarm = input(
        "please copy-paste the alarm you wanna remove from the above list example(17:32|quick|2022-04-24|None) here: ")

    # removing it
    for k in alarm_list:
        if k == ualarm:
            alarm_list.remove(k)

    reading.close()

    joined_list = ",".join(alarm_list)

    # then we open the file and write the log
    with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_log.txt", "w") as writing: # ---------------------
        writing.write(joined_list)

    writing.close()

elif ui == "4":

    print("\nHere is a list of all the alrams that have rung. \n")

    with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_rung.txt", "r") as reading: # ---------------------
        content = reading.read()
        log_list = content.split(".")

    for t in log_list:
        print(t)

# this is the alarm part:

with open("F:\\aryans_code_notes\\python_language\\python_projects\\alarm_clock\\alarm_log.txt", "r") as f: # ---------------------
    content = f.read()
    alarm_list = content.split(",")
    alarm_list = alarm_list[0:len(alarm_list)-1]

print("\n---------------------------------------------------------------------------------------------------------\n")
print("\t\tTHE ALARM IS RUNNING NOW MINIZE IT.\nIf YOU WANT TO DO ANOTHER OPERTAION LIKE DELETE ALARM OR VIEW ALARMS CLOSE THIS WINDOW AND RUN PROGRAM AGAIN")
print("\n---------------------------------------------------------------------------------------------------------\n")
while True:

    # this is a for else loop the else run only if the loop runs through all the iteration and never breaks.
    for i in alarm_list:

        time_meassage_date = i.split("|")
        custom_week = time_meassage_date[-1]
        custom_date = time_meassage_date[2]
        custom_message = time_meassage_date[1]
        hour_and_minute = time_meassage_date[0].split(":")
        alarm_hour = hour_and_minute[0]
        alarm_min = hour_and_minute[1]

        # for debugging and seeinghow the program works
        # print(time_meassage_date)
        # print()

        notify_user(alarm_hour, alarm_min, custom_message,
                    custom_date, custom_week)
    else:
        time.sleep(10)
