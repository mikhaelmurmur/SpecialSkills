__author__ = 'lord'



import cherrypy
import pandas as pd, os
from spyre import server
from matplotlib import pyplot as plt
class FirstApp(server.App):
    title="Application"
    inputs=[{"input_type":'dropdown',
             "label":'Select time series',
             "options":[{"label": "VHI", "value":"VHI"},
                        {"label": "TCI", "value":"TCI"},
                        {"label": "VCI", "value":"VCI"}],
             "variable_name": 'time_series',
             "action_id": "update_data"},
            {"input_type":'dropdown',
             "label":'Select province',
             "options":[{"label": "Vinnytsya", "value":"1"},
                        {"label": "Volyn", "value":"2"},
                        {"label": "Dnipropetrovs'k", "value":"3"},
                        {"label": "Donets'k", "value":"4"},
                        {"label": "Zhytomyr", "value":"5"},
                        {"label": "Transcarpathia", "value":"6"},
                        {"label": "Zaporizhzhya", "value":"7"},
                        {"label": "Ivano-Frankivs'k", "value":"8"},
                        {"label": "Kiev", "value":"9"},
                        {"label": "Kirovohrad", "value":"10"},
                        {"label": "Luhans'k", "value":"11"},
                        {"label": "L'viv", "value":"12"},
                        {"label": "Mykolayiv", "value":"13"},
                        {"label": "Odessa", "value":"14"},
                        {"label": "Poltava", "value":"15"},
                        {"label": "Rivne", "value":"16"},
                        {"label": "Sumy", "value":"17"},
                        {"label": "Ternopil'", "value":"18"},
                        {"label": "Kharkiv", "value":"19"},
                        {"label": "Kherson", "value":"20"},
                        {"label": "Khmel'nyts'kyy", "value":"21"},
                        {"label": "Cherkasy", "value":"22"},
                        {"label": "Chernivtsi", "value":"23"},
                        {"label": "Chernihiv", "value":"24"},
                        {"label": "Crimea", "value":"25"},
                        {"label": "Kiev City", "value":"26"},
                        {"label": "Sevastopol'", "value":"27"}],
            "variable_name": 'province',
            "action_id": "update_data"},
           {"input_type": 'text',
            "label": 'Week from',
            "value": 1,
            "variable_name": 'week_min',
            "action_id": "update_data"},
           {"input_type": 'text',
            "label": 'Week to',
            "value": 52,
            "variable_name": 'week_max',
            "action_id": "update_data"},
           {"input_type": 'text',
            "label": 'Year',
            "value": 1981,
            "variable_name": 'year',
            "action_id": "update_data"}]

    controls=[{"control_type": "button",
               "label": "Update",
               "control_id": "update_data"}]

    tabs = ["Plot", "Table"]

    outputs=[{"output_type": "plot",
              "output_id": "plot",
              "control_id": "update_data",
              "tab": "Plot",
              "on_page_load": True},
             {"output_type": "table",
              "output_id": "table_id",
              "control_id": "update_data",
              "tab": "Table",
              "on_page_load": True}]

    def getData(self, params):
        province=int(params['province'])
        year=int(params['year'])
        week_min=int(params['week_min'])
        week_max=int(params['week_max'])
        self.time_series=params['time_series']
        os.chdir("/home/yana/lab_1/clean_data/")
        cwd=os.getcwd()
        frames=[]
        filelist=os.listdir(cwd)
        filelist.sort()
        for files in filelist:
            frames.append(pd.read_csv(files, index_col=False, header=0))
        df=frames[province][frames[province]['year'] == year]
        df=df[df['week'] >= week_min]
        df=df[df['week'] <= week_max]
        df=df[['week', self.time_series]]
        return df

    def getPlot(self, params):
        df=self.getData(params)
        plt_obj=dfh.set_index('Week').plot()
        plt_obj.set_title(self.time_series)
        fig = plt_obj.get_figure()
        return fig

def main():
    app=FirstApp()

    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    app.launch()
if __name__ == '__main__':
    main()






