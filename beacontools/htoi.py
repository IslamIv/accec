def s16(value):
    return -(value & 0x8000) | (value & 0x7fff)
