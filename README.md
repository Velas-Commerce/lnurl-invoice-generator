# LNURL Invoice Generator

This script generates a Lightning Network invoice using the LNURL-Pay protocol. The user is prompted to input an amount in satoshis, which is then used to generate an invoice.

## Prerequisites

- Python 3.11.3 or newer
- Pip (Python Package Installer)

## Setup

1.  Install the required Python libraries by running `pip install -r requirements.txt`.

2.  Set the `LNURL_LINK` environment variable in a `.env` file in the root directory of the project. The `.env` file should look like this:

    LNURL_LINK=your_lnurl_link_here

    Replace `your_lnurl_link_here` with your actual lnurl link.

3.  Activate the virtual envrionment:

```
Windows:
$ .\venv\Scripts\Activate

Mac / Linux:
$ source venv/bin/activate
```

4. Run the script by executing `python lnurl-invoice-generator.py`
   You'll be prompted to enter an amount in satoshis.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
