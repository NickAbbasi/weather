def writing_results(file_list):

    import pandas as pd
    from sqlalchemy import create_engine
    from datetime import date
    file = open('..\pw.txt')
    pw = str(file.readline())
    file.close()
    #list = ['..\\ADW20210101.csv', '..\\ADW20210102.csv']
    list = file_list
    x = 0
    for l in list:
        print(list[x])
        data = pd.read_csv(list[x])

        data['ImportDate'] = date.today()

        engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                           .format(user="nick",
                                   pw=pw,
                                   db="weather_data"))

        #print(data)
        data.to_sql('raw_import_hourly', con = engine, if_exists = 'append',index = False ,chunksize = 1000)
        x+=1
#cnx = mysql.connector.connect(**config)

#writing_results()
#cnx.close()
