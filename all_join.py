import fitbit
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib



def January():
    heart_df1 = pd.read_csv("./January/January_1th.csv")
    heart_df2 = pd.read_csv("./January/January_2th.csv")
    heart_df3 = pd.read_csv("./January/January_3th.csv")
    heart_df4 = pd.read_csv("./January/January_4th.csv")
    heart_df5 = pd.read_csv("./January/January_5th.csv")
    heart_df6 = pd.read_csv("./January/January_6th.csv")
    heart_df7 = pd.read_csv("./January/January_7th.csv")
    heart_df8 = pd.read_csv("./January/January_8th.csv")
    heart_df9 = pd.read_csv("./January/January_9th.csv")
    heart_df10 = pd.read_csv("./January/January_10th.csv")
    heart_df11 = pd.read_csv("./January/January_11th.csv")
    heart_df12 = pd.read_csv("./January/January_12th.csv")
    heart_df13 = pd.read_csv("./January/January_13th.csv")
    heart_df14 = pd.read_csv("./January/January_14th.csv")
    heart_df15 = pd.read_csv("./January/January_15th.csv")
    heart_df16 = pd.read_csv("./January/January_16th.csv")
    heart_df17 = pd.read_csv("./January/January_17th.csv")
    heart_df18 = pd.read_csv("./January/January_18th.csv")
    heart_df19 = pd.read_csv("./January/January_19th.csv")
    heart_df20 = pd.read_csv("./January/January_20th.csv")
    heart_df21 = pd.read_csv("./January/January_21th.csv")
    heart_df22 = pd.read_csv("./January/January_22th.csv")
    heart_df23 = pd.read_csv("./January/January_23th.csv")
    heart_df24 = pd.read_csv("./January/January_24th.csv")
    heart_df25 = pd.read_csv("./January/January_25th.csv")
    heart_df26 = pd.read_csv("./January/January_26th.csv")
    heart_df27 = pd.read_csv("./January/January_27th.csv")
    heart_df28 = pd.read_csv("./January/January_28th.csv")
    heart_df29 = pd.read_csv("./January/January_29th.csv")
    heart_df30 = pd.read_csv("./January/January_30th.csv")
    heart_df31 = pd.read_csv("./January/January_31th.csv")

    all_df = pd.concat([heart_df1, heart_df2, heart_df3, heart_df4, heart_df5, heart_df6,heart_df7, heart_df8, heart_df9,heart_df10,heart_df11, heart_df12, heart_df13, heart_df14, heart_df15, heart_df16,heart_df17, heart_df18, heart_df9,heart_df20,heart_df21, heart_df22, heart_df23, heart_df24, heart_df25, heart_df26,heart_df27, heart_df28, heart_df29,heart_df30,heart_df31])
    all_df.to_csv("January.csv")

def February():
    heart_df1 = pd.read_csv("February_1th.csv")
    heart_df2 = pd.read_csv("February_2th.csv")
    heart_df3 = pd.read_csv("February_3th.csv")
    heart_df4 = pd.read_csv("February_4th.csv")
    heart_df5 = pd.read_csv("February_5th.csv")
    heart_df6 = pd.read_csv("February_6th.csv")
    heart_df7 = pd.read_csv("February_7th.csv")
    heart_df8 = pd.read_csv("February_8th.csv")
    heart_df9 = pd.read_csv("February_9th.csv")
    heart_df10 = pd.read_csv("February_10th.csv")
    heart_df11 = pd.read_csv("February_11th.csv")
    heart_df12 = pd.read_csv("February_12th.csv")
    heart_df13 = pd.read_csv("February_13th.csv")
    heart_df14 = pd.read_csv("February_14th.csv")
    heart_df15 = pd.read_csv("February_15th.csv")
    heart_df16 = pd.read_csv("February_16th.csv")
    heart_df17 = pd.read_csv("February_17th.csv")
    heart_df18 = pd.read_csv("February_18th.csv")
    heart_df19 = pd.read_csv("February_19th.csv")
    heart_df20 = pd.read_csv("February_20th.csv")
    heart_df21 = pd.read_csv("February_21th.csv")
    heart_df22 = pd.read_csv("February_22th.csv")
    heart_df23 = pd.read_csv("February_23th.csv")
    heart_df24 = pd.read_csv("February_24th.csv")
    heart_df25 = pd.read_csv("February_25th.csv")
    heart_df26 = pd.read_csv("February_26th.csv")
    heart_df27 = pd.read_csv("February_27th.csv")
    heart_df28 = pd.read_csv("February_28th.csv")
    

    all_df = pd.concat([heart_df1, heart_df2, heart_df3, heart_df4, heart_df5, heart_df6,heart_df7, heart_df8, heart_df9,heart_df10,heart_df11, heart_df12, heart_df13, heart_df14, heart_df15, heart_df16,heart_df17, heart_df18, heart_df9,heart_df20,heart_df21, heart_df22, heart_df23, heart_df24, heart_df25, heart_df26,heart_df27, heart_df28])
    all_df.to_csv("February.csv")

