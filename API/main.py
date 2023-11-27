# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data.data import loadData
from data.mostUsedYear import getMostUsedYear
from data.totalReferences import getTotalReferences
from data.mostUsedReference import getMostUsedJournal
from data.mostUsedReference import getMostUsedEditorial
from data.histogramType import getTypeFrequency
app = FastAPI()
urlJSON = "https://raw.githubusercontent.com/byepesg/TransformaMetrics/main/src/data/JSON6.json"
# Configurar el middleware CORS para permitir todas las solicitudes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get-all-data")
async def mostrar_datos(url: str =urlJSON ):
    try:
        df = await loadData(url)
        return {"datos": df.to_dict(orient="records")}
    except ValueError as e:
        return {"error": str(e)}
    
@app.get("/most-used-year")
async def most_used_year(url: str = urlJSON):
    try:
        df = await loadData(url)
        return {"most_used_year": getMostUsedYear(df)}
    except ValueError as e:
        return {"error": str(e)}
    
@app.get("/total_references")
async def get_total_references(url: str = urlJSON):
    try:
        df = await loadData(url)
        return {"total_references": getTotalReferences(df)}
    except ValueError as e:
        return {"error": str(e)}
@app.get("/most_used_journal")
async def get_most_used_referencesl(url: str = urlJSON):
    try:
        df = await loadData(url)
        return {"most_used_journal": getMostUsedJournal(df),
                "most_used_editorial": getMostUsedEditorial(df)
                }
    except ValueError as e:
        return {"error": str(e)}  
@app.get("/histogram_data")      
async def get_type_years(url: str = urlJSON):
    try:
        df = await loadData(url)
        return {"Data": getTypeFrequency(df)}  
    except ValueError as e:
        return {"error": str(e)}         