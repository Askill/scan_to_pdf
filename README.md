# scan to pdf

read files from "front" and "back" dirs, assume that the stack of appaers has simply been moved to the scan bed again without shuffeling and merge the files into a pdf.

Quick and dirty, using img2pdf and pdftk.

*Do not use outside of trusted environment.*

## Requirements

- pdftk
- img2pdf
  
## Run

    python -m virtualenv venv
    # venv/scripts/Activate.ps1
    # source venv/bin/activate
    pip install -r requirements.txt

    python combine.py