def March():
    heart_df1 = pd.read_csv("March_1th.csv")
    heart_df2 = pd.read_csv("March_2th.csv")
    heart_df3 = pd.read_csv("March_3th.csv")
    heart_df4 = pd.read_csv("March_4th.csv")
    heart_df5 = pd.read_csv("March_5th.csv")
    heart_df6 = pd.read_csv("March_6th.csv")
    heart_df7 = pd.read_csv("March_7th.csv")
    heart_df8 = pd.read_csv("March_8th.csv")
    heart_df9 = pd.read_csv("March_9th.csv")
    heart_df10 = pd.read_csv("March_10th.csv")
    heart_df11 = pd.read_csv("March_11th.csv")
    heart_df12 = pd.read_csv("March_12th.csv")
    heart_df13 = pd.read_csv("March_13th.csv")
    heart_df14 = pd.read_csv("March_14th.csv")
    heart_df15 = pd.read_csv("March_15th.csv")
    heart_df16 = pd.read_csv("March_16th.csv")
    heart_df17 = pd.read_csv("March_17th.csv")
    heart_df18 = pd.read_csv("March_18th.csv")
    heart_df19 = pd.read_csv("March_19th.csv")
    heart_df20 = pd.read_csv("March_20th.csv")
    heart_df21 = pd.read_csv("March_21th.csv")
    heart_df22 = pd.read_csv("March_22th.csv")
    heart_df23 = pd.read_csv("March_23th.csv")
    heart_df24 = pd.read_csv("March_24th.csv")
    heart_df25 = pd.read_csv("March_25th.csv")
    heart_df26 = pd.read_csv("March_26th.csv")
    heart_df27 = pd.read_csv("March_27th.csv")
    heart_df28 = pd.read_csv("March_28th.csv")
    heart_df29 = pd.read_csv("March_29th.csv")
    heart_df30 = pd.read_csv("March_30th.csv")
    heart_df31 = pd.read_csv("March_31th.csv")

    all_df = pd.concat([heart_df1, heart_df2, heart_df3, heart_df4, heart_df5, heart_df6,heart_df7, heart_df8, heart_df9,heart_df10,heart_df11, heart_df12, heart_df13, heart_df14, heart_df15, heart_df16,heart_df17, heart_df18, heart_df9,heart_df20,heart_df21, heart_df22, heart_df23, heart_df24, heart_df25, heart_df26,heart_df27, heart_df28, heart_df29,heart_df30,heart_df31])
    all_df.to_csv("March.csv")

