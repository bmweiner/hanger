# Extract - Transform - Load

## Pack

The etl pack is a directory layout to support my ETL processing framework for
small scale data science projects (local machine).

### etl.py

Since git does not track empty directories, a `make.py` script is included to
initialize the etl pack. This must be run before generating templates with
jetpack.

    python make.py

## ETL Framework

This ETL processing framework supports data readiness for small scale data
science projects (local machine). The framework provides a directory structure
for storing data and logic (scripts) and standards for workflow. This framework
is designed for data science projects with static data requirements. Projects
that require dynamic or near real-time data should use different methods.

### Directory Structure

  * **etl\extract** Scripts to move src files to stage/src
  * **etl\load** Scripts to load tables from stage/tbl to production system
  * **etl\local** Local storage for source files obtained manually
  * **etl\stage\src** Landing zone for raw source files
  * **etl\stage\tbl** Landing zone for final data tables
  * **etl\stage\tmp** Landing zone for intermediate processed data tables
  * **etl\transform\build** Scripts to build final tables (stage/tbl)
  * **etl\transform\prep** Scripts to pre-process src files (stage/tmp)

### Workflow

This workflow is listed in sequence of task execution [extract, transform-prep,
transform-build, load]. Dependencies should exist from task to task, but not
within a task. For mutli-person teams, work can be divided by task and/or
system. For example, with systems {x,y} and staff {a,b,c}:

Table 1: divided by system

| | E | T | L |
|---|---|---|---|
| x | a | a | a |
| y | b | b | b |

Table 2: divided by task

| | E | T | L |
|---|---|---|---|
| x | a | b | c |
| y | a | b | c |

#### Data

  * The stage is a transient area used to store files transferred from external
    systems, intermediate tables, and final tables
  * The stage is designed to be deleted or overwritten as ETL scripts
    re-create the content at runtime
  * Source files obtained manually (e.g. email attachment) should be stored in
    the `etl\local` directory
  * The `etl\local` directory should not be deleted at runtime

#### Extract

| Script Repository | `etl\extract` |
|:---|:---|
| Data Source | external or `etl\local`|
| Data Destination | `etl\stage\src`|

  * An extract script transfers source files from an external source or the
    `etl\local` directory to the `etl\stage\src` directory on the local machine
  * Generally one extract script can be created for each system or file
  * Name scripts according to the external system or system and file (e.g.
    uci.py or uci_iris.py)

#### Transform

  * Transform scripts prepare intermediate tables and build final tables

##### Transform - Prep

| Script Repository | `etl\transform\prep` |
|:---|:---|
| Data Source | `etl\stage\src` |
| Data Destination | `etl\stage\tmp` |

  * A prep script performs common pre-build steps on a source file such as
    format conversion and column name standardization
  * Prep scripts are useful to limit repetition in build scripts (e.g. when a
    single source file is used to build multiple tables)
  * Name scripts according to the source file (e.g. iris.py)

##### Transform - Build

| Script Repository | `etl\transform\build` |
|:---|:---|
| Data Source | `etl\stage\src` or `etl\stage\tmp` |
| Data Destination | `etl\stage\tbl` |

  * A build script creates the final table and contains steps such as joins,
    reshaping, conversion, and casting
  * A single build script should exist for each table
  * Name scripts according to the final table name (e.g. iris.py)

#### Load

| Script Repository | `etl\load` |
|:---|:---|
| Data Source | `etl\stage\tbl` |
| Data Destination | data repository |

  * A load script transfers final tables from `etl\stage\tbl` to the project
    data repository, likely at a location accessible to the team
