# ndx-labmetadata-abf extension for NWB:N

Extension of the [lab_meta_data](https://pynwb.readthedocs.io/en/stable/pynwb.file.html#pynwb.file.NWBFile.lab_meta_data) field.

[![PyPI version]()

[Python Installation](#python-installation)

[Python Usage](#python-usage)

### Python Installation
```bash
pip install git+https://github.com/ben-dichter-consulting/ndx-labmetadata-abf.git
```

### Python Usage

```python
from datetime import datetime
from pynwb import NWBFile, NWBHDF5IO
from ndx_labmetadata_abf import LabMetaData_ext

nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone())

# Creates LabMetaData container
lab_metadata = LabMetaData_ext(
    name='LabMetaData',
    cell_id='cell_id',
    tissue_sample_id='tissue_sample_id',
)

# Add to file
nwb.add_lab_meta_data(lab_metadata)

# Write nwb file
with NWBHDF5IO('test_labmetadata.nwb', 'w') as io:
    io.write(nwb)

# Read nwb file and check its content
with NWBHDF5IO('test_labmetadata.nwb', 'r', load_namespaces=True) as io:
    nwb = io.read()
    print(nwb.lab_meta_data['LabMetaData'])
```