def April():
    heart_df1 = pd.read_csv("April_1th.csv")
    heart_df2 = pd.read_csv("April_2th.csv")
    heart_df3 = pd.read_csv("April_3th.csv")
    heart_df4 = pd.read_csv("April_4th.csv")
    heart_df5 = pd.read_csv("April_5th.csv")
    heart_df6 = pd.read_csv("April_6th.csv")
    heart_df7 = pd.read_csv("April_7th.csv")
    heart_df8 = pd.read_csv("April_8th.csv")
    heart_df9 = pd.read_csv("April_9th.csv")
    heart_df10 = pd.read_csv("April_10th.csv")
    heart_df11 = pd.read_csv("April_11th.csv")
    heart_df12 = pd.read_csv("April_12th.csv")
    heart_df13 = pd.read_csv("April_13th.csv")
    heart_df14 = pd.read_csv("April_14th.csv")
    heart_df15 = pd.read_csv("April_15th.csv")
    heart_df16 = pd.read_csv("April_16th.csv")
    heart_df17 = pd.read_csv("April_17th.csv")
    heart_df18 = pd.read_csv("April_18th.csv")
    heart_df19 = pd.read_csv("April_19th.csv")
    heart_df20 = pd.read_csv("April_20th.csv")
    heart_df21 = pd.read_csv("April_21th.csv")
    heart_df22 = pd.read_csv("April_22th.csv")
    heart_df23 = pd.read_csv("April_23th.csv")
    heart_df24 = pd.read_csv("April_24th.csv")
    heart_df25 = pd.read_csv("April_25th.csv")
    heart_df26 = pd.read_csv("April_26th.csv")
    heart_df27 = pd.read_csv("April_27th.csv")
    heart_df28 = pd.read_csv("April_28th.csv")
    heart_df29 = pd.read_csv("April_29th.csv")
    heart_df30 = pd.read_csv("April_30th.csv")

    all_df = pd.concat([heart_df1, heart_df2, heart_df3, heart_df4, heart_df5, heart_df6,heart_df7, heart_df8, heart_df9,heart_df10,heart_df11, heart_df12, heart_df13, heart_df14, heart_df15, heart_df16,heart_df17, heart_df18, heart_df9,heart_df20,heart_df21, heart_df22, heart_df23, heart_df24, heart_df25, heart_df26,heart_df27, heart_df28, heart_df29,heart_df30])
    all_df.to_csv("April.csv")

def May():
    heart_df1 = pd.read_csv("May_1th.csv")
    heart_df2 = pd.read_csv("May_2th.csv")
    heart_df3 = pd.read_csv("May_3th.csv")
    heart_df4 = pd.read_csv("May_4th.csv")
    heart_df5 = pd.read_csv("May_5th.csv")
    heart_df6 = pd.read_csv("May_6th.csv")
    heart_df7 = pd.read_csv("May_7th.csv")
    heart_df8 = pd.read_csv("May_8th.csv")
    heart_df9 = pd.read_csv("May_9th.csv")
    heart_df10 = pd.read_csv("May_10th.csv")
    heart_df11 = pd.read_csv("May_11th.csv")
    heart_df12 = pd.read_csv("May_12th.csv")
    heart_df13 = pd.read_csv("May_13th.csv")
    heart_df14 = pd.read_csv("May_14th.csv")
    heart_df15 = pd.read_csv("May_15th.csv")
    heart_df16 = pd.read_csv("May_16th.csv")
    heart_df17 = pd.read_csv("May_17th.csv")
    heart_df18 = pd.read_csv("May_18th.csv")
    heart_df19 = pd.read_csv("May_19th.csv")
    heart_df20 = pd.read_csv("May_20th.csv")
    heart_df21 = pd.read_csv("May_21th.csv")
    heart_df22 = pd.read_csv("May_22th.csv")
    heart_df23 = pd.read_csv("May_23th.csv")
    heart_df24 = pd.read_csv("May_24th.csv")
    heart_df25 = pd.read_csv("May_25th.csv")
    heart_df26 = pd.read_csv("May_26th.csv")
    heart_df27 = pd.read_csv("May_27th.csv")
    heart_df28 = pd.read_csv("May_28th.csv")
    heart_df29 = pd.read_csv("May_29th.csv")
    heart_df30 = pd.read_csv("May_30th.csv")
    heart_df31 = pd.read_csv("May_31th.csv")

    all_df = pd.concat([heart_df1, heart_df2, heart_df3, heart_df4, heart_df5, heart_df6,heart_df7, heart_df8, heart_df9,heart_df10,heart_df11, heart_df12, heart_df13, heart_df14, heart_df15, heart_df16,heart_df17, heart_df18, heart_df9,heart_df20,heart_df21, heart_df22, heart_df23, heart_df24, heart_df25, heart_df26,heart_df27, heart_df28, heart_df29,heart_df30,heart_df31])
    all_df.to_csv("May.csv")

