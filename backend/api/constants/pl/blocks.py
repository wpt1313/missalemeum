from ..la.blocks import *


SANCTI = (
    constants.SANCTI_01_01,
    constants.SANCTI_01_05,
    constants.SANCTI_01_06,
    constants.SANCTI_01_11,
    constants.SANCTI_01_13,
    constants.SANCTI_01_14,
    constants.SANCTI_01_14C,
    constants.SANCTI_01_15,
    constants.SANCTI_01_15C,
    constants.SANCTI_01_16,
    constants.SANCTI_01_17,
    constants.SANCTI_01_18,
    constants.SANCTI_01_19,
    constants.SANCTI_01_19C,
    constants.SANCTI_01_20,
    constants.SANCTI_01_21,
    constants.SANCTI_01_22,
    constants.SANCTI_01_23,
    constants.SANCTI_01_23C,
    constants.SANCTI_01_24,
    constants.SANCTI_01_25,
    constants.SANCTI_01_25C,
    constants.SANCTI_01_26,
    constants.SANCTI_01_27,
    constants.SANCTI_01_28,
    constants.SANCTI_01_28C,
    constants.SANCTI_01_29,
    constants.SANCTI_01_30,
    constants.SANCTI_01_31,
    constants.SANCTI_02_01,
    constants.SANCTI_02_02,
    constants.SANCTI_02_03,
    constants.SANCTI_02_04,
    constants.SANCTI_02_05,
    constants.SANCTI_02_06,
    constants.SANCTI_02_06C,
    constants.SANCTI_02_07,
    constants.SANCTI_02_08,
    constants.SANCTI_02_09,
    constants.SANCTI_02_09C,
    constants.SANCTI_02_10,
    constants.SANCTI_02_11,
    constants.SANCTI_02_12,
    constants.SANCTI_02_14,
    constants.SANCTI_02_15,
    constants.SANCTI_02_18,
    constants.SANCTI_02_22,
    constants.SANCTI_02_22C,
    constants.SANCTI_02_23,
    constants.SANCTI_02_24,
    constants.SANCTI_02_27,
    constants.SANCTI_03_04,
    constants.SANCTI_03_04C,
    constants.SANCTI_03_06,
    constants.SANCTI_03_07,
    constants.SANCTI_03_08,
    constants.SANCTI_03_09,
    constants.SANCTI_03_10,
    constants.SANCTI_03_12,
    constants.SANCTI_03_15PL,
    constants.SANCTI_03_17,
    constants.SANCTI_03_18,
    constants.SANCTI_03_19,
    constants.SANCTI_03_21,
    constants.SANCTI_03_24,
    constants.SANCTI_03_25,
    constants.SANCTI_03_27,
    constants.SANCTI_03_28,
    constants.SANCTI_04_11,
    constants.SANCTI_04_13,
    constants.SANCTI_04_14,
    constants.SANCTI_04_17,
    constants.SANCTI_04_21,
    constants.SANCTI_04_22,
    constants.SANCTI_04_23PL,
    constants.SANCTI_04_24,
    constants.SANCTI_04_25,
    constants.SANCTI_04_25C,
    constants.SANCTI_04_26,
    constants.SANCTI_04_27,
    constants.SANCTI_04_28,
    constants.SANCTI_04_29,
    constants.SANCTI_04_30,
    constants.SANCTI_05_01,
    constants.SANCTI_05_02,
    constants.SANCTI_05_03PL,
    constants.SANCTI_05_04PL,
    constants.SANCTI_05_04,
    constants.SANCTI_05_05,
    constants.SANCTI_05_08PL,
    constants.SANCTI_05_09,
    constants.SANCTI_05_10,
    constants.SANCTI_05_10C,
    constants.SANCTI_05_11,
    constants.SANCTI_05_12,
    constants.SANCTI_05_13,
    constants.SANCTI_05_14,
    constants.SANCTI_05_15,
    constants.SANCTI_05_16,
    constants.SANCTI_05_16PL,
    constants.SANCTI_05_17,
    constants.SANCTI_05_18,
    constants.SANCTI_05_19,
    constants.SANCTI_05_19C,
    constants.SANCTI_05_20,
    constants.SANCTI_05_24PL,
    constants.SANCTI_05_25,
    constants.SANCTI_05_26,
    constants.SANCTI_05_26C,
    constants.SANCTI_05_27,
    constants.SANCTI_05_27C,
    constants.SANCTI_05_28,
    constants.SANCTI_05_29,
    constants.SANCTI_05_30,
    constants.SANCTI_05_31,
    constants.SANCTI_05_31C,
    constants.SANCTI_06_01,
    constants.SANCTI_06_02,
    constants.SANCTI_06_04,
    constants.SANCTI_06_05,
    constants.SANCTI_06_06,
    constants.SANCTI_06_09,
    constants.SANCTI_06_10,
    constants.SANCTI_06_10PL,
    constants.SANCTI_06_11,
    constants.SANCTI_06_12,
    constants.SANCTI_06_12C,
    constants.SANCTI_06_13,
    constants.SANCTI_06_14,
    constants.SANCTI_06_15PL,
    constants.SANCTI_06_15,
    constants.SANCTI_06_17,
    constants.SANCTI_06_18,
    constants.SANCTI_06_18C,
    constants.SANCTI_06_19,
    constants.SANCTI_06_19C,
    constants.SANCTI_06_20,
    constants.SANCTI_06_21,
    constants.SANCTI_06_22,
    constants.SANCTI_06_23,
    constants.SANCTI_06_24,
    constants.SANCTI_06_25,
    constants.SANCTI_06_26,
    constants.SANCTI_06_28,
    constants.SANCTI_06_29,
    constants.SANCTI_06_30,
    constants.SANCTI_07_01,
    constants.SANCTI_07_02,
    constants.SANCTI_07_02C,
    constants.SANCTI_07_03,
    constants.SANCTI_07_05,
    constants.SANCTI_07_07,
    constants.SANCTI_07_08,
    constants.SANCTI_07_10,
    constants.SANCTI_07_11,
    constants.SANCTI_07_12,
    constants.SANCTI_07_12C,
    constants.SANCTI_07_13PL,
    constants.SANCTI_07_14,
    constants.SANCTI_07_15PL,
    constants.SANCTI_07_15,
    constants.SANCTI_07_16,
    constants.SANCTI_07_17,
    constants.SANCTI_07_18PL,
    constants.SANCTI_07_18,
    constants.SANCTI_07_18C,
    constants.SANCTI_07_19,
    constants.SANCTI_07_20PL,
    constants.SANCTI_07_20C,
    constants.SANCTI_07_20,
    constants.SANCTI_07_21,
    constants.SANCTI_07_21C,
    constants.SANCTI_07_22,
    constants.SANCTI_07_23,
    constants.SANCTI_07_23C,
    constants.SANCTI_07_24,
    constants.SANCTI_07_24PL,
    constants.SANCTI_07_25,
    constants.SANCTI_07_25C,
    constants.SANCTI_07_26,
    constants.SANCTI_07_27,
    constants.SANCTI_07_28,
    constants.SANCTI_07_29,
    constants.SANCTI_07_29C,
    constants.SANCTI_07_30,
    constants.SANCTI_07_31,
    constants.SANCTI_08_01,
    constants.SANCTI_08_02,
    constants.SANCTI_08_02C,
    constants.SANCTI_08_04,
    constants.SANCTI_08_05,
    constants.SANCTI_08_06,
    constants.SANCTI_08_06C,
    constants.SANCTI_08_07,
    constants.SANCTI_08_07C,
    constants.SANCTI_08_08,
    constants.SANCTI_08_08C,
    constants.SANCTI_08_09,
    constants.SANCTI_08_09C,
    constants.SANCTI_08_10,
    constants.SANCTI_08_11,
    constants.SANCTI_08_12,
    constants.SANCTI_08_13,
    constants.SANCTI_08_14,
    constants.SANCTI_08_14C,
    constants.SANCTI_08_15,
    constants.SANCTI_08_16,
    constants.SANCTI_08_17,
    constants.SANCTI_08_18,
    constants.SANCTI_08_19,
    constants.SANCTI_08_20,
    constants.SANCTI_08_21,
    constants.SANCTI_08_22,
    constants.SANCTI_08_22C,
    constants.SANCTI_08_23,
    constants.SANCTI_08_24,
    constants.SANCTI_08_25,
    constants.SANCTI_08_26PL,
    constants.SANCTI_08_27,
    constants.SANCTI_08_28,
    constants.SANCTI_08_28C,
    constants.SANCTI_08_29,
    constants.SANCTI_08_29C,
    constants.SANCTI_08_30,
    constants.SANCTI_08_30C,
    constants.SANCTI_08_31,
    constants.SANCTI_09_01PL,
    constants.SANCTI_09_02,
    constants.SANCTI_09_03,
    constants.SANCTI_09_05,
    constants.SANCTI_09_07PL,
    constants.SANCTI_09_08,
    constants.SANCTI_09_08C,
    constants.SANCTI_09_09,
    constants.SANCTI_09_10,
    constants.SANCTI_09_11,
    constants.SANCTI_09_12,
    constants.SANCTI_09_14,
    constants.SANCTI_09_15,
    constants.SANCTI_09_15C,
    constants.SANCTI_09_16,
    constants.SANCTI_09_16C,
    constants.SANCTI_09_17,
    constants.SANCTI_09_18,
    constants.SANCTI_09_19,
    constants.SANCTI_09_20,
    constants.SANCTI_09_21,
    constants.SANCTI_09_22,
    constants.SANCTI_09_22C,
    constants.SANCTI_09_23,
    constants.SANCTI_09_23C,
    constants.SANCTI_09_24,
    constants.SANCTI_09_25PL,
    constants.SANCTI_09_26,
    constants.SANCTI_09_27,
    constants.SANCTI_09_28,
    constants.SANCTI_09_29,
    constants.SANCTI_09_30,
    constants.SANCTI_10_01,
    constants.SANCTI_10_01PL,
    constants.SANCTI_10_02,
    constants.SANCTI_10_03,
    constants.SANCTI_10_04,
    constants.SANCTI_10_05,
    constants.SANCTI_10_06,
    constants.SANCTI_10_07,
    constants.SANCTI_10_07C,
    constants.SANCTI_10_08,
    constants.SANCTI_10_08C,
    constants.SANCTI_10_09,
    constants.SANCTI_10_09PL,
    constants.SANCTI_10_09C,
    constants.SANCTI_10_10,
    constants.SANCTI_10_10PL,
    constants.SANCTI_10_11,
    constants.SANCTI_10_13,
    constants.SANCTI_10_14,
    constants.SANCTI_10_15,
    constants.SANCTI_10_16,
    constants.SANCTI_10_17,
    constants.SANCTI_10_18,
    constants.SANCTI_10_19,
    constants.SANCTI_10_21PL,
    constants.SANCTI_10_20,
    constants.SANCTI_10_21C,
    constants.SANCTI_10_21,
    constants.SANCTI_10_23,
    constants.SANCTI_10_24,
    constants.SANCTI_10_25,
    constants.SANCTI_10_28,
    constants.SANCTI_11_01,
    constants.SANCTI_11_02_1,
    constants.SANCTI_11_02_2,
    constants.SANCTI_11_02_3,
    constants.SANCTI_11_04,
    constants.SANCTI_11_04C,
    constants.SANCTI_11_08,
    constants.SANCTI_11_09,
    constants.SANCTI_11_09C,
    constants.SANCTI_11_10,
    constants.SANCTI_11_10C,
    constants.SANCTI_11_11,
    constants.SANCTI_11_11C,
    constants.SANCTI_11_12PL,
    constants.SANCTI_11_13,
    constants.SANCTI_11_13PL,
    constants.SANCTI_11_14,
    constants.SANCTI_11_15,
    constants.SANCTI_11_16,
    constants.SANCTI_11_17PL,
    constants.SANCTI_11_17,
    constants.SANCTI_11_18,
    constants.SANCTI_11_19,
    constants.SANCTI_11_19C,
    constants.SANCTI_11_20PL,
    constants.SANCTI_11_20,
    constants.SANCTI_11_21,
    constants.SANCTI_11_22,
    constants.SANCTI_11_23,
    constants.SANCTI_11_23C,
    constants.SANCTI_11_24,
    constants.SANCTI_11_24C,
    constants.SANCTI_11_25,
    constants.SANCTI_11_26,
    constants.SANCTI_11_26C,
    constants.SANCTI_11_29,
    constants.SANCTI_11_30,
    constants.SANCTI_12_02PL,
    constants.SANCTI_12_02,
    constants.SANCTI_12_03,
    constants.SANCTI_12_04PL,
    constants.SANCTI_12_05,
    constants.SANCTI_12_06,
    constants.SANCTI_12_07,
    constants.SANCTI_12_08,
    constants.SANCTI_12_10,
    constants.SANCTI_12_11,
    constants.SANCTI_12_13,
    constants.SANCTI_12_16,
    constants.SANCTI_12_21,
    constants.SANCTI_12_24,
    constants.SANCTI_12_25_1,
    constants.SANCTI_12_25_2,
    constants.SANCTI_12_25_3,
    constants.SANCTI_12_26,
    constants.SANCTI_12_26C,
    constants.SANCTI_12_27,
    constants.SANCTI_12_27C,
    constants.SANCTI_12_28,
    constants.SANCTI_12_28C,
    constants.SANCTI_12_29,
    constants.SANCTI_12_29C,
    constants.SANCTI_12_31,
    constants.SANCTI_12_31C,
)

ALL_IDS = TEMPORA_IDS + list(SANCTI)
