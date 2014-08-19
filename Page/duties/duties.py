#! /usr/bin/python
import csv
import pickle
import datetime


########################################
# classes
########################################

class Guy(object):
    """one guy for queue"""
    def __init__(self, line):
        sLine = line.split(',')
        self.name = sLine[0].strip()

        self.absence = []
        # whole week absence (marked by X)
        if len(sLine) > 1 and sLine[1].strip() != '':
            if sLine[1].strip() == 'x' or sLine[1].strip() == 'X':
                for index in range(5):
                    absence = datetime.datetime.today()+datetime.timedelta(days=index)
                    absence = absence.replace(hour = 0, minute=0, second=0, microsecond=0)
                    self.absence.append(absence)

            # specified days of absence
            else:
                for index in range(1,len(sLine)):
                    param = sLine[index].strip()

                    param = param+'.'+(str(datetime.datetime.today().year))

                    absence = datetime.datetime.strptime(param, '%d.%m.%Y')
                    self.absence.append(absence)

    def next5days(self):
        today = datetime.datetime.today()
        today = today.replace(hour = 0, minute=0, second=0, microsecond=0)

        next5DaysAv = []
        for day in range(5):
            curDay = today+datetime.timedelta(days=day)
            verdict = True
            for ab in self.absence:
                if curDay == ab:
                    verdict = False
            next5DaysAv.append(verdict)

        self.next5DaysAv = next5DaysAv
        return self.next5DaysAv

    def canHaveDuty(self, index):
        outList = self.next5days()
        return outList[index]

    def nbrOfPossibleDaysTillEndOfWeek(self, index):
        outList = self.next5days()

        nbrOfDays = 0
        for i in range(index+1, 5):
            if outList[i]:
                nbrOfDays += 1
        return nbrOfDays

    def __str__(self):
        text = self.name + ':  '
        for ab in self.absence:
            text = text + str(ab) + ' '
        return text

    def __repr__(self):
        return self.name

########################################
# functions
########################################

def makeARandom(listOfGuys):
    """return list of guys in order of duties"""
    from random import choice
    import sys

    today = datetime.datetime.today()
    today = today.replace(hour = 0, minute=0, second=0, microsecond=0)
    takenGuys = []

    duties = []

    for day in range(5):
        curDay = today+datetime.timedelta(days=day)

        possibleGuys = []
        for guy in listOfGuys:
            if guy.canHaveDuty(day) == True:
                possibleGuys.append(guy)

        if len(possibleGuys) == 0:
            sys.exit(str(curDay)+ ': nobody can have a duty!')

        zeroDaysLeft = []
        for guy in possibleGuys:
            if guy.nbrOfPossibleDaysTillEndOfWeek(day) == 0:
                zeroDaysLeft.append(guy)

        guysForRand = []
        if len(zeroDaysLeft) == 0:
            for guy in possibleGuys:
                if guy in duties:
                    pass
                else:
                    guysForRand.append(guy)
        else:
            for guy in zeroDaysLeft:
                if guy in duties:
                    pass
                else:
                    guysForRand.append(guy)

        if len(guysForRand) > 0:
            duties.append(choice(guysForRand))
        else:
            possibleBackupGuys = []
            for guy in listOfGuys:
                if guy.canHaveDuty(day) == True:
                    possibleBackupGuys.append(guy)
            duties.append(choice(possibleBackupGuys))
    return duties

def duties():
    listOfPresence = 'names.csv'
    listOfGuys = []
    f = open(listOfPresence, 'r')
    for line in f:
        listOfGuys.append(Guy(line))
    f.close()
    duties = makeARandom(listOfGuys)
    return duties


if __name__ == "__main__":

    picked_guys = duties()
    picked_guys = [repr(name) for name in picked_guys]
    pickle.dump(picked_guys, open('choiced_names.pickle', 'w'))