def June():
    heart_df1 = pd.read_csv("June_1th.csv")
    heart_df2 = pd.read_csv("June_2th.csv")
    heart_df3 = pd.read_csv("June_3th.csv")
    heart_df4 = pd.read_csv("June_4th.csv")
    heart_df5 = pd.read_csv("June_5th.csv")
    heart_df6 = pd.read_csv("June_6th.csv")
    heart_df7 = pd.read_csv("June_7th.csv")
    heart_df8 = pd.read_csv("June_8th.csv")
    heart_df9 = pd.read_csv("June_9th.csv")
    heart_df10 = pd.read_csv("June_10th.csv")
    heart_df11 = pd.read_csv("June_11th.csv")
    heart_df12 = pd.read_csv("June_12th.csv")
    heart_df13 = pd.read_csv("June_13th.csv")
    heart_df14 = pd.read_csv("June_14th.csv")
    heart_df15 = pd.read_csv("June_15th.csv")
    heart_df16 = pd.read_csv("June_16th.csv")
    heart_df17 = pd.read_csv("June_17th.csv")
    heart_df18 = pd.read_csv("June_18th.csv")
    heart_df19 = pd.read_csv("June_19th.csv")
    heart_df20 = pd.read_csv("June_20th.csv")
    heart_df21 = pd.read_csv("June_21th.csv")
    heart_df22 = pd.read_csv("June_22th.csv")
    heart_df23 = pd.read_csv("June_23th.csv")
    heart_df24 = pd.read_csv("June_24th.csv")
    heart_df25 = pd.read_csv("June_25th.csv")
    heart_df26 = pd.read_csv("June_26th.csv")
    heart_df27 = pd.read_csv("June_27th.csv")
    heart_df28 = pd.read_csv("June_28th.csv")
    heart_df29 = pd.read_csv("June_29th.csv")
    heart_df30 = pd.read_csv("June_30th.csv")

    all_df = pd.concat([heart_df1, heart_df2, heart_df3, heart_df4, heart_df5, heart_df6,heart_df7, heart_df8, heart_df9,heart_df10,heart_df11, heart_df12, heart_df13, heart_df14, heart_df15, heart_df16,heart_df17, heart_df18, heart_df9,heart_df20,heart_df21, heart_df22, heart_df23, heart_df24, heart_df25, heart_df26,heart_df27, heart_df28, heart_df29,heart_df30])
    all_df.to_csv("June.csv")

def July():
    heart_df1 = pd.read_csv("July_1th.csv")
    heart_df2 = pd.read_csv("July_2th.csv")
    heart_df3 = pd.read_csv("July_3th.csv")
    heart_df4 = pd.read_csv("July_4th.csv")
    heart_df5 = pd.read_csv("July_5th.csv")
    heart_df6 = pd.read_csv("July_6th.csv")
    heart_df7 = pd.read_csv("July_7th.csv")
    heart_df8 = pd.read_csv("July_8th.csv")
    heart_df9 = pd.read_csv("July_9th.csv")
    heart_df10 = pd.read_csv("July_10th.csv")
    heart_df11 = pd.read_csv("July_11th.csv")
    heart_df12 = pd.read_csv("July_12th.csv")
    heart_df13 = pd.read_csv("July_13th.csv")
    heart_df14 = pd.read_csv("July_14th.csv")
    heart_df15 = pd.read_csv("July_15th.csv")
    heart_df16 = pd.read_csv("July_16th.csv")
    heart_df17 = pd.read_csv("July_17th.csv")
    heart_df18 = pd.read_csv("July_18th.csv")
    heart_df19 = pd.read_csv("July_19th.csv")
    heart_df20 = pd.read_csv("July_20th.csv")
    heart_df21 = pd.read_csv("July_21th.csv")
    heart_df22 = pd.read_csv("July_22th.csv")
    heart_df23 = pd.read_csv("July_23th.csv")
    heart_df24 = pd.read_csv("July_24th.csv")
    heart_df25 = pd.read_csv("July_25th.csv")
    heart_df26 = pd.read_csv("July_26th.csv")
    heart_df27 = pd.read_csv("July_27th.csv")
    heart_df28 = pd.read_csv("July_28th.csv")
    heart_df29 = pd.read_csv("July_29th.csv")
    heart_df30 = pd.read_csv("July_30th.csv")
    heart_df31 = pd.read_csv("July_31th.csv")

    all_df = pd.concat([heart_df1, heart_df2, heart_df3, heart_df4, heart_df5, heart_df6,heart_df7, heart_df8, heart_df9,heart_df10,heart_df11, heart_df12, heart_df13, heart_df14, heart_df15, heart_df16,heart_df17, heart_df18, heart_df9,heart_df20,heart_df21, heart_df22, heart_df23, heart_df24, heart_df25, heart_df26,heart_df27, heart_df28, heart_df29,heart_df30,heart_df31])
    all_df.to_csv("July.csv")

