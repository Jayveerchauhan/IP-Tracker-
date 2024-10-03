
# IPTracer
A GUI-based OSINT tool which is a bulk IP info extraction tool that fetches detailed information for a list of IP addresses. It utilizes the IP2Location database to provide accurate data. The tool is developed using Python and Tkinter for the graphical user interface.


## Features

- Fetch details such as country, region, city, latitude, longitude, ZIP code, and time zone for given IP addresses.
- Upload a text file containing multiple IP addresses.
- Save the IP details to a CSV file.
- Simple and intuitive GUI built with Tkinter.

## Prerequisites

- Python 3.6+
- Tkinter (usually included with Python installations)
- pandas
- IP2Location

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Jayveerchauhan/IP-Tracker-.git
    cd IPTracer
    ```

2. Install the required Python packages:
    ```sh
    pip install pandas IP2Location
    ```

3. Ensure you have the IP2Location database file `database.BIN`.

4. Place the database file, along with `logo.png` in the project directory.

## Usage

1. Run the application:
    ```sh
    python IPTracer.py
    ```

2. Follow the GUI prompts:
    - Click "Upload IP Addresses File" to select a text file containing the IP addresses.
    - The tool will fetch the details and prompt you to save the results to a CSV file.

## Building the Executable

To create a standalone executable, use PyInstaller:

1. Install PyInstaller:
    ```sh
    pip install pyinstaller
    ```

2. Run the PyInstaller command:
    ```sh
    pyinstaller --name=IPTracer --onefile --add-data "logo.png;." --add-data "database.BIN;." IPTracer.py
    ```

3. The executable will be located in the `dist` directory.


- [IP2Location](https://www.ip2location.com/) for the geolocation database.
- The Python Software Foundation.
- [PyInstaller](https://www.pyinstaller.org/) for packaging the application.
