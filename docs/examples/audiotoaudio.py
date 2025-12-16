from simplemp import transcode

transcode(
    input_file="/path/to/input.wav", output_file="/path/to/output.mp3",
    audio_encoder="wmav1", samplerate=11025, bitrate_audio=32000, sample_fmt="s16",
    mute=False, debug=False, overwrite=False, thread_count=3, thread_type="SLICE",
)