def August():
    heart_df1 = pd.read_csv("August_1th.csv")
    heart_df2 = pd.read_csv("August_2th.csv")
    heart_df3 = pd.read_csv("August_3th.csv")
    heart_df4 = pd.read_csv("August_4th.csv")
    heart_df5 = pd.read_csv("August_5th.csv")
    heart_df6 = pd.read_csv("August_6th.csv")
    heart_df7 = pd.read_csv("August_7th.csv")
    heart_df8 = pd.read_csv("August_8th.csv")
    heart_df9 = pd.read_csv("August_9th.csv")
    heart_df10 = pd.read_csv("August_10th.csv")
    heart_df11 = pd.read_csv("August_11th.csv")
    heart_df12 = pd.read_csv("August_12th.csv")
    heart_df13 = pd.read_csv("August_13th.csv")
    heart_df14 = pd.read_csv("August_14th.csv")
    heart_df15 = pd.read_csv("August_15th.csv")
    heart_df16 = pd.read_csv("August_16th.csv")
    heart_df17 = pd.read_csv("August_17th.csv")
    heart_df18 = pd.read_csv("August_18th.csv")
    heart_df19 = pd.read_csv("August_19th.csv")
    heart_df20 = pd.read_csv("August_20th.csv")
    heart_df21 = pd.read_csv("August_21th.csv")
    heart_df22 = pd.read_csv("August_22th.csv")
    heart_df23 = pd.read_csv("August_23th.csv")
    heart_df24 = pd.read_csv("August_24th.csv")
    heart_df25 = pd.read_csv("August_25th.csv")
    heart_df26 = pd.read_csv("August_26th.csv")
    heart_df27 = pd.read_csv("August_27th.csv")
    heart_df28 = pd.read_csv("August_28th.csv")
    heart_df29 = pd.read_csv("August_29th.csv")
    heart_df30 = pd.read_csv("August_30th.csv")
    heart_df31 = pd.read_csv("August_31th.csv")

    all_df = pd.concat([heart_df1, heart_df2, heart_df3, heart_df4, heart_df5, heart_df6,heart_df7, heart_df8, heart_df9,heart_df10,heart_df11, heart_df12, heart_df13, heart_df14, heart_df15, heart_df16,heart_df17, heart_df18, heart_df9,heart_df20,heart_df21, heart_df22, heart_df23, heart_df24, heart_df25, heart_df26,heart_df27, heart_df28, heart_df29,heart_df30,heart_df31])
    all_df.to_csv("August.csv")

def September():
    heart_df1 = pd.read_csv("September_1th.csv")
    heart_df2 = pd.read_csv("September_2th.csv")
    heart_df3 = pd.read_csv("September_3th.csv")
    heart_df4 = pd.read_csv("September_4th.csv")
    heart_df5 = pd.read_csv("September_5th.csv")
    heart_df6 = pd.read_csv("September_6th.csv")
    heart_df7 = pd.read_csv("September_7th.csv")
    heart_df8 = pd.read_csv("September_8th.csv")
    heart_df9 = pd.read_csv("September_9th.csv")
    heart_df10 = pd.read_csv("September_10th.csv")
    heart_df11 = pd.read_csv("September_11th.csv")
    heart_df12 = pd.read_csv("September_12th.csv")
    heart_df13 = pd.read_csv("September_13th.csv")
    heart_df14 = pd.read_csv("September_14th.csv")
    heart_df15 = pd.read_csv("September_15th.csv")
    heart_df16 = pd.read_csv("September_16th.csv")
    heart_df17 = pd.read_csv("September_17th.csv")
    heart_df18 = pd.read_csv("September_18th.csv")
    heart_df19 = pd.read_csv("September_19th.csv")
    heart_df20 = pd.read_csv("September_20th.csv")
    heart_df21 = pd.read_csv("September_21th.csv")
    heart_df22 = pd.read_csv("September_22th.csv")
    heart_df23 = pd.read_csv("September_23th.csv")
    heart_df24 = pd.read_csv("September_24th.csv")
    heart_df25 = pd.read_csv("September_25th.csv")
    heart_df26 = pd.read_csv("September_26th.csv")
    heart_df27 = pd.read_csv("September_27th.csv")
    heart_df28 = pd.read_csv("September_28th.csv")
    heart_df29 = pd.read_csv("September_29th.csv")
    heart_df30 = pd.read_csv("September_30th.csv")

    all_df = pd.concat([heart_df1, heart_df2, heart_df3, heart_df4, heart_df5, heart_df6,heart_df7, heart_df8, heart_df9,heart_df10,heart_df11, heart_df12, heart_df13, heart_df14, heart_df15, heart_df16,heart_df17, heart_df18, heart_df9,heart_df20,heart_df21, heart_df22, heart_df23, heart_df24, heart_df25, heart_df26,heart_df27, heart_df28, heart_df29,heart_df30])
    all_df.to_csv("September.csv")

