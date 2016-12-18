# Extract - Transform - Load

The etl pack is a directory layout to support my ETL processing framework for
small scale data science projects (local machine).

## etl.py

Since git does not track empty directories, a `make.py` script is included to
initialize the etl pack. This must be run before generating templates with
jetpack.

    python make.py
