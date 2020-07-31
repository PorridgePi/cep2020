def openCSV(filename):
    file = open(filename, 'r')

    fileList = []
    for line in file:
        line = line[:-1]
        fileList.append(line.split(','))

    file.close

    return fileList


def dupList(origList):
    result = []
    for i in origList:
        result.append(i)
    return result


def printList(l):
    for i in l:
        print(i)


def getSchool(fileList, schoolType='all'):
    fileList = dupList(fileList)
    fileList.pop(0)
    schools = []
    for i in fileList:
        if i[0] not in schools:
            if schoolType == 'all':
                schools.append(i[0])
            elif schoolType == 'primary' and i[1] == 'PRIMARY':
                schools.append(i[0])
            elif schoolType == 'secondary' and i[1] == 'SECONDARY':
                schools.append(i[0])
            elif schoolType == 'jc' and i[1] == 'JUNIOR COLLEGE':
                schools.append(i[0])
    return schools


def searchSchool(fileList, query, schoolType='all'):
    schools = getSchool(fileList, schoolType)
    result = []
    for i in schools:
        if query.upper() in i:
            result.append(i)
    if schoolType == 'primary' or schoolType == 'secondary':
        schoolType = schoolType.upper()
    elif schoolType == 'jc':
        schoolType = 'JUNIOR COLLEGE'
    return [result, schoolType]


def getCCA(fileList, schools, generic=True, getNumber=False):
    result = []
    for school in schools[0]:
        cca = [school, []]
        for i in fileList:
            if i[0] == school and i[1] == schools[1]:
                if generic:
                    cca[1].append(i[3])
                else:
                    if i[4] != 'na':
                        cca[1].append(i[4])
                    else:
                        cca[1].append(i[3])
            elif i[0] == school and schools[1] == 'all':
                if generic:
                    cca[1].append(i[3])
                else:
                    if i[4] != 'na':
                        cca[1].append(i[4])
                    else:
                        cca[1].append(i[3])
        if getNumber:
            cca[1] = len(cca[1])
        result.append(cca)

    return dict(result)


def findCCA(fileList, schools, ccaName, detailed=False, getNumber=False):
    result = []
    for i in fileList:
        if i[0] in schools[0]:
            if ccaName.upper() in i[4]:
                if detailed:
                    result.append([i[0], i[4]])
                else:
                    result.append([i[0]])
            elif ccaName.upper() in i[3]:
                if detailed:
                    result.append([i[0], i[3]])
                else:
                    result.append([i[0]])
    if getNumber:
        return len(result)
    else:
        return result


def main():
    exit = False
    while not exit:
        functions = '''\nFunctions:
(1) Get CCA(s) of school(s)
(2) Find which school(s) have specified CCA
(-1) to exit
    '''
        fileList = openCSV('co-curricular-activities-ccas.csv')

        function = input(functions+'\nWhich function would you want to use?\n>>> ')
        if function == '-1':
            exit = True
            break
        while function not in ['1', '2']:
            function = input('Please only enter 1 or 2! Which function would you want to use?\n>>> ')
            if function == '-1':
                exit = True
                break

        if function == '1':
            schoolType = input('Do you want to restrict the results to a certain level of education? [All/Primary/Secondary/JC]\n>>> ').lower()
            while schoolType not in ['jc', 'secondary', 'primary', 'all']:
                schoolType = input('Please only enter All, Primary, Secondary or JC!\n>>> ').lower()
            if schoolType.lower() == 'all':
                print('''\nNOTE:
When there are schools of the same name but have two or more different levels, the CCAs of both levels are listed as one school.
This causes duplicated CCAs.
For example, Raffles Institution includes both Secondary and JC, so the CCAs of both Secondary and JC are listed as one school.
As of now, there is no easy fix for this.\n''')
            schools = input('Please enter a name to be searched for.\n>>> ')
            schools = searchSchool(fileList, schools, schoolType)
            while schools[0] == []:
                print('No school found.')
                schools = input('Please enter a school to be searched for.\n>>> ')
                schools = searchSchool(fileList, schools, schoolType)
            confirm = input('\nYou are retrieving the CCA(s) of the following schools:\n'+', '.join(schools[0])+'\n\nConfirm? [y/n] ')
            while confirm not in ['y', 'n']:
                confirm = input('Please only enter y or n!\n>>> ')
            if confirm == 'n':
                continue
            generic = input("\nWould you like the school-specific CCA name? [y/n]\n>>> ")
            while generic not in ['y', 'n']:
                generic = input('Please only enter y or n!\n>>> ')
            if generic == 'y':
                generic = False
            else:
                generic = True
            ccas = getCCA(fileList, schools, generic)

            for school in ccas:
                print('\n'+school+' has the following CCA(s):')
                for i in ccas[school]:
                    print('\t'+i)

        elif function == '2':
            schoolType = input('Do you want to restrict the results to a certain level of education? [All/Primary/Secondary/JC]\n>>> ').lower()
            while schoolType not in ['jc', 'secondary', 'primary', 'all']:
                schoolType = input('Please only enter All, Primary, Secondary or JC!\n>>> ').lower()
            cca = input('Please enter a CCA to be searched for.\n>>> ')
            schools = searchSchool(fileList, '', schoolType)

            detailed = input("Would you like the exact CCA name? [y/n]\n>>> ")
            while detailed not in ['y', 'n']:
                detailed = input('Please only enter y or n!\n>>> ')
            if detailed == 'y':
                detailed = True
            else:
                detailed = False

            schools = findCCA(fileList, schools, cca, detailed)
            if schools == []:
                print("No CCA found.")
            else:
                print('\nThe following schools have the CCA "'+cca+'":')
                for school in schools:
                    print('  '+school[0])
                    print('\t'+school[1])


if __name__ == "__main__":
    main()