def October():
    heart_df1 = pd.read_csv("October_1th.csv")
    heart_df2 = pd.read_csv("October_2th.csv")
    heart_df3 = pd.read_csv("October_3th.csv")
    heart_df4 = pd.read_csv("October_4th.csv")
    heart_df5 = pd.read_csv("October_5th.csv")
    heart_df6 = pd.read_csv("October_6th.csv")
    heart_df7 = pd.read_csv("October_7th.csv")
    heart_df8 = pd.read_csv("October_8th.csv")
    heart_df9 = pd.read_csv("October_9th.csv")
    heart_df10 = pd.read_csv("October_10th.csv")
    heart_df11 = pd.read_csv("October_11th.csv")
    heart_df12 = pd.read_csv("October_12th.csv")
    heart_df13 = pd.read_csv("October_13th.csv")
    heart_df14 = pd.read_csv("October_14th.csv")
    heart_df15 = pd.read_csv("October_15th.csv")
    heart_df16 = pd.read_csv("October_16th.csv")
    heart_df17 = pd.read_csv("October_17th.csv")
    heart_df18 = pd.read_csv("October_18th.csv")
    heart_df19 = pd.read_csv("October_19th.csv")
    heart_df20 = pd.read_csv("October_20th.csv")
    heart_df21 = pd.read_csv("October_21th.csv")
    heart_df22 = pd.read_csv("October_22th.csv")
    heart_df23 = pd.read_csv("October_23th.csv")
    heart_df24 = pd.read_csv("October_24th.csv")
    heart_df25 = pd.read_csv("October_25th.csv")
    heart_df26 = pd.read_csv("October_26th.csv")
    heart_df27 = pd.read_csv("October_27th.csv")
    heart_df28 = pd.read_csv("October_28th.csv")
    heart_df29 = pd.read_csv("October_29th.csv")
    heart_df30 = pd.read_csv("October_30th.csv")
    heart_df31 = pd.read_csv("October_31th.csv")

    all_df = pd.concat([heart_df1, heart_df2, heart_df3, heart_df4, heart_df5, heart_df6,heart_df7, heart_df8, heart_df9,heart_df10,heart_df11, heart_df12, heart_df13, heart_df14, heart_df15, heart_df16,heart_df17, heart_df18, heart_df9,heart_df20,heart_df21, heart_df22, heart_df23, heart_df24, heart_df25, heart_df26,heart_df27, heart_df28, heart_df29,heart_df30,heart_df31])
    all_df.to_csv("October.csv")

