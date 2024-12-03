from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/big/data/sorting")
def big_data_sorting():
    # 实现大数据分析排序, 要用到快速排序以及快速排序
    data = []
    return data
