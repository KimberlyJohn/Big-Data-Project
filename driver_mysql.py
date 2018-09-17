#!/usr/bin/python

import mysql.connector

cnx = mysql.connector.connect(user='scott', password='password',
                              host='127.0.0.1',
                              database='employees')
cnx.close()




        # Patient Information
        # Supported by MySQL

        elif query == '4':

            patient_id = input('Patient ID: ')

            if db == 'mongodb':
                patient = patients.find_one({ 'id' : patient_id })

                if patient is None:
                    print('Invalid patient ID. Not found in DB.')
                else:
                    print('Age:', patient['age'])
                    print('Gender:', patient['gender'])
                    print('Education:', patient['education'])
                    print('Diagnosis:', patient['diagnosis'])

            elif db == 'neo4j':
                patient = graph.find_one(label = 'Patient', property_key = 'id', property_value = patient_id)
                print('Age:', patient['age'])
                print('Gender:', patient['gender'])
                print('Education:', patient['education'])

        else:
            print('Pick query 1, 2, 3, or 4')

        print('-' * 10)
        db = input('Which db? ')
        query = input('Which query? ')

    print('bye...')


if __name__ == "__main__":
    main()
