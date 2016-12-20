"""Create ETL assets."""

import os

# directories
try:
    os.mkdir('etl')
except FileExistsError as e:
    msg = "existing etl directory found, must delete before proceeding."
    raise FileExistsError(msg)

directories = [
    ('local',),
    ('stage',),
    ('stage', 'src'),
    ('stage', 'tmp'),
    ('stage', 'tbl'),
    ('extract',),
    ('transform',),
    ('transform','prep'),
    ('transform','build'),
    ('load',),
]

paths = [os.path.join('etl', *k) for k in directories]
for path in paths:
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

# readme
with open('README.md', 'r') as f:
    readme = f.read()

with open(os.path.join('etl', 'README.md'), 'w') as f:
    f.write(readme[readme.find('## ETL Framework'):])

# gitignore
