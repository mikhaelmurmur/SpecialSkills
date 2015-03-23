__author__ = 'lord'
from spyre import server


import cherrypy

#region
Regions = [0 for x in range(25)]
Regions[0]=24
Regions[1]=25
Regions[2]=5
Regions[3]=6
Regions[4]=27
Regions[5]=23
Regions[6]=26
Regions[7]=7
Regions[8]=11
Regions[9]=13
Regions[10]=14
Regions[11]=15
Regions[12]=16
Regions[13]=17
Regions[14]=18
Regions[15]=19
Regions[16]=21
Regions[17]=22
Regions[18]=8
Regions[19]=9
Regions[20]=10
Regions[21]=1
Regions[22]=3
Regions[23]=2
Regions[24]=4





import pandas as pd, os
import urllib2
import json
import numpy as np
from matplotlib import pyplot as plt

# # region Description
# def downloadcsv(region_number):
#         import  urllib2
#         if Regions[region_number-1]>9:
#             url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R"+ str(Regions[region_number-1])+".txt"
#         else:
#             url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R0"+ str(Regions[region_number-1])+".txt"
#         vhi_url = urllib2.urlopen(url)
#         out = open(str(region_number)+'.csv', 'wb')
#         out.write(vhi_url.read())
#         out.close()
# # endregion



def get_y_axis(region, name,year,start_week,finish_week):
        df = pd.read_csv(str(region)+'.csv',index_col=False, header=1)
        if(name=="vhi"):
            result= df.vhi[df['Year']==year & df['Week']>=start_week & df['Week']<=finish_week].tolist()
        else:
            if(name=="vci"):
                result= df.vci[df['Year']==year & df['Week']>=start_week & df['Week']<=finish_week].tolist()
            else:
                result= df.tci[df['Year']==year & df['Week']>=start_week & df['Week']<=finish_week].tolist()

        return result


class StockExample(server.App):
    title = "Indexes"

    inputs = [{
                  "input_type":'dropdown',
                    "label": 'Indexes',
                    "options" : [ {"label": "VHI", "value":"VHI"},
                                  {"label": "VCI", "value":"VCI"},
                                  {"label": "TCI", "value":"TCI"}],
                    "variable_name": 'indexes',
                    "action_id": "plot"
              },
        {
          "input_type": 'slider',
          "label":'Year',
          "min":1981,
          "max":2015,
          "value":1981,
          "variable_name":'year',
          "action_id": "plot"
        },
        {
          "input_type": 'slider',
          "label":'Start week',
          "min":1,
          "max":52,
          "value":1,
          "variable_name":'start_week',
          "action_id": "plot"
        },
        {
          "input_type": 'slider',
          "label":'Finish week',
          "min":1,
          "max":52,
          "value":52,
          "variable_name":'finish_week',
          "action_id": "plot"
        },
        {
            "input_type":'dropdown',
                    "label": 'Region',
                    "options" : [ {"label": "Vinnica", "value":1},
                                  {"label": "Volin", "value":2},
                                  {"label": "Dipropetrovsk", "value":3},
                                  {"label": "Donetsk", "value":4},
                                  {"label": "Jitomir", "value":5},
                                  {"label": "Zakarpatya", "value":6},
                                  {"label": "Zaporizhia", "value":7},
                                  {"label": "Ivano-Frankivsk", "value":8},
                                  {"label": "Kyiv", "value":9},
                                  {"label": "Kirovograd", "value":10},
                                  {"label": "Lugansk", "value":11},
                                  {"label": "Lviv", "value":12},
                                  {"label": "Mykolaiv", "value":13},
                                  {"label": "Odessa", "value":14},
                                  {"label": "Poltava", "value":15},
                                  {"label": "Rivne", "value":16},
                                  {"label": "Sumy", "value":17},
                                  {"label": "Ternopil", "value":18},
                                  {"label": "Kharkiv", "value":19},
                                  {"label": "Kherson", "value":20},
                                  {"label": "Hmelnickii", "value":21},
                                  {"label": "Cherkassy", "value":22},
                                  {"label": "Chernivci", "value":23},
                                  {"label": "Chernigiv", "value":24},
                                  {"label": "Crymia", "value":25}],
                    "variable_name": 'region_number',
                    "action_id": "plot"

        }]

    tabs = ["Plot", "Table"]


    outputs = [{    "output_type" : "plot",
                    "output_id" : "plot",
                    "tab": "Plot",
                    "control_id":"plot",
                    "on_page_load" : True },
             {"output_type": "table",
              "output_id": "table_id",
              "control_id": "update_data",
              "tab": "Table",
              "on_page_load": True}]

    def getData(self, params):
        province=int(params['region_number'])
        year=int(params['year'])
        week_min=int(params['start_week'])
        week_max=int(params['finish_week'])
        self.time_series=params['indexes']
        df = pd.read_csv(str(province)+".csv", index_col=False, header=1)
        df = df[df['year']==year]
        df=df[df['week'] >= week_min]
        df=df[df['week'] <= week_max]
        #df=df[df['week', self.time_series]]
        return df

    def getPlot(self, params):
        df=self.getData(params)
        plt_obj=df.set_index('week').plot()
        plt_obj.set_title(self.time_series)
        fig = plt_obj.get_figure()
        return fig



app = StockExample()

cherrypy.config.update({'server.socket_host': '0.0.0.0'})


app.launch(port=9943)