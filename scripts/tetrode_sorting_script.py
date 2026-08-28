from pathlib import Path

import spikeinterface.full as si
from probeinterface import get_probe


file_path=r"../data/raw/sub-KM131_ses-20180116T184757_behavior+ecephys+image.nwb"

recording = si.read_nwb_recording(
    file_path=file_path,
    load_channel_properties=True,
)

probe = get_probe(
    manufacturer="cambridgeneurotech",
    probe_name="ASSY-77-H3",
)
probe.wiring_to_device('ASSY-77>Adpt.A64-Om32_2x-sm-NN>RHD2164')

recording= recording.set_probe(probe)

filtered_recording = si.bandpass_filter(
    recording, freq_min=300, freq_max=6000
)

cmr_recording = si.common_reference(
    filtered_recording, operator="median"
)

output_folder = Path("../reports/processed/dendi")

first_shank_recording = cmr_recording

sorting = si.run_sorter(
    "kilosort4",
    first_shank_recording,
    folder=output_folder,
    remove_existing_folder=True,
    do_CAR=False,
    highpass_cutoff=0.1,
    verbose=True,
)