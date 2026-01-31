import pandas as pd


music = pd.DataFrame({
    "Age": ["20","23","25","26","28","30","31","33","35","20","23","25","26","28","30","31","33","35"],
    "Gender": [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
    "Genre" : ["HipHop","HipHop","HipHop","Pop","Pop","Pop","Classical","Classical","Classical","Dance","Dance","Dance","RnB","RnB","RnB","classical","classical","classical"]
})

music = music.set_index('Age')

music.to_csv(r'C:\Users\hp\Desktop\data_analysis\music.csv')  #"C:\Users\hp\Desktop\data_analysis"

print(music)