from fastapi import FastAPI
import pyodbc
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS settings to allow requests from your front end
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define connection string
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=127.0.0.1;"
    "DATABASE=PhelieuDatabase;"
    "UID=sa;"
    "PWD=123;"
    "TrustServerCertificate=yes;"
)

@app.get("/data")
async def get_data():
    conn = None
    cursor = None
    try:
        # Connect to SQL Server
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Call stored procedure
        cursor.execute("{CALL selectdata}")

        # Fetch results
        rows = cursor.fetchall()

        # Convert results to list of dicts
        data = []
        columns = [column[0] for column in cursor.description]
        for row in rows:
            row_data = {columns[i]: row[i] for i in range(len(columns))}
            data.append(row_data)

        return jsonable_encoder(data)

    except pyodbc.Error as ex:
        # Handle errors
        return {"error": str(ex)}
    finally:
        # Close connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()
#uvicorn selectdata:app --host 127.0.0.1 --port 1234/data
