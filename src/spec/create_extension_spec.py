from pynwb.spec import NWBNamespaceBuilder, NWBGroupSpec, export_spec
import os


def main():
    ns_builder = NWBNamespaceBuilder(doc='type for storing lab metadata',
                                     name='ndx-labmetadata-abf',
                                     version='0.1.1',
                                     author='Luiz Tauffer and Ben Dichter',
                                     contact='ben.dichter@gmail.com')

    ns_builder.include_type('LabMetaData', namespace='core')

    LabMetaData_ext = NWBGroupSpec(
        doc='type for storing lab metadata',
        neurodata_type_def='LabMetaData_ext',
        neurodata_type_inc='LabMetaData',
    )

    LabMetaData_ext.add_attribute(
        name='cell_id',
        doc='Cell id.',
        dtype='text',
        shape=None,
    )

    LabMetaData_ext.add_attribute(
        name='tissue_sample_id',
        doc='Tissue sample id.',
        dtype='text',
        shape=None,
    )

    new_data_types = [LabMetaData_ext]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    main()
