from datetime import datetime
from pynwb import NWBFile, NWBHDF5IO
from ndx_dandi_icephys import DandiIcephysMetadata, CreSubject
import unittest


class TestExt(unittest.TestCase):
    def test_metadata(self):
        nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone())

        # Creates LabMetaData container
        lab_metadata = DandiIcephysMetadata(cell_id='my_cell_id')

        # Add to file
        nwb.add_lab_meta_data(lab_metadata)

        # Write nwb file
        with NWBHDF5IO('test_labmetadata.nwb', 'w') as io:
            io.write(nwb)

        # Read nwb file and check its content
        with NWBHDF5IO('test_labmetadata.nwb', 'r', load_namespaces=True) as io:
            nwb = io.read()
            assert(nwb.lab_meta_data['DandiIcephysMetadata'].cell_id == 'my_cell_id')

    def test_cre(self):
        nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone())

        nwb.subject = CreSubject(cre='AA')

        # Write nwb file
        with NWBHDF5IO('test_labmetadata.nwb', 'w') as io:
            io.write(nwb)

        # Read nwb file and check its content
        with NWBHDF5IO('test_labmetadata.nwb', 'r', load_namespaces=True) as io:
            nwb = io.read()
            assert (nwb.subject.cre == 'AA')