def November():
    heart_df1 = pd.read_csv("November_1th.csv")
    heart_df2 = pd.read_csv("November_2th.csv")
    heart_df3 = pd.read_csv("November_3th.csv")
    heart_df4 = pd.read_csv("November_4th.csv")
    heart_df5 = pd.read_csv("November_5th.csv")
    heart_df6 = pd.read_csv("November_6th.csv")
    heart_df7 = pd.read_csv("November_7th.csv")
    heart_df8 = pd.read_csv("November_8th.csv")
    heart_df9 = pd.read_csv("November_9th.csv")
    heart_df10 = pd.read_csv("November_10th.csv")
    heart_df11 = pd.read_csv("November_11th.csv")
    heart_df12 = pd.read_csv("November_12th.csv")
    heart_df13 = pd.read_csv("November_13th.csv")
    heart_df14 = pd.read_csv("November_14th.csv")
    heart_df15 = pd.read_csv("November_15th.csv")
    heart_df16 = pd.read_csv("November_16th.csv")
    heart_df17 = pd.read_csv("November_17th.csv")
    heart_df18 = pd.read_csv("November_18th.csv")
    heart_df19 = pd.read_csv("November_19th.csv")
    heart_df20 = pd.read_csv("November_20th.csv")
    heart_df21 = pd.read_csv("November_21th.csv")
    heart_df22 = pd.read_csv("November_22th.csv")
    heart_df23 = pd.read_csv("November_23th.csv")
    heart_df24 = pd.read_csv("November_24th.csv")
    heart_df25 = pd.read_csv("November_25th.csv")
    heart_df26 = pd.read_csv("November_26th.csv")
    heart_df27 = pd.read_csv("November_27th.csv")
    heart_df28 = pd.read_csv("November_28th.csv")
    heart_df29 = pd.read_csv("November_29th.csv")
    heart_df30 = pd.read_csv("November_30th.csv")

    all_df = pd.concat([heart_df1, heart_df2, heart_df3, heart_df4, heart_df5, heart_df6,heart_df7, heart_df8, heart_df9,heart_df10,heart_df11, heart_df12, heart_df13, heart_df14, heart_df15, heart_df16,heart_df17, heart_df18, heart_df9,heart_df20,heart_df21, heart_df22, heart_df23, heart_df24, heart_df25, heart_df26,heart_df27, heart_df28, heart_df29,heart_df30])
    all_df.to_csv("November.csv")

def December():
    heart_df1 = pd.read_csv("December_1th.csv")
    heart_df2 = pd.read_csv("December_2th.csv")
    heart_df3 = pd.read_csv("December_3th.csv")
    heart_df4 = pd.read_csv("December_4th.csv")
    heart_df5 = pd.read_csv("December_5th.csv")
    heart_df6 = pd.read_csv("December_6th.csv")
    heart_df7 = pd.read_csv("December_7th.csv")
    heart_df8 = pd.read_csv("December_8th.csv")
    heart_df9 = pd.read_csv("December_9th.csv")
    heart_df10 = pd.read_csv("December_10th.csv")
    heart_df11 = pd.read_csv("December_11th.csv")
    heart_df12 = pd.read_csv("December_12th.csv")
    heart_df13 = pd.read_csv("December_13th.csv")
    heart_df14 = pd.read_csv("December_14th.csv")
    heart_df15 = pd.read_csv("December_15th.csv")
    heart_df16 = pd.read_csv("December_16th.csv")
    heart_df17 = pd.read_csv("December_17th.csv")
    heart_df18 = pd.read_csv("December_18th.csv")
    heart_df19 = pd.read_csv("December_19th.csv")
    heart_df20 = pd.read_csv("December_20th.csv")
    heart_df21 = pd.read_csv("December_21th.csv")
    heart_df22 = pd.read_csv("December_22th.csv")
    heart_df23 = pd.read_csv("December_23th.csv")
    heart_df24 = pd.read_csv("December_24th.csv")
    heart_df25 = pd.read_csv("December_25th.csv")
    heart_df26 = pd.read_csv("December_26th.csv")
    heart_df27 = pd.read_csv("December_27th.csv")
    heart_df28 = pd.read_csv("December_28th.csv")
    heart_df29 = pd.read_csv("December_29th.csv")
    heart_df30 = pd.read_csv("December_30th.csv")
    heart_df31 = pd.read_csv("December_31th.csv")

    all_df = pd.concat([heart_df1, heart_df2, heart_df3, heart_df4, heart_df5, heart_df6,heart_df7, heart_df8, heart_df9,heart_df10,heart_df11, heart_df12, heart_df13, heart_df14, heart_df15, heart_df16,heart_df17, heart_df18, heart_df9,heart_df20,heart_df21, heart_df22, heart_df23, heart_df24, heart_df25, heart_df26,heart_df27, heart_df28, heart_df29,heart_df30,heart_df31])
    all_df.to_csv("December.csv")