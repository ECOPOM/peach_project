import cv2

ddd = profile.get_stream(rs.stream.depth)
intr = ddd.get_intrinsic()
print(intr)
