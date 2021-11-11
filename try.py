ipeline()
cfg = rs.config()
cfg.enable_device_from_file(r"C:\Users\Gianmy\Desktop\Coding\Test\bin22_d435_C_20210729_151839.bag") ##Works only with .bag files in C:/
profile = pipe.start(cfg)
playback = profile.get_device().as_playback()


ddd = profile.get_stream(rs.stream.depth)
intr = ddd.get_intrinsic()
print(intr)