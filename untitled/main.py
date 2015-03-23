__author__ = 'lord'
import  urllib2
import time
import pandas as pd

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





def downloadcsv(region_number):
    import  urllib2
    if Regions[region_number-1]>9:
        url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R"+ str(Regions[region_number-1])+".txt"
    else:
       url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R0"+ str(Regions[region_number-1])+".txt"
    vhi_url = urllib2.urlopen(url)
    out = open('vhi_id_'+str(region_number)+'_'+time.strftime("%d_%m_%Y") +'_'+ time.strftime("%H_%M_%S") +'.csv', 'wb')
    out.write(vhi_url.read())
    out.close()
    print "VHI is downloaded..."





def download_frame(name):
    df = pd.read_csv(name,index_col=False, header=1)
    print list(df.columns.values)
    print max(list(df['VHI']))








def vhi_moreless(name):
    df = pd.read_csv(name,index_col=False, header=1)
    vhi_less= set(df.year[df['VHI']<35].tolist())
    vhi_more = set(df.year[df['VHI']>85].tolist())
    print set(vhi_less).intersection(vhi_more)


# region Description
def downloadcsv(region_number):
        import  urllib2
        if Regions[region_number-1]>9:
            url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R"+ str(Regions[region_number-1])+".txt"
        else:
            url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R0"+ str(Regions[region_number-1])+".txt"
        vhi_url = urllib2.urlopen(url)
        out = open(str(region_number)+'.csv', 'wb')
        out.write(vhi_url.read())
        out.close()
# endregion

for i in range(1,25):
    downloadcsv(i)


vhi_moreless("vhi_id_1_22_02_2015_06_37_48.csv")
vhi_moreless("vhi_id_2_22_02_2015_06_37_49.csv")
vhi_moreless("vhi_id_3_22_02_2015_06_37_50.csv")
vhi_moreless("vhi_id_4_22_02_2015_06_37_50.csv")
vhi_moreless("vhi_id_5_22_02_2015_06_37_51.csv")
vhi_moreless("vhi_id_6_22_02_2015_06_37_52.csv")
vhi_moreless("vhi_id_7_22_02_2015_06_37_52.csv")
vhi_moreless("vhi_id_8_22_02_2015_06_37_53.csv")
vhi_moreless("vhi_id_9_22_02_2015_06_37_54.csv")
vhi_moreless("vhi_id_10_22_02_2015_06_37_55.csv")
vhi_moreless("vhi_id_11_22_02_2015_06_37_55.csv")
vhi_moreless("vhi_id_12_22_02_2015_06_37_56.csv")
vhi_moreless("vhi_id_13_22_02_2015_06_37_57.csv")
vhi_moreless("vhi_id_14_22_02_2015_06_37_58.csv")
vhi_moreless("vhi_id_15_22_02_2015_06_37_58.csv")
vhi_moreless("vhi_id_16_22_02_2015_06_37_59.csv")
vhi_moreless("vhi_id_17_22_02_2015_06_38_00.csv")
vhi_moreless("vhi_id_18_22_02_2015_06_38_00.csv")
vhi_moreless("vhi_id_19_22_02_2015_06_38_01.csv")
vhi_moreless("vhi_id_20_22_02_2015_06_38_02.csv")
vhi_moreless("vhi_id_21_22_02_2015_06_38_03.csv")
vhi_moreless("vhi_id_22_22_02_2015_06_38_03.csv")
vhi_moreless("vhi_id_23_22_02_2015_06_38_04.csv")
vhi_moreless("vhi_id_24_22_02_2015_06_38_05.csv")