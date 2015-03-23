__author__ = 'lord'


# coding: utf-8

# In[5]:

import urllib2, datetime, sys, pandas as pd, os
def download(id):
    now_time=datetime.datetime.now()
    curr=now_time.strftime("%d.%m.%Y_%I:%M:%S_%p")
    url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R{:02d}.txt".format(id)
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    req = urllib2.Request(url, headers=hdr)
    vhi_url = urllib2.urlopen(req)
    out = open('vhi_id_{:02d}_{}.csv'.format(id,curr),'wb')
    out.write(vhi_url.read())
    out.close()
    sys.stdout.write("|")
def inframe(cwd):
    df=[]
    filelist=os.listdir(cwd)
    filelist.sort()
    for files in filelist:
        df.append(pd.read_csv(files, index_col=False, header=1))
    return df
def sort(frames):
    temp=[23,24,4,5,26,22,25,6,10,12,13,14,15,16,17,18,20,21,7,8,9,0,2,1,3,11,19]
    sortframes=[]
    for i in temp:
        sortframes.append(frames[i])
    return sortframes
def cleaning(frames):
    for i in range(27):
        frames[i]=frames[i][frames[i]['%Area_VHI_LESS_35'] != -1]
        frames[i].to_csv('vhi_id_{:02d}.csv'.format(i+1), index=False, float_format="%.4f")
    return frames
def download_all():
    id=1
    while id<28:
        download(id)
        id+=1
    print(" Download complete")
def VHI_min_max(year,id,frames):
    os.chdir("/home/yana/lab_1/VHI")
    df=frames[id-1][frames[id-1]['year'] == year]
    df=df.drop(['SMN', 'SMT','VCI','TCI','%Area_VHI_LESS_15','%Area_VHI_LESS_35'],1)
    df.to_csv('vhi_for_{}_year_for_{:02d}_province.ods'.format(year,id), index=False)
    max_VHI=df['VHI'].max()
    min_VHI=df['VHI'].min()
    print 'max VHI for this province in {}: '.format(year),max_VHI
    print 'min VHI for this province in {}: '.format(year),min_VHI
def VHI_drought_except(perc,id,frames):
    os.chdir("/home/yana/lab_1/VHI/drought")
    df=frames[id-1]
    df=df.drop(['SMN', 'SMT', 'VCI', 'TCI'],1)
    print 'VHI for all years for {:02d} province'.format(id)
    print df['VHI']
    df=df[df['%Area_VHI_LESS_15'] > perc]
    df=df.drop(['%Area_VHI_LESS_15','%Area_VHI_LESS_35'],1)
    df.to_csv('years_of_exceptional_drought_for_{:02d}_province.csv'.format(id), index=False)
def VHI_drought_moderate(perc,id,frames):
    os.chdir("/home/yana/lab_1/VHI/drought")
    df=frames[id-1]
    df=df.drop(['SMN', 'SMT', 'VCI', 'TCI'],1)
    print 'VHI for all years for {:02d} province'.format(id)
    print df['VHI']
    df=df[df['%Area_VHI_LESS_35'] > perc]
    df=df.drop(['%Area_VHI_LESS_15','%Area_VHI_LESS_35'],1)
    df.to_csv('years_of_moderate_drought_for_{:02d}_province.csv'.format(id), index=False)
def first_valid():
    region=0
    year=0
    while int(region)<1 or int(region)>27:
        region=raw_input("Input id of province: ")
        if not 1<=int(region)<=27:
            print "Invalid id! Right input: 0<id<28. Try again"
    while int(year)<1981 or int(year)>2015:
        year=raw_input("Input year: ")
        if not 1981<=int(year)<=2015:
            print "Invalid year! Right input: 1980<year<2016. Try again"
    return int(year),int(region)
def second_valid():
    perc=0.0
    region=0
    while int(region)<1 or int(region)>27:
        region=raw_input("Input id of province: ")
        if not 1<=int(region)<=27:
            print "Invalid id! Right input: 0<id<28. Try again"
    while float(perc)<=0.00 or float(perc)>100.00:
        perc=raw_input("Input percent of area: ")
        if not 0.00<=float(perc)<=100.00:
            print "Invalid percent! Right input: 0.00<percent<100.00. Try again"
    return float(perc),int(region)

def main():
    os.chdir("/home/yana/lab_1/raw_data")
    cwd=os.getcwd()
    download_all()
    frames=inframe(cwd)
    frames=sort(frames)
    os.chdir("/home/yana/lab_1/clean_data")
    frames=cleaning(frames)
    year,region=first_valid()
    VHI_min_max(year,region,frames)
    perc,region=second_valid()
    VHI_drought_except(perc,region,frames)
    perc,region=second_valid()
    VHI_drought_moderate(perc,region,frames)


if __name__ == '__main__':
    main()


# In[ ]:



