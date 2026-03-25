# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 21:36:25 2023

@author: kentang
"""

import sxtwl, re
import itertools

Gan, Zhi = list("甲乙丙丁戊己庚辛壬癸"),list("子丑寅卯辰巳午未申酉戌亥")

def jiazi():
    return list(map(lambda x: "{}{}".format(Gan[x % len(Gan)], Zhi[x % len(Zhi)]), list(range(60))))

def get_jiazi_code(jz):
    return dict(zip(jiazi(), [84,162,10,42,54,70,72,182,221,170,117,289,28,54,72,81,66,54,91,136,221,170,100,187,24,35,108,99,195,84,91,136,117,36,204,169,48,70,130,221,195,84,50,180,187,60,238,135,84,162,130,221,63,48,56,156,78,80,117,289])).get(jz)

def num_to_gua(num):
    return dict(zip(list(range(1,10))+[0], list("艮兌坎離震巽巽坤乾艮"))).get(num)
    

class Shenyishu():
    def __init__(self, year, month, day, hour):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
    
    def gangzhi(self):
        cdate = sxtwl.fromSolar(self.year, self.month, self.day)
        yTG = Gan[cdate.getYearGZ().tg] + Zhi[cdate.getYearGZ().dz]
        mTG = Gan[cdate.getMonthGZ().tg] + Zhi[cdate.getMonthGZ().dz]
        dTG  = Gan[cdate.getDayGZ().tg] + Zhi[cdate.getDayGZ().dz]
        hTG = Gan[cdate.getHourGZ(self.hour).tg] + Zhi[cdate.getHourGZ(self.hour).dz]
        return [yTG, mTG, dTG, hTG]
    
    def ymd_total(self):
        y = get_jiazi_code(self.gangzhi()[0])
        m = get_jiazi_code(self.gangzhi()[1])
        d = get_jiazi_code(self.gangzhi()[2])
        h = get_jiazi_code(self.gangzhi()[3])
        return y + m + d + h
    
    def get_gua(self):
        num = str(self.ymd_total())
        gua = [num_to_gua(i) for i in num]
        return 
    
    
if __name__ == '__main__':
    print(Shenyishu(2023,7,4,22).ymd_total())
