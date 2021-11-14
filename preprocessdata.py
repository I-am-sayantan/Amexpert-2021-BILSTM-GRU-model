import pandas as pd
import numpy as np
import re

def processB1(x,b,train,test):
  ans=[]
  rows=[]
  regex = re.compile('[^a-zA-Z0-9,]')
  for i in x:
      y=regex.sub('', i).split(',')
      row=[]
      if 'P00' in y:
          row.append(1)
      else:
          row.append(0)
      for z in range(1,22):
          if 'P'+str(z) in y:
              row.append(1)
          else:
              row.append(0)
      rows.append(row)
      ans.append(y)
  ans=np.array(ans)
  rows=np.array(rows)
  if b=='train':
      c=0
      for row in rows:
          train['P00']=row[0]
          for i in range(1,22):
              train['P'+str(i)]=row[i]
          c=c+1   

      c=0
      for row in rows:
          train['P00'][c]=row[0]
          for i in range(1,22):
              train['P'+str(i)][c]=row[i]
          c=c+1
  else:
      c=0
      for row in rows:
          test['P00']=row[0]
          for i in range(1,22):
              test['P'+str(i)]=row[i]
          c=c+1   

      c=0
      for row in rows:
          test['P00'][c]=row[0]
          for i in range(1,22):
              test['P'+str(i)][c]=row[i]
          c=c+1

def processB2(x,train):
    ans=[]
    rows=[]
    regex = re.compile('[^a-zA-Z0-9,]')
    for i in x:
        y=regex.sub('', i).split(',')
        row=[]
        if 'P00' in y:
            row.append(1)
        else:
            row.append(0)
        for z in range(1,22):
            if 'P'+str(z) in y:
                row.append(1)
            else:
                row.append(0)
        rows.append(row)
        ans.append(y)
    ans=np.array(ans)
    rows=np.array(rows)

    c=0
    for row in rows:
        train['P00_T']=row[0]
        for i in range(1,22):
            train['P'+str(i)+'_T']=row[i]
        c=c+1   

    c=0
    for row in rows:
        train['P00_T'][c]=row[0]
        for i in range(1,22):
            train['P'+str(i)+'_T'][c]=row[i]
        c=c+1

def submission(sub,th,LIST,pred1,pred20):
  pred2=LIST[0]
  pred3=LIST[1]
  pred4=LIST[2]
  pred5=LIST[3]
  pred6=LIST[4]
  pred7=LIST[5]
  pred8=LIST[6]
  pred9=LIST[7]
  pred10=LIST[8]
  pred11=LIST[9]
  pred12=LIST[10]
  pred13=LIST[11]
  pred14=LIST[12]
  pred15=LIST[13]
  pred16=LIST[14]
  pred17=LIST[15]
  pred18=LIST[16]
  pred19=LIST[17]
  pred=[]
  pred.append(pred1)
  pred.append(pred2)
  pred.append(pred3)
  pred.append(pred4)
  pred.append(pred5)
  pred.append(pred6)
  pred.append(pred7)
  pred.append(pred8)
  pred.append(pred9)
  pred.append(pred10)
  pred.append(pred11)
  pred.append(pred12)
  pred.append(pred13)
  pred.append(pred14)
  pred.append(pred15)
  pred.append(pred16)
  pred.append(pred17)
  pred.append(pred18)
  pred.append(pred19)
  pred.append(pred20)
  pred=np.array(pred)
  final=[]
  for i in range(20327):
      f=[]
      m=0
      index=-1
      for j in range(20):
          if pred[j][i][0][0]>m:
              m=pred[j][i][0][0]
              index=j
          if pred[j][i][0][0]>=th:
              f.append([pred[j][i][0][0],j])
      if len(f)==0:
          final.append([index])
      else:
          if len(f)==1:
              final.append([f[0][1]])
          elif len(f)==2:
              final.append([f[0][1],f[1][1]])
          else:
              sorted(f)
              final.append([f[0][1],f[1][1],f[2][1]])
  convert={}
  convert[0]='P00'
  for i in range(1,20):
      convert[i]='P'+str(i)
  convert[19]='P20'

  final_last=[]
  for x in final:
      s='['
      for y in x:
          s+='\''+convert[y]+'\''+','
      s=s[:-1]    
      s+=']'
      final_last.append(s)

  sub['Product_Holding_B2']=final_last
  sub.to_csv("submission"+str(th)+".csv",index=False)
  print(sub,th)