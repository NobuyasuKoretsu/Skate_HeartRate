import main
import fitbit
import pandas as pd
import numpy as np
import os
import sys
import all_join

DATE1 = "2019-11-01"
DATE2 = "2019-11-02"
DATE3 = "2019-11-03"
DATE4 = "2019-11-04"
DATE5 = "2019-11-05"
DATE6 = "2019-11-06"
DATE7 = "2019-11-07"
DATE8 = "2019-11-08"
DATE9 = "2019-11-09"
DATE10 = "2019-11-10"
DATE11 = "2019-11-11"
DATE12 = "2019-11-12"
DATE13 = "2019-11-13"
DATE14 = "2019-11-14"
DATE15 = "2019-11-15"
DATE16 = "2019-11-16"
DATE17 = "2019-11-17"
DATE18 = "2019-11-18"
DATE19 = "2019-11-19"
DATE20 = "2019-11-20"
DATE21 = "2019-11-21"
DATE22 = "2019-11-22"
DATE23 = "2019-11-23"
DATE24 = "2019-11-24"
DATE25 = "2019-11-25"
DATE26 = "2019-11-26"
DATE27 = "2019-11-27"
DATE28 = "2019-11-28"
DATE29 = "2019-11-29"
DATE30 = "2019-11-30"

def Get_November(authd_client):
    # 心拍数を取得（1秒単位）
    # 1日
    data_sec1 = authd_client.intraday_time_series('activities/heart', DATE1, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec1 = data_sec1["activities-heart-intraday"]["dataset"]
    heart_df1 = pd.DataFrame.from_dict(heart_sec1)
    heart_df1.index = pd.to_datetime([DATE1 + " " + t for t in heart_df1.time])
    heart_df1.to_csv('November_1th.csv')

    # 2日
    data_sec2 = authd_client.intraday_time_series('activities/heart', DATE2, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec2 = data_sec2["activities-heart-intraday"]["dataset"]
    heart_df2 = pd.DataFrame.from_dict(heart_sec2)
    heart_df2.index = pd.to_datetime([DATE2 + " " + t for t in heart_df2.time])
    heart_df2.to_csv('November_2th.csv')

    # 3日
    data_sec3 = authd_client.intraday_time_series('activities/heart', DATE3, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec3 = data_sec3["activities-heart-intraday"]["dataset"]
    heart_df3 = pd.DataFrame.from_dict(heart_sec3)
    heart_df3.index = pd.to_datetime([DATE3 + " " + t for t in heart_df3.time])
    heart_df3.to_csv('November_3th.csv')

    # 4日
    data_sec4 = authd_client.intraday_time_series('activities/heart', DATE4, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec4 = data_sec4["activities-heart-intraday"]["dataset"]
    heart_df4 = pd.DataFrame.from_dict(heart_sec4)
    heart_df4.index = pd.to_datetime([DATE4 + " " + t for t in heart_df4.time])
    heart_df4.to_csv('November_4th.csv')

    # 5日
    data_sec5 = authd_client.intraday_time_series('activities/heart', DATE5, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec5 = data_sec5["activities-heart-intraday"]["dataset"]
    heart_df5 = pd.DataFrame.from_dict(heart_sec5)
    heart_df5.index = pd.to_datetime([DATE5 + " " + t for t in heart_df5.time])
    heart_df5.to_csv('November_5th.csv')

    # 6日
    data_sec6 = authd_client.intraday_time_series('activities/heart', DATE6, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec6 = data_sec6["activities-heart-intraday"]["dataset"]
    heart_df6 = pd.DataFrame.from_dict(heart_sec6)
    heart_df6.index = pd.to_datetime([DATE6 + " " + t for t in heart_df6.time])
    heart_df6.to_csv('November_6th.csv')

    # 7日
    data_sec7 = authd_client.intraday_time_series('activities/heart', DATE7, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec7 = data_sec7["activities-heart-intraday"]["dataset"]
    heart_df7 = pd.DataFrame.from_dict(heart_sec7)
    heart_df7.index = pd.to_datetime([DATE7 + " " + t for t in heart_df7.time])
    heart_df7.to_csv('November_7th.csv')

    # 8日
    data_sec8 = authd_client.intraday_time_series('activities/heart', DATE8, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec8 = data_sec8["activities-heart-intraday"]["dataset"]
    heart_df8 = pd.DataFrame.from_dict(heart_sec8)
    heart_df8.index = pd.to_datetime([DATE8 + " " + t for t in heart_df8.time])
    heart_df8.to_csv('November_8th.csv')

    # 9日
    data_sec9 = authd_client.intraday_time_series('activities/heart', DATE9, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec9 = data_sec9["activities-heart-intraday"]["dataset"]
    heart_df9 = pd.DataFrame.from_dict(heart_sec9)
    heart_df9.index = pd.to_datetime([DATE9 + " " + t for t in heart_df9.time])
    heart_df9.to_csv('November_9th.csv')

    # 10日
    data_sec10 = authd_client.intraday_time_series('activities/heart', DATE10, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec10 = data_sec10["activities-heart-intraday"]["dataset"]
    heart_df10 = pd.DataFrame.from_dict(heart_sec10)
    heart_df10.index = pd.to_datetime([DATE10 + " " + t for t in heart_df10.time])
    heart_df10.to_csv('November_10th.csv')

    # 11日
    data_sec11 = authd_client.intraday_time_series('activities/heart', DATE11, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec11 = data_sec11["activities-heart-intraday"]["dataset"]
    heart_df11 = pd.DataFrame.from_dict(heart_sec11)
    heart_df11.index = pd.to_datetime([DATE11 + " " + t for t in heart_df11.time])
    heart_df11.to_csv('November_11th.csv')

    # 12日
    data_sec12 = authd_client.intraday_time_series('activities/heart', DATE12, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec12 = data_sec12["activities-heart-intraday"]["dataset"]
    heart_df12= pd.DataFrame.from_dict(heart_sec12)
    heart_df12.index = pd.to_datetime([DATE12 + " " + t for t in heart_df12.time])
    heart_df12.to_csv('November_12th.csv')

    # 13日
    data_sec13 = authd_client.intraday_time_series('activities/heart', DATE13, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec13 = data_sec13["activities-heart-intraday"]["dataset"]
    heart_df13 = pd.DataFrame.from_dict(heart_sec13)
    heart_df13.index = pd.to_datetime([DATE13 + " " + t for t in heart_df13.time])
    heart_df13.to_csv('November_13th.csv')

    # 14日
    data_sec14 = authd_client.intraday_time_series('activities/heart', DATE14, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec14 = data_sec14["activities-heart-intraday"]["dataset"]
    heart_df14 = pd.DataFrame.from_dict(heart_sec14)
    heart_df14.index = pd.to_datetime([DATE14 + " " + t for t in heart_df14.time])
    heart_df14.to_csv('November_14th.csv')

    # 15日
    data_sec15 = authd_client.intraday_time_series('activities/heart', DATE15, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec15 = data_sec15["activities-heart-intraday"]["dataset"]
    heart_df15 = pd.DataFrame.from_dict(heart_sec15)
    heart_df15.index = pd.to_datetime([DATE15 + " " + t for t in heart_df15.time])
    heart_df15.to_csv('November_15th.csv')

    # 16日
    data_sec16 = authd_client.intraday_time_series('activities/heart', DATE16, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec16 = data_sec16["activities-heart-intraday"]["dataset"]
    heart_df16 = pd.DataFrame.from_dict(heart_sec16)
    heart_df16.index = pd.to_datetime([DATE16 + " " + t for t in heart_df16.time])
    heart_df16.to_csv('November_16th.csv')

    # 17日
    data_sec17 = authd_client.intraday_time_series('activities/heart', DATE17, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec17 = data_sec17["activities-heart-intraday"]["dataset"]
    heart_df17 = pd.DataFrame.from_dict(heart_sec17)
    heart_df17.index = pd.to_datetime([DATE17 + " " + t for t in heart_df17.time])
    heart_df17.to_csv('November_17th.csv')

    # 18日
    data_sec18 = authd_client.intraday_time_series('activities/heart', DATE18, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec18 = data_sec18["activities-heart-intraday"]["dataset"]
    heart_df18 = pd.DataFrame.from_dict(heart_sec18)
    heart_df18.index = pd.to_datetime([DATE18 + " " + t for t in heart_df18.time])
    heart_df18.to_csv('November_18th.csv')

    # 19日
    data_sec19 = authd_client.intraday_time_series('activities/heart', DATE19, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec19 = data_sec19["activities-heart-intraday"]["dataset"]
    heart_df19 = pd.DataFrame.from_dict(heart_sec19)
    heart_df19.index = pd.to_datetime([DATE19 + " " + t for t in heart_df19.time])
    heart_df19.to_csv('November_19th.csv')

    # 20日
    data_sec20 = authd_client.intraday_time_series('activities/heart', DATE20, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec20 = data_sec20["activities-heart-intraday"]["dataset"]
    heart_df20 = pd.DataFrame.from_dict(heart_sec20)
    heart_df20.index = pd.to_datetime([DATE20 + " " + t for t in heart_df20.time])
    heart_df20.to_csv('November_20th.csv')

    # 21日
    data_sec21 = authd_client.intraday_time_series('activities/heart', DATE21, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec21 = data_sec21["activities-heart-intraday"]["dataset"]
    heart_df21 = pd.DataFrame.from_dict(heart_sec21)
    heart_df21.index = pd.to_datetime([DATE21 + " " + t for t in heart_df21.time])
    heart_df21.to_csv('November_21th.csv')

    # 22日
    data_sec22 = authd_client.intraday_time_series('activities/heart', DATE22, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec22 = data_sec22["activities-heart-intraday"]["dataset"]
    heart_df22 = pd.DataFrame.from_dict(heart_sec22)
    heart_df22.index = pd.to_datetime([DATE22 + " " + t for t in heart_df22.time])
    heart_df22.to_csv('November_22th.csv')

    # 23日
    data_sec23 = authd_client.intraday_time_series('activities/heart', DATE23, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec23 = data_sec23["activities-heart-intraday"]["dataset"]
    heart_df23 = pd.DataFrame.from_dict(heart_sec23)
    heart_df23.index = pd.to_datetime([DATE23 + " " + t for t in heart_df23.time])
    heart_df23.to_csv('November_23th.csv')

    # 24日
    data_sec24 = authd_client.intraday_time_series('activities/heart', DATE24, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec24 = data_sec24["activities-heart-intraday"]["dataset"]
    heart_df24 = pd.DataFrame.from_dict(heart_sec24)
    heart_df24.index = pd.to_datetime([DATE24 + " " + t for t in heart_df24.time])
    heart_df24.to_csv('November_24th.csv')

    # 25日
    data_sec25 = authd_client.intraday_time_series('activities/heart', DATE25, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec25 = data_sec25["activities-heart-intraday"]["dataset"]
    heart_df25 = pd.DataFrame.from_dict(heart_sec25)
    heart_df25.index = pd.to_datetime([DATE25 + " " + t for t in heart_df25.time])
    heart_df25.to_csv('November_25th.csv')

    # 26日
    data_sec26 = authd_client.intraday_time_series('activities/heart', DATE26, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec26 = data_sec26["activities-heart-intraday"]["dataset"]
    heart_df26 = pd.DataFrame.from_dict(heart_sec26)
    heart_df26.index = pd.to_datetime([DATE26 + " " + t for t in heart_df26.time])
    heart_df26.to_csv('November_26th.csv')

    # 27日
    data_sec27 = authd_client.intraday_time_series('activities/heart', DATE27, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec27 = data_sec27["activities-heart-intraday"]["dataset"]
    heart_df27 = pd.DataFrame.from_dict(heart_sec27)
    heart_df27.index = pd.to_datetime([DATE27 + " " + t for t in heart_df27.time])
    heart_df27.to_csv('November_27th.csv')

    # 28日
    data_sec28 = authd_client.intraday_time_series('activities/heart', DATE28, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec28 = data_sec28["activities-heart-intraday"]["dataset"]
    heart_df28 = pd.DataFrame.from_dict(heart_sec28)
    heart_df28.index = pd.to_datetime([DATE28 + " " + t for t in heart_df28.time])
    heart_df28.to_csv('November_28th.csv')

    # 29日
    data_sec29 = authd_client.intraday_time_series('activities/heart', DATE29, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec29 = data_sec29["activities-heart-intraday"]["dataset"]
    heart_df29 = pd.DataFrame.from_dict(heart_sec29)
    heart_df29.index = pd.to_datetime([DATE29 + " " + t for t in heart_df29.time])
    heart_df29.to_csv('November_29th.csv')

    # 30日
    data_sec30 = authd_client.intraday_time_series('activities/heart', DATE30, detail_level='1sec') #'1sec', '1min', or '15min'
    heart_sec30 = data_sec30["activities-heart-intraday"]["dataset"]
    heart_df30 = pd.DataFrame.from_dict(heart_sec30)
    heart_df30.index = pd.to_datetime([DATE30 + " " + t for t in heart_df30.time])
    heart_df30.to_csv('November_30th.csv')

    all_join.November()