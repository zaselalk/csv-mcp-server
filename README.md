# CSV MCP Server

A Model Context Protocol (MCP) server that provides tools for managing items in a CSV file. This server enables AI assistants and other MCP clients to perform CRUD operations on structured data stored in CSV format.

## Features

- **Add Items**: Create new items with a name and quantity
- **Retrieve Items**: Get item details by ID
- **List All Items**: Read all items from the CSV file
- **Auto-initialization**: Automatically creates the CSV file if it doesn't exist
- **UUID Generation**: Each item gets a unique identifier

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/zaselalk/csv-mcp-server.git
cd csv-mcp-server
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Server

Start the MCP server by running:

```bash
python mcp_server.py
```

The server will start and listen for MCP client connections.

### Available Tools

The server exposes three main tools through the MCP protocol:

#### 1. `add_item`

Adds a new item to the CSV file.

**Parameters:**
- `name` (string): The name of the item
- `qty` (int): The quantity of the item

**Returns:**
- `item_id` (string): The unique UUID assigned to the new item

**Example:**
```python
# Add a pen drive with quantity 5
item_id = add_item("pen drive", 5)
# Returns: "8713b031-dd68-431a-b107-191249601ad3"
```

#### 2. `get_item`

Retrieves an item by its ID.

**Parameters:**
- `item_id` (string): The unique identifier of the item

**Returns:**
- Dictionary containing:
  - `id` (string): Item ID
  - `name` (string): Item name
  - `qty` (int): Item quantity
- Empty dictionary `{}` if item not found

**Example:**
```python
# Get item details
item = get_item("8713b031-dd68-431a-b107-191249601ad3")
# Returns: {"id": "8713b031-dd68-431a-b107-191249601ad3", "name": "pen drive", "qty": 5}
```

#### 3. `read_all_items`

Retrieves all items from the CSV file.

**Parameters:**
- None

**Returns:**
- List of dictionaries, each containing:
  - `id` (string): Item ID
  - `name` (string): Item name
  - `qty` (int): Item quantity

**Example:**
```python
# Get all items
items = read_all_items()
# Returns: [
#   {"id": "8713b031-dd68-431a-b107-191249601ad3", "name": "pen drive", "qty": 5},
#   {"id": "53ef44f4-b687-4654-a1d6-0e13c8b09808", "name": "pencil", "qty": 1},
#   ...
# ]
```

## Data Storage

The server stores data in a CSV file named `data.csv` in the same directory as the server script. The CSV file has the following structure:

```csv
id,name,qty
8713b031-dd68-431a-b107-191249601ad3,Banana,2
8c071b04-97cf-45ed-8ff2-2369ea36bc21,Banana,2
53ef44f4-b687-4654-a1d6-0e13c8b09808,pencil,1
```

If the file doesn't exist when the server starts, it will be automatically created with the appropriate headers.

## Configuration

The server is configured to use:
- **Server Name**: "File Server"
- **Data File**: `data.csv` (in the same directory as `mcp_server.py`)
- **Encoding**: UTF-8

To change the data file location, modify the `File` variable in `mcp_server.py`:

```python
File = Path(__file__).parent / "data.csv"
```

## Technical Details

### Dependencies

This project uses [FastMCP](https://pypi.org/project/fastmcp/), a Python framework for building MCP servers. The main dependencies include:
- `fastmcp`: For building the MCP server
- Standard Python libraries: `csv`, `uuid`, `pathlib`

For a complete list of dependencies, see `requirements.txt`.

### Architecture

- **Framework**: Built on FastMCP
- **Data Format**: CSV with columns: id, name, qty
- **ID Generation**: UUIDs (Universally Unique Identifiers)
- **File Operations**: Synchronous file I/O with proper encoding

## Use Cases

This CSV MCP server can be used for:
- Simple inventory management
- Data collection and tracking
- Testing MCP client implementations
- Learning about MCP server development
- Prototyping data-driven applications

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## License

This project is open source. Please check the repository for license details.

## Links

- GitHub Repository: [https://github.com/zaselalk/csv-mcp-server](https://github.com/zaselalk/csv-mcp-server)
- Model Context Protocol: [https://modelcontextprotocol.io](https://modelcontextprotocol.io)

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.
