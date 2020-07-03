from pynwb.spec import NWBNamespaceBuilder, NWBGroupSpec, export_spec
import os


def main():
    ns_builder = NWBNamespaceBuilder(doc='type for storing lab metadata',
                                     name='ndx-dandi-icephys',
                                     version='0.3.0',
                                     author='Luiz Tauffer and Ben Dichter',
                                     contact='ben.dichter@gmail.com')

    ns_builder.include_type('LabMetaData', namespace='core')
    ns_builder.include_type('Subject', namespace='core')

    CreSubject = NWBGroupSpec(
        doc='subject with Cre information',
        neurodata_type_def='CreSubject',
        neurodata_type_inc='Subject'
    )

    CreSubject.add_dataset(
        name='cre',
        doc='cre type',
        dtype='text',
        quantity='?'
    )

    LabMetaData_ext = NWBGroupSpec(
        name='DandiIcephysMetadata',
        doc='type for storing lab metadata',
        neurodata_type_def='DandiIcephysMetadata',
        neurodata_type_inc='LabMetaData',
    )

    for args in (('cell_id', 'text'),
                 ('slice_id', 'text'),
                 ('tissue_sample_id', 'text'),
                 ('targeted_layer', 'int'),
                 ('exon_reads', 'int'),
                 ('intron_reads', 'int'),
                 ('intergenic_reads', 'int'),
                 ('sequencing_batch', 'int'),
                 ('number_of_genes_detected', 'int'),
                 ('RNA_family', 'text'),
                 ('RNA_type', 'text'),
                 ('RNA_type_confidence', 'float'),
                 ('RNA_type_top3', 'text'),
                 ('ALM_VISp_top3', 'text'),
                 ('length', 'int', 'length in pb'),
                 ('yield', 'int', 'yield in (pg/ul)'),
                 ('hold_time', 'int', 'hold time in (min)'),
                 ('soma_depth_4x', 'float'),
                 ('soma_depth_um', 'float'),
                 ('cortical_thickness_4x', 'float'),
                 ('cortical_thickness_um', 'float'),
                 ('traced', 'text'),
                 ('exclusion_reason', 'text')):

        if len(args) == 2:
            name, dtype = args
            doc = name.replace('_', ' ')
        elif len(args) == 3:
            name, dtype, doc = args
        else:
            raise ValueError('bad number of args')

        LabMetaData_ext.add_dataset(
            name=name,
            doc=doc,
            dtype=dtype,
            quantity='?'
        )

    new_data_types = [LabMetaData_ext, CreSubject]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    main()
