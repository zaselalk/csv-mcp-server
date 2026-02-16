import csv
import uuid
from pathlib import Path
from fastmcp import FastMCP

mcp = FastMCP("File Server")
File = Path(__file__).parent / "data.csv"

def _ensure():
    if not File.exists():
        File.write_text("id,name,qty\n",encoding="utf-8")

@mcp.tool()
def add_item(name: str, qty: int) -> str:
    _ensure()
    item_id = str(uuid.uuid4())
    with File.open("a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([item_id, name, qty])
    return item_id

@mcp.tool()
def get_item(item_id: str) -> dict:
    _ensure()
    with File.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["id"] == item_id:
                return {"id": row["id"], "name": row["name"], "qty": int(row["qty"])}
    return {}

@mcp.tool()
def read_all_items() -> list:
    _ensure()
    items = []
    with File.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append({"id": row["id"], "name": row["name"], "qty": int(row["qty"])})
    return items

if __name__ == "__main__":
    mcp.run()





