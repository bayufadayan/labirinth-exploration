from ursina import *
from random import randint


def Labirinth():
    # ************** PEMBUATAN LABIRINTH **************
    # Wall Pusat
    tinggi = 30

    wall_001 = Entity(
        model="cube",
        collider="box",
        texture="assets/Texture/textures/old_sandstone_02_diff_1k.jpg",
        color="#78787A",
        texture_scale=(2, 5),
        position=(-6.5, 0, -0.5),
        scale=(2, tinggi, 8),
    )


    wall_002 = duplicate(wall_001, position=(6.5, 0, -0.5), scale=(2, tinggi, 8))
    wall_003 = Entity(
        model="cube",
        collider="box",
        texture="assets/Texture/textures/old_sandstone_02_diff_1k.jpg",
        color="#78787A",
        texture_scale=(2, 7),
        position=(0, 0, -3.5),
        scale=(15, tinggi, 2),
    )
    wall_011 = duplicate(
        wall_001, position=(-11.5, 0, -5.5), scale=(2, tinggi, 28), texture_scale=(2, 3)
    )
    wall_012 = duplicate(
        wall_003, position=(1, 0, 7.5), scale=(23, tinggi, 2), texture_scale=(3, 2)
    )
    wall_013 = duplicate(wall_001, position=(11.5, 0, 3), scale=(2, tinggi, 7))
    wall_014 = duplicate(
        wall_003,
        position=(-7, 0, -8.5),
        scale=(7, tinggi, 2),
    )
    wall_015 = duplicate(wall_003, position=(6, 0, -8.5), scale=(13, tinggi, 2))
    wall_016 = duplicate(wall_001, position=(11.5, 0, -5), scale=(2, tinggi, 5))
    wall_021 = duplicate(wall_003, position=(-19.5, 0, 2.5), scale=(10, tinggi, 2))
    wall_022 = duplicate(
        wall_003, position=(-15.5, 0, -8), scale=(2, tinggi, 19), texture_scale=(2, 7)
    )
    wall_023 = duplicate(wall_003, position=(-19.5, 0, -6.5), scale=(2, tinggi, 16))
    wall_024 = duplicate(wall_003, position=(-23.5, 0, -0.5), scale=(2, tinggi, 4))
    wall_025 = duplicate(wall_001, position=(-23.5, 0, -13), scale=(2, tinggi, 13))
    wall_026 = duplicate(wall_001, position=(-17.5, 0, -18.5), scale=(10, tinggi, 2))

    wall_031 = duplicate(wall_001, position=(15, 0, -3.5), scale=(5, tinggi, 2))
    wall_032 = duplicate(wall_001, position=(18.5, 0, 7.5), scale=(6, tinggi, 2))
    wall_033 = duplicate(wall_001, position=(16.5, 0, 2), scale=(2, tinggi, 9))
    wall_034 = duplicate(wall_001, position=(20.5, 0, 0), scale=(2, tinggi, 13))
    wall_035 = duplicate(wall_001, position=(25.5, 0, 1), scale=(2, tinggi, 15))

    wall_041 = duplicate(
        wall_001,
        position=(7.5, 0, -12),
        scale=(2, tinggi, 5),
    )
    wall_042 = duplicate(
        wall_001,
        position=(-6.5, 0, -16),
        scale=(2, tinggi, 7),
    )
    wall_043 = duplicate(
        wall_001,
        position=(0.5, 0, -13.5),
        scale=(12, tinggi, 2),
    )
    wall_044 = duplicate(
        wall_001,
        position=(6, 0, -18.5),
        scale=(23, tinggi, 2),
    )
    wall_045 = duplicate(
        wall_001,
        position=(12.5, 0, -15.5),
        scale=(2, tinggi, 4),
    )
    wall_046 = duplicate(
        wall_001,
        position=(16.5, 0, -14.5),
        scale=(6, tinggi, 2),
    )
    wall_047 = duplicate(
        wall_001,
        position=(16.5, 0, -10),
        scale=(2, tinggi, 7),
    )
    wall_049 = duplicate(
        wall_001,
        position=(20.5, 0, -17),
        scale=(2, tinggi, 15),
    )
    wall_050 = duplicate(
        wall_001,
        position=(25.5, 0, -17),
        scale=(2, tinggi, 15),
    )
    wall_051 = duplicate(
        wall_001,
        position=(23, 0, -23.5),
        scale=(3, tinggi, 2),
    )
    wall_052 = duplicate(
        wall_001,
        position=(28, 0, -9.5),
        scale=(3, tinggi, 2),
    )
    wall_052 = duplicate(
        wall_001, position=(-4, 0, -23.5), scale=(41, tinggi, 2), texture_scale=(5, 5)
    )

    wall_061 = duplicate(
        wall_001,
        position=(-40.5, 0, -21.5),
        scale=(8, tinggi, 14),
    )
    wall_062 = duplicate(
        wall_001,
        position=(-40.5, 0, -10.5),
        scale=(8, tinggi, 2),
    )
    wall_063 = duplicate(
        wall_001,
        position=(-40.5, 0, -4),
        scale=(8, tinggi, 5),
    )
    wall_064 = duplicate(
        wall_001,
        position=(-38, 0, 2.5),
        scale=(13, tinggi, 2),
    )
    wall_071 = duplicate(
        wall_001,
        position=(-32.5, 0, -13),
        scale=(2, tinggi, 23),
    )
    wall_072 = duplicate(
        wall_001,
        position=(-30.5, 0, -23.5),
        scale=(2, tinggi, 2),
    )
    wall_073 = duplicate(
        wall_001,
        position=(-28.5, 0, -8),
        scale=(2, tinggi, 33),
    )
    wall_074 = duplicate(
        wall_001,
        position=(-34.5, 0, 7.5),
        scale=(10, tinggi, 2),
    )
    wall_075 = duplicate(
        wall_001,
        position=(-40.5, 0, 12.5),
        scale=(2, tinggi, 12),
    )
    wall_076 = duplicate(
        wall_001,
        position=(-40.5, 0, 25.5),
        scale=(2, tinggi, 8),
    )
    wall_077 = duplicate(
        wall_001,
        position=(-31, 0, 24.5),
        scale=(11, tinggi, 6),
    )
    wall_078 = duplicate(
        wall_001,
        position=(-24, 0, 25.5),
        scale=(3, tinggi, 4),
    )
    wall_079 = duplicate(
        wall_001,
        position=(-21.5, 0, 26.5),
        scale=(2, tinggi, 6),
    )
    wall_080 = duplicate(
        wall_001,
        position=(-31, 0, 17.5),
        scale=(17, tinggi, 2),
    )
    wall_081 = duplicate(
        wall_001,
        position=(-21.5, 0, 19),
        scale=(2, tinggi, 5),
    )
    wall_082 = duplicate(
        wall_001,
        position=(-10.5, 0, 20.5),
        scale=(20, tinggi, 2),
    )
    wall_083 = duplicate(
        wall_001,
        position=(1, 0, 24.5),
        scale=(3, tinggi, 10),
    )
    wall_090 = duplicate(
        wall_001,
        position=(18.5, 0, 24.5),
        scale=(16, tinggi, 4),
    )
    wall_091 = duplicate(
        wall_001,
        position=(25.5, 0, 17),
        scale=(2, tinggi, 11),
    )
    wall_092 = duplicate(
        wall_001,
        position=(16, 0, 12.5),
        scale=(17, tinggi, 2),
    )
    wall_093 = duplicate(
        wall_001,
        position=(6.5, 0, 20.5),
        scale=(2, tinggi, 18),
    )
    wall_094 = duplicate(
        wall_001,
        position=(-5.5, 0, 14),
        scale=(22, tinggi, 5),
    )
    wall_095 = duplicate(
        wall_001,
        position=(-21, 0, 7.5),
        scale=(13, tinggi, 2),
    )
    wall_096 = duplicate(
        wall_001,
        position=(-20, 0, 11.5),
        scale=(3, tinggi, 6),
    )
    wall_097 = duplicate(
        wall_001,
        position=(-25, 0, 13.5),
        scale=(3, tinggi, 6),
    )
    wall_098 = duplicate(
        wall_001,
        position=(-30, 0, 11.5),
        scale=(3, tinggi, 6),
    )
    wall_099 = duplicate(
        wall_001,
        position=(-35, 0, 13.5),
        scale=(3, tinggi, 6),
    )

    # wall Selatan
    wall_100 = duplicate(
        wall_001,
        position=(-46.5, 0, -75),
        scale=(12, tinggi, 3),
    )
    wall_101 = duplicate(
        wall_001,
        position=(-40.5, 0, -81),
        scale=(18, tinggi, 3),
    )
    wall_102 = duplicate(
        wall_001,
        position=(-30, 0, -76.5),
        scale=(3, tinggi, 18),
    )
    wall_103 = duplicate(
        wall_001,
        position=(-36, 0, -70.5),
        scale=(3, tinggi, 18),
    )
    wall_104 = duplicate(
        wall_001,
        position=(-43.5, 0, -69),
        scale=(12, tinggi, 3),
    )
    wall_105 = duplicate(
        wall_001,
        position=(-48, 0, -64.5),
        scale=(3, tinggi, 6),
    )
    wall_106 = duplicate(
        wall_001,
        position=(-43.5, 0, -63),
        scale=(6, tinggi, 3),
    )
    wall_107 = duplicate(
        wall_001,
        position=(-30, 0, -63),
        scale=(9, tinggi, 3),
    )
    wall_108 = duplicate(
        wall_001,
        position=(-24, 0, -69),
        scale=(3, tinggi, 27),
    )
    wall_109 = duplicate(
        wall_001,
        position=(-18, 0, -81),
        scale=(9, tinggi, 3),
    )
    wall_110 = duplicate(
        wall_001,
        position=(-12, 0, -75),
        scale=(3, tinggi, 15),
    )
    wall_111 = duplicate(wall_001, position=(-9, 0, -69), scale=(3, tinggi, 3))
    wall_112 = duplicate(
        wall_001,
        position=(-6, 0, -76.5),
        scale=(3, tinggi, 18),
    )
    wall_113 = duplicate(
        wall_001,
        position=(-48, 0, -52.5),
        scale=(3, tinggi, 12),
    )
    wall_114 = duplicate(
        wall_001,
        position=(-39, 0, -57),
        scale=(15, tinggi, 3),
    )
    wall_115 = duplicate(
        wall_001,
        position=(-30, 0, -54),
        scale=(3, tinggi, 9),
    )
    wall_116 = duplicate(
        wall_001,
        position=(-34.5, 0, -51),
        scale=(6, tinggi, 3),
    )
    wall_117 = duplicate(
        wall_001,
        position=(-42, 0, -49.5),
        scale=(3, tinggi, 12),
    )
    wall_118 = duplicate(
        wall_001,
        position=(-38.5, 0, -45),
        scale=(4, tinggi, 3),
    )
    wall_119 = duplicate(
        wall_001,
        position=(-35, 0, -40.5),
        scale=(3, tinggi, 12),
    )
    wall_120 = duplicate(
        wall_001,
        position=(-17.5, 0, -33),
        scale=(14, tinggi, 3),
    )
    wall_121 = duplicate(
        wall_001,
        position=(-29, 0, -40.5),
        scale=(3, tinggi, 12),
    )
    wall_122 = duplicate(
        wall_001,
        position=(-19, 0, -39),
        scale=(17, tinggi, 3),
    )
    wall_123 = duplicate(
        wall_001,
        position=(-17.5, 0, -45),
        scale=(20, tinggi, 3),
    )
    wall_124 = duplicate(
        wall_001,
        position=(-24, 0, -48),
        scale=(3, tinggi, 3),
    )
    wall_125 = duplicate(
        wall_001,
        position=(-19.5, 0, -51),
        scale=(12, tinggi, 3),
    )
    wall_126 = duplicate(
        wall_001,
        position=(-12, 0, -54),
        scale=(3, tinggi, 9),
    )
    wall_127 = duplicate(
        wall_001,
        position=(-16.5, 0, -57),
        scale=(6, tinggi, 3),
    )
    wall_128 = duplicate(
        wall_001,
        position=(-18, 0, -69),
        scale=(3, tinggi, 15),
    )
    wall_129 = duplicate(
        wall_001,
        position=(-12, 0, -63),
        scale=(9, tinggi, 3),
    )
    wall_130 = duplicate(
        wall_001,
        position=(-6, 0, -52.5),
        scale=(3, tinggi, 24),
    )
    wall_131 = duplicate(
        wall_001,
        position=(0, 0, -36),
        scale=(15, tinggi, 3),
    )
    wall_132 = duplicate(
        wall_001,
        position=(9, 0, -33),
        scale=(9, tinggi, 3),
    )
    wall_133 = duplicate(
        wall_001,
        position=(0, 0, -69),
        scale=(3, tinggi, 27),
    )
    wall_134 = duplicate(
        wall_001,
        position=(3, 0, -72),
        scale=(3, tinggi, 3),
    )
    wall_135 = duplicate(
        wall_001,
        position=(6, 0, -78),
        scale=(3, tinggi, 15),
    )
    wall_136 = duplicate(
        wall_001,
        position=(10.5, 0, -81),
        scale=(6, tinggi, 3),
    )
    wall_137 = duplicate(
        wall_001,
        position=(18, 0, -78),
        scale=(3, tinggi, 9),
    )
    wall_138 = duplicate(
        wall_001,
        position=(15, 0, -75),
        scale=(3, tinggi, 3),
    )
    wall_139 = duplicate(
        wall_001,
        position=(12, 0, -69),
        scale=(3, tinggi, 15),
    )
    wall_140 = duplicate(
        wall_001,
        position=(9, 0, -63),
        scale=(3, tinggi, 3),
    )
    wall_141 = duplicate(
        wall_001,
        position=(6, 0, -54),
        scale=(3, tinggi, 27),
    )
    wall_142 = duplicate(
        wall_001,
        position=(0, 0, -42),
        scale=(9, tinggi, 3),
    )
    wall_143 = duplicate(
        wall_001,
        position=(0, 0, -48),
        scale=(3, tinggi, 9),
    )
    wall_144 = duplicate(
        wall_001,
        position=(16.5, 0, -51),
        scale=(18, tinggi, 3),
    )
    wall_145 = duplicate(
        wall_001,
        position=(12, 0, -43.5),
        scale=(3, tinggi, 12),
    )
    wall_146 = duplicate(
        wall_001,
        position=(24, 0, -46.5),
        scale=(3, tinggi, 6),
    )
    wall_147 = duplicate(
        wall_001,
        position=(18, 0, -54),
        scale=(3, tinggi, 3),
    )
    wall_148 = duplicate(
        wall_001,
        position=(22.5, 0, -57),
        scale=(24, tinggi, 3),
    )
    wall_149 = duplicate(
        wall_001,
        position=(30, 0, -49.5),
        scale=(3, tinggi, 12),
    )
    wall_150 = duplicate(
        wall_001,
        position=(36, 0, -66),
        scale=(3, tinggi, 21),
    )
    wall_151 = duplicate(
        wall_001,
        position=(33, 0, -75),
        scale=(3, tinggi, 3),
    )
    wall_152 = duplicate(
        wall_001,
        position=(30, 0, -69),
        scale=(3, tinggi, 15),
    )
    wall_153 = duplicate(
        wall_001,
        position=(24, 0, -73.5),
        scale=(3, tinggi, 24),
    )
    wall_154 = duplicate(
        wall_001,
        position=(21, 0, -63),
        scale=(3, tinggi, 3),
    )
    wall_155 = duplicate(
        wall_001,
        position=(18, 0, -66),
        scale=(3, tinggi, 9),
    )
    wall_156 = duplicate(
        wall_001,
        position=(34.5, 0, -81),
        scale=(12, tinggi, 3),
    )
    wall_157 = duplicate(
        wall_001,
        position=(42, 0, -79.5),
        scale=(3, tinggi, 12),
    )
    wall_158 = duplicate(
        wall_001,
        position=(48, 0, -75),
        scale=(9, tinggi, 3),
    )
    wall_159 = duplicate(
        wall_001,
        position=(54, 0, -78),
        scale=(3, tinggi, 9),
    )
    wall_160 = duplicate(
        wall_001,
        position=(49.5, 0, -81),
        scale=(6, tinggi, 3),
    )
    wall_161 = duplicate(
        wall_001,
        position=(45, 0, -69),
        scale=(15, tinggi, 3),
    )
    wall_162 = duplicate(
        wall_001,
        position=(54, 0, -63),
        scale=(3, tinggi, 15),
    )
    wall_163 = duplicate(
        wall_001,
        position=(43.5, 0, -63),
        scale=(13, tinggi, 3),
    )
    wall_164 = duplicate(
        wall_001,
        position=(45, 0, -57),
        scale=(9, tinggi, 3),
    )
    wall_165 = duplicate(
        wall_001,
        position=(42, 0, -54),
        scale=(3, tinggi, 3),
    )
    wall_166 = duplicate(
        wall_001,
        position=(36, 0, -48),
        scale=(3, tinggi, 9),
    )
    wall_167 = duplicate(
        wall_001,
        position=(18, 0, -39),
        scale=(3, tinggi, 15),
    )
    wall_168 = duplicate(
        wall_001,
        position=(30, 0, -33),
        scale=(21, tinggi, 3),
    )
    wall_169 = duplicate(
        wall_001,
        position=(37, 0, -25.5),
        scale=(3, tinggi, 12),
    )
    wall_170 = duplicate(
        wall_001,
        position=(36, 0, -36),
        scale=(3, tinggi, 3),
    )
    wall_171 = duplicate(
        wall_001,
        position=(33, 0, -39),
        scale=(21, tinggi, 3),
    )
    wall_172 = duplicate(
        wall_001,
        position=(45, 0, -51),
        scale=(15, tinggi, 3),
    )
    wall_173 = duplicate(
        wall_001,
        position=(54, 0, -45),
        scale=(3, tinggi, 15),
    )
    wall_174 = duplicate(
        wall_001,
        position=(57, 0, -39),
        scale=(3, tinggi, 3),
    )
    wall_175 = duplicate(
        wall_001,
        position=(60, 0, -54),
        scale=(3, tinggi, 45),
    )
    wall_176 = duplicate(
        wall_001,
        position=(64, 0, -51),
        scale=(6, tinggi, 3),
    )
    wall_177 = duplicate(
        wall_001,
        position=(64, 0, -39),
        scale=(5, tinggi, 3),
    )
    wall_178 = duplicate(
        wall_001,
        position=(51, 0, -33),
        scale=(15, tinggi, 3),
    )
    wall_179 = duplicate(
        wall_001,
        position=(48, 0, -40.5),
        scale=(3, tinggi, 12),
    )
    wall_180 = duplicate(
        wall_001,
        position=(43.5, 0, -45),
        scale=(6, tinggi, 3),
    )
    wall_181 = duplicate(
        wall_001,
        position=(49, 0, -25.5),
        scale=(3, tinggi, 12),
    )
    wall_182 = duplicate(
        wall_001,
        position=(46, 0, -21),
        scale=(3, tinggi, 3),
    )
    wall_183 = duplicate(
        wall_001,
        position=(43, 0, -24),
        scale=(3, tinggi, 9),
    )
    wall_184 = duplicate(
        wall_001,
        position=(55, 0, -22.5),
        scale=(3, tinggi, 12),
    )
    wall_185 = duplicate(
        wall_001,
        position=(60, 0, -22.5),
        scale=(3, tinggi, 12),
    )
    wall_186 = duplicate(
        wall_001,
        position=(70, 0, -21),
        scale=(5, tinggi, 3),
    )
    wall_187 = duplicate(
        wall_001,
        position=(66, 0, -27),
        scale=(3, tinggi, 15),
    )
    wall_188 = duplicate(
        wall_001,
        position=(73, 0, -27),
        scale=(5, tinggi, 3),
    )
    wall_189 = duplicate(
        wall_001,
        position=(68.5, 0, -33),
        scale=(2, tinggi, 3),
    )
    wall_190 = duplicate(
        wall_001,
        position=(71, 0, -48),
        scale=(3, tinggi, 33),
    )
    wall_191 = duplicate(
        wall_001,
        position=(67, 0, -45),
        scale=(5, tinggi, 3),
    )
    wall_192 = duplicate(
        wall_001,
        position=(67, 0, -57),
        scale=(5, tinggi, 3),
    )
    wall_193 = duplicate(
        wall_001,
        position=(68.5, 0, -63),
        scale=(2, tinggi, 3),
    )
    wall_194 = duplicate(
        wall_001,
        position=(66, 0, -69),
        scale=(3, tinggi, 15),
    )
    wall_195 = duplicate(
        wall_001,
        position=(68.5, 0, -75),
        scale=(2, tinggi, 3),
    )
    wall_196 = duplicate(
        wall_001,
        position=(73, 0, -69),
        scale=(5, tinggi, 3),
    )
    wall_197 = duplicate(
        wall_001,
        position=(71, 0, -78),
        scale=(3, tinggi, 9),
    )
    wall_198 = duplicate(
        wall_001,
        position=(67, 0, -81),
        scale=(5, tinggi, 3),
    )
    wall_199 = duplicate(
        wall_001,
        position=(60, 0, -82.5),
        scale=(3, tinggi, 6),
    )

    # Wall Utara
    wall_200 = duplicate(
        wall_001,
        position=(19.5, 0, 83),
        scale=(2, tinggi, 5),
    )
    wall_201 = duplicate(
        wall_001,
        position=(21.5, 0, 81.5),
        scale=(2, tinggi, 2),
    )
    wall_202 = duplicate(
        wall_001,
        position=(23.5, 0, 79),
        scale=(2, tinggi, 7),
    )
    wall_203 = duplicate(
        wall_001,
        position=(19, 0, 76.5),
        scale=(7, tinggi, 2),
    )
    wall_204 = duplicate(
        wall_001,
        position=(14.5, 0, 74),
        scale=(2, tinggi, 7),
    )
    wall_205 = duplicate(
        wall_001,
        position=(20, 0, 71.5),
        scale=(9, tinggi, 2),
    )
    wall_206 = duplicate(
        wall_001,
        position=(21.5, 0, 66.5),
        scale=(12, tinggi, 2),
    )
    wall_207 = duplicate(
        wall_001,
        position=(14.5, 0, 63.5),
        scale=(2, tinggi, 8),
    )
    wall_208 = duplicate(
        wall_001,
        position=(18.5, 0, 49.5),
        scale=(2, tinggi, 28),
    )
    wall_209 = duplicate(
        wall_001,
        position=(14.5, 0, 48.5),
        scale=(2, tinggi, 16),
    )
    wall_210 = duplicate(
        wall_001,
        position=(20.5, 0, 55.5),
        scale=(2, tinggi, 2),
    )
    wall_211 = duplicate(
        wall_001,
        position=(15, 0, 36.5),
        scale=(5, tinggi, 2),
    )
    wall_212 = duplicate(
        wall_001,
        position=(9.5, 0, 40),
        scale=(2, tinggi, 15),
    )
    wall_213 = duplicate(
        wall_001,
        position=(9.5, 0, 64),
        scale=(2, tinggi, 27),
    )
    wall_214 = duplicate(
        wall_001,
        position=(7, 0, 60.5),
        scale=(3, tinggi, 2),
    )
    wall_215 = duplicate(
        wall_001,
        position=(4.5, 0, 66),
        scale=(2, tinggi, 13),
    )
    wall_216 = duplicate(
        wall_001,
        position=(9.5, 0, 81.5),
        scale=(12, tinggi, 2),
    )
    wall_217 = duplicate(
        wall_001,
        position=(9.5, 0, 84),
        scale=(2, tinggi, 3),
    )
    wall_218 = duplicate(
        wall_001,
        position=(-0.5, 0, 79),
        scale=(2, tinggi, 7),
    )
    wall_219 = duplicate(
        wall_001,
        position=(4.5, 0, 76.5),
        scale=(7, tinggi, 2),
    )
    wall_220 = duplicate(
        wall_001,
        position=(-0.5, 0, 64.5),
        scale=(2, tinggi, 16),
    )
    wall_221 = duplicate(
        wall_001,
        position=(-6.5, 0, 66),
        scale=(10, tinggi, 3),
    )
    wall_222 = duplicate(
        wall_001,
        position=(-4, 0, 60.5),
        scale=(5, tinggi, 2),
    )
    wall_223 = duplicate(
        wall_001,
        position=(-5.5, 0, 55.5),
        scale=(18, tinggi, 2),
    )
    wall_224 = duplicate(
        wall_001,
        position=(4.5, 0, 46),
        scale=(2, tinggi, 21),
    )
    wall_225 = duplicate(
        wall_001,
        position=(-0.5, 0, 44.5),
        scale=(2, tinggi, 14),
    )
    wall_226 = duplicate(
        wall_001,
        position=(-5.5, 0, 47.5),
        scale=(2, tinggi, 14),
    )
    wall_227 = duplicate(
        wall_001,
        position=(-10.5, 0, 44.5),
        scale=(2, tinggi, 14),
    )
    wall_228 = duplicate(
        wall_001,
        position=(-15.5, 0, 47),
        scale=(2, tinggi, 19),
    )
    wall_229 = duplicate(
        wall_001,
        position=(-8, 0, 36.5),
        scale=(9, tinggi, 2),
    )
    wall_230 = duplicate(
        wall_001,
        position=(-10.5, 0, 58),
        scale=(2, tinggi, 3),
    )
    wall_231 = duplicate(
        wall_001,
        position=(-15.5, 0, 60.5),
        scale=(12, tinggi, 2),
    )
    wall_232 = duplicate(
        wall_001,
        position=(-18, 0, 41.5),
        scale=(3, tinggi, 2),
    )
    wall_233 = duplicate(
        wall_001,
        position=(-20.5, 0, 48.5),
        scale=(2, tinggi, 16),
    )
    wall_234 = duplicate(
        wall_001,
        position=(-23, 0, 55.5),
        scale=(3, tinggi, 2),
    )
    wall_235 = duplicate(
        wall_001,
        position=(-25.5, 0, 66),
        scale=(2, tinggi, 23),
    )
    wall_236 = duplicate(
        wall_001,
        position=(-20.5, 0, 65.5),
        scale=(8, tinggi, 2),
    )
    wall_237 = duplicate(
        wall_001,
        position=(-15.5, 0, 71),
        scale=(2, tinggi, 13),
    )
    wall_238 = duplicate(
        wall_001,
        position=(-12, 0, 76.5),
        scale=(5, tinggi, 2),
    )
    wall_239 = duplicate(
        wall_001,
        position=(-9, 0, 71.5),
        scale=(5, tinggi, 2),
    )
    wall_240 = duplicate(
        wall_001,
        position=(-4.5, 0, 76.5),
        scale=(2, tinggi, 12),
    )
    wall_241 = duplicate(
        wall_001,
        position=(-13, 0, 81.5),
        scale=(13, tinggi, 2),
    )
    wall_242 = duplicate(
        wall_001,
        position=(-10.5, 0, 84),
        scale=(2, tinggi, 3),
    )
    wall_243 = duplicate(
        wall_001,
        position=(-20.5, 0, 76),
        scale=(2, tinggi, 13),
    )
    wall_244 = duplicate(
        wall_001,
        position=(-30.5, 0, 76.5),
        scale=(8, tinggi, 2),
    )
    wall_245 = duplicate(
        wall_001,
        position=(-30.5, 0, 80),
        scale=(2, tinggi, 5),
    )
    wall_246 = duplicate(
        wall_001,
        position=(-28, 0, 81.5),
        scale=(3, tinggi, 2),
    )
    wall_247 = duplicate(
        wall_001,
        position=(-25.5, 0, 83),
        scale=(2, tinggi, 5),
    )
    wall_248 = duplicate(
        wall_001,
        position=(-35.5, 0, 68.5),
        scale=(2, tinggi, 18),
    )
    wall_249 = duplicate(
        wall_001,
        position=(-38, 0, 60.5),
        scale=(3, tinggi, 2),
    )
    wall_250 = duplicate(
        wall_001,
        position=(-40.5, 0, 71),
        scale=(2, tinggi, 23),
    )
    wall_251 = duplicate(
        wall_001,
        position=(-37, 0, 81.5),
        scale=(5, tinggi, 2),
    )
    wall_252 = duplicate(
        wall_001,
        position=(-20.5, 0, 35),
        scale=(2, tinggi, 5),
    )
    wall_253 = duplicate(
        wall_001,
        position=(-23, 0, 36.5),
        scale=(3, tinggi, 2),
    )
    wall_254 = duplicate(
        wall_001,
        position=(-25.5, 0, 43.5),
        scale=(2, tinggi, 16),
    )
    wall_255 = duplicate(
        wall_001,
        position=(-30.5, 0, 56.5),
        scale=(2, tinggi, 32),
    )
    wall_256 = duplicate(
        wall_001,
        position=(-37, 0, 36.5),
        scale=(15, tinggi, 2),
    )
    wall_257 = duplicate(
        wall_001,
        position=(-38, 0, 55.5),
        scale=(13, tinggi, 2),
    )
    wall_258 = duplicate(
        wall_001,
        position=(-35.5, 0, 47.5),
        scale=(2, tinggi, 14),
    )
    wall_259 = duplicate(
        wall_001,
        position=(-40.5, 0, 47.5),
        scale=(2, tinggi, 14),
    )
    wall_260 = duplicate(
        wall_001,
        position=(-45.5, 0, 60.5),
        scale=(2, tinggi, 50),
    )
    wall_261 = duplicate(
        wall_001,
        position=(-54.5, 0, 81.5),
        scale=(10, tinggi, 2),
    )
    wall_262 = duplicate(
        wall_001,
        position=(-50.5, 0, 66),
        scale=(2, tinggi, 13),
    )
    wall_263 = duplicate(
        wall_001,
        position=(-53, 0, 71.5),
        scale=(3, tinggi, 2),
    )
    wall_264 = duplicate(
        wall_001,
        position=(-55.5, 0, 59),
        scale=(2, tinggi, 37),
    )
    wall_265 = duplicate(
        wall_001,
        position=(-50.5, 0, 55.5),
        scale=(8, tinggi, 2),
    )
    wall_266 = duplicate(
        wall_001,
        position=(-50.5, 0, 42),
        scale=(2, tinggi, 19),
    )
    wall_267 = duplicate(
        wall_001,
        position=(-57, 0, 36.5),
        scale=(5, tinggi, 2),
    )


    # RED Wall
    wall_R01 = duplicate(
        wall_001,
        position=(-40.5, 0, -37.5),
        scale=(2, 50, 12),
        color="#921818",
        texture_scale=(10, 10),
    )
    wall_R02 = duplicate(
        wall_R01, position=(-57.5, 0, -41.5), scale=(32, 50, 4), texture_scale=(40, 40)
    )
    wall_R03 = duplicate(
        wall_R01, position=(-76, 0, -5.5), scale=(5, 50, 76), texture_scale=(50, 50)
    )
    wall_R04 = duplicate(
        wall_R01, position=(-54.5, 0, -67.5), scale=(4, 50, 48), texture_scale=(40, 40)
    )
    wall_R05 = duplicate(
        wall_R01, position=(13.5, 0, -88.5), scale=(132, 50, 6), texture_scale=(50, 50)
    )
    wall_R06 = duplicate(
        wall_R01, position=(77.5, 0, -49), scale=(4, 50, 73), texture_scale=(40, 40)
    )
    wall_R07 = duplicate(
        wall_R01, position=(54, 0, -14.5), scale=(43, 50, 4), texture_scale=(40, 40)
    )
    wall_R08 = duplicate(
        wall_R01, position=(71.5, 0, 25.5), scale=(4, 50, 76), texture_scale=(40, 40)
    )
    wall_R09 = duplicate(
        wall_R01, position=(45.5, 0, 61.5), scale=(48, 50, 4), texture_scale=(40, 40)
    )
    wall_R10 = duplicate(
        wall_R01, position=(23.5, 0, 46), scale=(4, 50, 27), texture_scale=(40, 40)
    )
    wall_R11 = duplicate(
        wall_R01, position=(-18, 0, 87.5), scale=(91, 50, 4), texture_scale=(40, 40)
    )
    wall_R12 = duplicate(
        wall_R01, position=(-61.5, 0, 59), scale=(4, 50, 53), texture_scale=(40, 40)
    )
    wall_R13 = duplicate(
        wall_R01, position=(-60.5, 0, 30), scale=(26, 50, 5), texture_scale=(40, 40)
    )

    # purple wall
    wall_P01 = duplicate(
        wall_001,
        position=(31, 0, -3),
        scale=(3, 50, 51),
        color=color.violet,
        texture_scale=(9, 2),
    )
    wall_P02 = duplicate(
        wall_P01, position=(24.5, 0, -30), scale=(16, 50, 3), texture_scale=(15, 15)
    )
    wall_P03 = duplicate(
        wall_P01, position=(-17, 0, -30), scale=(61, 50, 3), texture_scale=(50, 50)
    )
    wall_P04 = duplicate(
        wall_P01, position=(-46, 0, -15), scale=(3, 50, 27), texture_scale=(20, 20)
    )
    wall_P05 = duplicate(
        wall_P01, position=(-46, 0, 17), scale=(3, 50, 31), texture_scale=(25, 25)
    )
    wall_P06 = duplicate(
        wall_P01, position=(-42, 0, 31), scale=(5, 50, 3), texture_scale=(10, 10)
    )
    wall_P07 = duplicate(
        wall_P01, position=(-26.5, 0, 31), scale=(20, 50, 3), texture_scale=(20, 20)
    )
    wall_P08 = duplicate(
        wall_P01,
        position=(8, 0, 31),
        scale=(43, 50, 3),
    )
    wall_P09 = duplicate(
        wall_P01,
        position=(-12, 0, 27),
        scale=(3, 50, 5),
    )
    wall_P10 = duplicate(
        wall_P01,
        position=(31, 0, 29.5),
        scale=(3, 50, 6),
    )
