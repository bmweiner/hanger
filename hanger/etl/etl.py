"""Create ETL directories and README."""

import os

try:
    os.mkdir('etl')
except FileExistsError as e:
    msg = "existing etl directory found, must delete before proceeding."
    raise FileExistsError(msg)

directories = {
    ('local',):'Local storage for data files obtained manually',
    ('stage',):'Transient staging area for data files',
    ('stage', 'src'):'Landing zone for raw source data',
    ('stage', 'tmp'):'Landing zone for intermediate processed data tables',
    ('stage', 'tbl'):'Landing zone for final data tables',
    ('extract',):'Scripts to move src files to stage/src',
    ('transform',):'Scripts to transform src files',
    ('transform','prep'):'Scripts to pre-process src files (stage/tmp)',
    ('transform','build'):'Scripts to build final tables (stage/tbl)',
    ('load',):'Scripts to load tables from stage/tbl to production system',
}

paths = [os.path.join('etl', *k) for k in directories.keys()]
for path in paths:
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

readme = {}
readme['header'] = ['# ETL {{name}}\n\n']

readme['tree'] = ['## Directory Structure\n\n']
for dirpath, dirnames, filenames in os.walk('etl'):
    if not dirnames and not filenames:
        k = tuple(dirpath.split('\\'))[1:]
        readme['tree'].append('* **' + dirpath + '** ' + directories[k] + '\n')
readme['tree'].append('\n')

readme['best'] = ['## Best Practices\n\n']
readme['best'].append('### Extract\n\n')
readme['best'].append('### Transform\n\n')
readme['best'].append('### Load\n\n')

with open(os.path.join('etl', 'README.md'), 'w') as f:
    f.writelines(readme['header'])
    f.writelines(readme['tree'])
    f.writelines(readme['best'])
