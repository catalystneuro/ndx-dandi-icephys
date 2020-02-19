from datetime import datetime
from pynwb import NWBFile, NWBHDF5IO
from ndx_dandi_icephys import LabMetaData_ext

nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone())

# Creates LabMetaData container
lab_metadata = LabMetaData_ext(
    name='LabMetaData',
    cell_id='cell_id',
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
